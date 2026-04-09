#!/usr/bin/env python3
"""
LLM4Rec Wiki CLI — 用于维护 LLM+RecSys 知识库的工具。

通过 OpenAI 兼容 SDK 使用阿里云百炼（Bailian）Qwen 模型。
支持标准 DashScope 密钥和 Coding Plan 密钥（sk-sp-*）。

命令：
    ingest <source_file>          — 处理新的源文档
    query "<question>"            — 向知识库提问
    fetch <url> [--no-ingest]     — 从 URL 抓取网页并分析更新知识库
    lint                          — 健康检查知识库
    summarize                     — 生成当前知识库状态摘要
    validate                      — 检查 API 密钥和连接状态
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

# 加载 .env 文件（如果存在）（项目根目录 = tools/ 的父目录）
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

# 网页抓取依赖
try:
    import requests
except ImportError:
    print("警告：未找到 requests 包。fetch 命令将不可用。安装：pip install requests")
    requests = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("警告：未找到 beautifulsoup4 包。fetch 命令将不可用。安装：pip install beautifulsoup4")
    BeautifulSoup = None

# 使用 OpenAI 兼容 SDK（同时支持标准密钥和 Coding Plan 密钥）
try:
    from openai import OpenAI
except ImportError:
    print("错误：未找到 openai 包。请安装：pip install openai")
    sys.exit(1)


# ─── Configuration ───────────────────────────────────────────────────────────

WIKI_ROOT = Path(__file__).parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
RAW_DIR = WIKI_ROOT / "raw"
SCHEMA_FILE = WIKI_ROOT / "AGENTS.md"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

API_KEY = os.environ.get("DASHSCOPE_API_KEY", "").strip().strip('"').strip("'")

if not API_KEY:
    print("错误：未设置 DASHSCOPE_API_KEY 环境变量。")
    print("请从这里获取密钥：https://bailian.console.aliyun.com/")
    sys.exit(1)

# 自动检测密钥类型并相应配置
IS_CODING_PLAN = API_KEY.startswith("sk-sp-")

if IS_CODING_PLAN:
    # Coding Plan 密钥 — 使用 Coding 专用端点和模型
    BASE_URL = "https://coding.dashscope.aliyuncs.com/v1"
    MODEL_DEFAULT = os.environ.get("BAILIAN_MODEL", "qwen3.6-plus")
    print(f"🔑 检测到 Coding Plan 密钥，使用模型：{MODEL_DEFAULT}")
else:
    # 标准 DashScope 密钥 — 使用常规端点
    BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    MODEL_DEFAULT = os.environ.get("BAILIAN_MODEL", "qwen-max")


def get_client():
    """为当前密钥类型创建 OpenAI 兼容客户端。"""
    return OpenAI(api_key=API_KEY, base_url=BASE_URL)


def validate_api_key():
    """通过最小化请求测试 API 密钥。"""
    client = get_client()
    model = "qwen3.5-plus" if IS_CODING_PLAN else "qwen-turbo"
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "hi"}],
            max_tokens=5,
        )
        print(f"✅ API 密钥有效！（模型：{model}）")
        print(f"   密钥类型：{'Coding Plan' if IS_CODING_PLAN else '标准 DashScope'}")
        print(f"   响应：{resp.choices[0].message.content}")
        return True
    except Exception as e:
        err_str = str(e)
        if "invalid_api_key" in err_str or "Incorrect API key" in err_str:
            print("❌ API 密钥无效！")
            print(f"   密钥前缀：{API_KEY[:12]}...")
            print(f"   密钥类型：{'Coding Plan (sk-sp-*)' if IS_CODING_PLAN else '标准 (sk-*)'}")
            print(f"   端点：{BASE_URL}")
            print(f"   错误：{e}")
            return False
        elif "not supported" in err_str and "model" in err_str:
            print(f"❌ 模型 '{model}' 不支持此密钥类型。")
            if IS_CODING_PLAN:
                print("   Coding Plan 支持的模型：qwen3.5-plus, qwen3-coder-plus, qwen3-coder-next, kimi-k2.5, glm-5, MiniMax-M2.5")
            return False
        else:
            print(f"⚠️  意外错误：{e}")
            return True


# ─── LLM Interface ───────────────────────────────────────────────────────────

def call_llm(prompt: str, system_prompt: str = "", model: str = None,
             temperature: float = 0.3, max_tokens: int = 16384) -> str:
    """调用百炼 LLM API 并返回响应文本。"""
    model = model or MODEL_DEFAULT
    client = get_client()

    # 限制 max_tokens 在模型允许范围内
    max_tokens = min(max_tokens, 65536)

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content or ""

    except Exception as e:
        print(f"\n❌ LLM API 错误：{e}")
        return ""


def call_llm_stream(prompt: str, system_prompt: str = "", model: str = None):
    """流式返回百炼 LLM 响应。"""
    model = model or MODEL_DEFAULT
    client = get_client()

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    except Exception as e:
        print(f"\n❌ LLM 流式错误：{e}")


# ─── Web Fetch & Conversion ─────────────────────────────────────────────────

def is_pdf_url(url: str) -> bool:
    """检测 URL 是否指向 PDF 文件。"""
    parsed = urlparse(url)
    path = parsed.path.lower()
    query = parsed.query.lower()
    # 检查路径后缀
    if path.endswith('.pdf'):
        return True
    # 检查 arXiv PDF 路径模式
    if re.match(r'/pdf/\d+\.\d+(?:v\d+)?$', parsed.path):
        return True
    # 检查查询参数
    if 'pdf' in query and ('download' in query or 'format' in query):
        return True
    return False


def convert_pdf_to_html_url(url: str) -> tuple[str, str]:
    """尝试将 PDF URL 转换为 HTML 页面 URL。

    返回: (转换后的URL, 来源类型)
    来源类型: "html" 或 "pdf"（无法转换时保持原 URL 用于后续 PDF 解析）
    """
    parsed = urlparse(url)
    path = parsed.path

    # arXiv: /pdf/2411.11739 → /abs/2411.11739
    match = re.match(r'/pdf/(\d+\.\d+)(?:v\d+)?\.?pdf?$', path)
    if match:
        paper_id = match.group(1)
        return f'https://arxiv.org/abs/{paper_id}', 'html'

    # arXiv PDF 下载路径带版本: /pdf/2411.11739v1
    match = re.match(r'/pdf/(\d+\.\d+)(?:v\d+)?$', path)
    if match:
        paper_id = match.group(1)
        return f'https://arxiv.org/abs/{paper_id}', 'html'

    # OpenReview: /pdf?id=xxx → /forum?id=xxx
    if 'openreview.net' in parsed.netloc and '/pdf' in path:
        forum_url = url.replace('/pdf?', '/forum?').replace('/pdf', '/forum')
        return forum_url, 'html'

    # ACL Anthology: /pdf/xxx → /xxx/ (去掉 /pdf/)
    if 'aclanthology.org' in parsed.netloc and '/pdf/' in path:
        html_path = path.replace('/pdf/', '/')
        return f'{parsed.scheme}://{parsed.netloc}{html_path}', 'html'

    # 其他 PDF 文件：尝试去掉 .pdf 后缀
    if path.endswith('.pdf'):
        base = path[:-4]
        return f'{parsed.scheme}://{parsed.netloc}{base}', 'html'

    # 如果无法转换为 HTML，返回原 URL 标记为 PDF
    return url, 'pdf'


def download_and_parse_pdf(url: str, timeout: int = 60) -> tuple[str, str]:
    """下载 PDF 并使用 PyMuPDF 提取文本内容。

    返回: (提取的文本, 来源URL)
    """
    if requests is None:
        print("❌ 缺少 requests 库。请安装：pip install requests")
        sys.exit(1)

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("❌ 缺少 PyMuPDF 库。请安装：pip install pymupdf")
        print("   或者改用 HTML 页面 URL（如 arXiv 用 /abs/ 而非 /pdf/）")
        sys.exit(1)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36",
    }

    print(f"📥 正在下载 PDF：{url}")
    resp = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    resp.raise_for_status()

    print(f"✅ PDF 下载完成，大小：{len(resp.content) / 1024:.1f} KB")

    # 使用 PyMuPDF 提取文本
    try:
        doc = fitz.open(stream=resp.content, filetype="pdf")
        text_parts = []
        title = ""

        # 尝试从元数据获取标题
        metadata = doc.metadata
        if metadata and metadata.get('title'):
            title = metadata['title'].strip()

        # 提取每页文本
        for i, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                text_parts.append(f"## 第 {i+1} 页\n\n{text.strip()}")

        doc.close()

        full_text = "\n\n".join(text_parts)
        print(f"✅ PDF 文本提取完成，共 {len(text_parts)} 页，{len(full_text)} 字符")

        if not title and text_parts:
            # 尝试从第一页提取标题（通常是前几行）
            first_page = text_parts[0]
            lines = [l.strip() for l in first_page.split('\n') if l.strip()]
            if lines:
                title = lines[0]

        return full_text, title

    except Exception as e:
        print(f"❌ PDF 解析失败：{e}")
        return "", ""


def fetch_webpage(url: str, timeout: int = 30) -> tuple[str, str, str]:
    """抓取网页并返回 (HTML, 最终URL, 来源类型)。

    来源类型: "html" 或 "pdf"
    """
    if requests is None:
        print("❌ 缺少 requests 库。请安装：pip install requests")
        sys.exit(1)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    print(f"🌐 正在抓取网页：{url}")
    try:
        resp = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        code = resp.status_code if 'resp' in dir() else 'unknown'
        print(f"❌ 抓取失败：HTTP {code}")
        if code == 403:
            print("   网站可能阻止了自动抓取（需要登录或有反爬机制）。")
            print("   建议：手动保存网页内容为 Markdown 文件后，放入 raw/sources/ 目录")
            print("   然后运行：python tools/llm_wiki.py ingest raw/sources/your_file.md")
        elif code == 404:
            print("   页面不存在，请检查 URL 是否正确。")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ 抓取失败：{e}")
        sys.exit(1)

    resp.encoding = resp.apparent_encoding
    content_type = resp.headers.get('Content-Type', '')

    # 检查 Content-Type 判断是否为 PDF
    if 'application/pdf' in content_type or 'application/octet-stream' in content_type:
        print(f"⚠️  检测到 PDF 内容类型（{content_type}）")
        print(f"   建议使用 HTML 页面 URL（如 arXiv 的 /abs/ 而非 /pdf/）")

    print(f"✅ 抓取成功，最终 URL：{resp.url}，大小：{len(resp.content)} 字符")
    return resp.text, resp.url, 'html'



def parse_llm_response(response: str) -> dict:
    """解析 LLM 的 JSON 风格响应，提取建议的操作。

    返回 dict 包含：
    - summary: 源文档摘要
    - update_pages: 需要更新的页面列表
    - create_pages: 需要创建的页面列表
    - contradictions: 矛盾列表
    - facts: 提取的关键事实
    - source_page_content: 源页面内容
    """
    import re
    result = {
        "summary": "",
        "update_pages": [],
        "create_pages": [],
        "contradictions": [],
        "facts": [],
        "source_page_content": ""
    }

    # 提取摘要
    match = re.search(r"### 源文档摘要\s*([\s\S]*?)(?=### |\Z)", response)
    if match:
        result["summary"] = match.group(1).strip()

    # 提取需要更新的页面（支持两种格式）
    # 格式1: - **wiki/concepts/X.md**：内容
    # 格式2: 1. 创建/更新 `wiki/concepts/X.md`：内容
    # 格式3: [HSTU](../models/HSTU.md) — 需要更新的内容（Markdown 链接格式）
    update_match = re.search(r"### 需要更新的页面\s*([\s\S]*?)(?=### |\Z)", response, re.DOTALL)
    if update_match:
        content = update_match.group(1).strip()
        for line in content.split('\n'):
            line = line.strip()
            # 格式1: - **\`wiki/concepts/X.md\`**：内容 (with backticks) or - **wiki/concepts/X.md**：内容
            if line.startswith(('- ', '* ')):
                # 尝试匹配带反引号的格式 **`path`**
                page_match = re.search(r'\*\*`([^`]+)`\*\*', line)
                if not page_match:
                    # 尝试匹配不带反引号的格式 **path**
                    page_match = re.search(r'\*\*(wiki/[^*]+)\*\*', line)
                if page_match:
                    path = page_match.group(1)
                    details = line.replace(page_match.group(0), '').replace('-', '').replace('*', '').replace('`', '').replace(':', '：').strip()
                    result["update_pages"].append({"path": path, "details": details})
            # 格式2: 1. 创建/更新 `wiki/concepts/X.md`：内容
            elif re.match(r'\d+\.\s', line):
                page_match = re.search(r'wiki/[^`\']+', line)
                if page_match:
                    path = page_match.group(0).strip('`\'" ')
                    desc_match = re.search(r'[:：]\s*(.+)', line)
                    details = desc_match.group(1).strip() if desc_match else ""
                    result["update_pages"].append({"path": path, "details": details})
            # 格式3: [HSTU](../models/HSTU.md) — 描述
            elif line.startswith(('- ', '* ')) or not line.startswith('#'):
                link_match = re.search(r'\[(.*?)\]\(\.\.\/([^)]+)\)', line)
                if link_match:
                    path = f'wiki/{link_match.group(2)}'
                    details = line.replace(link_match.group(0), '').strip('-* ').strip()
                    # 避免重复添加
                    if not any(p["path"] == path for p in result["update_pages"]):
                        result["update_pages"].append({"path": path, "details": details})

    # 提取需要创建的页面（支持两种格式）
    create_match = re.search(r"### 需要创建的新页面\s*([\s\S]*?)(?=### |\Z)", response, re.DOTALL)
    if create_match:
        content = create_match.group(1).strip()
        for line in content.split('\n'):
            line = line.strip()
            # 格式1: - **wiki/TYPE/new_page.md**：标题和描述
            if line.startswith(('- ', '* ')):
                page_match = re.search(r'\*\*(wiki/[^*]+)\*\*', line)
                if page_match:
                    path = page_match.group(1)
                    details = line.replace(page_match.group(0), '').replace('-', '').replace('*', '').replace(':', '：').strip()
                    result["create_pages"].append({"path": path, "details": details})
            # 格式2: 1. 创建 `wiki/TYPE/new_page.md`：描述
            elif re.match(r'\d+\.\s', line):
                page_match = re.search(r'wiki/[^`\']+', line)
                if page_match:
                    path = page_match.group(0).strip('`\'" ')
                    desc_match = re.search(r'[:：]\s*(.+)', line)
                    details = desc_match.group(1).strip() if desc_match else ""
                    result["create_pages"].append({"path": path, "details": details})

    # Fallback：从 "关联" 或其他 Markdown 链接中提取未创建的页面
    # 当 LLM 未遵循结构化格式时，尝试从关联章节中检测需要创建的页面
    if not result["create_pages"]:
        # 匹配 ## 关联 或 ### 关联
        link_sections = re.finditer(r'#{2,3}\s*[关联相关推荐][^\n]*\s*([\s\S]*?)(?=#{1,3}\s|\Z)', response, re.IGNORECASE)
        for section in link_sections:
            section_text = section.group(1)
            # 匹配 [名称](../path/to/page.md) 格式
            links = re.findall(r'\[([^\]]+)\]\(\.\.\/([^)]+)\)', section_text)
            for _, path in links:
                # 仅当路径在 wiki/ 目录下且不是 sources 时考虑创建
                full_path = f'wiki/{path}'
                if not any(p["path"] == full_path for p in result["update_pages"]) and not any(p["path"] == full_path for p in result["create_pages"]):
                    # 提取文件名
                    filename = path.split('/')[-1].replace('.md', '')
                    # 根据路径确定页面类型
                    if 'models' in path.lower():
                        page_type = 'models'
                    elif 'entities' in path.lower():
                        page_type = 'entities'
                    elif 'methods' in path.lower():
                        page_type = 'methods'
                    elif 'concepts' in path.lower():
                        page_type = 'concepts'
                    else:
                        page_type = 'models'
                    result["create_pages"].append({"path": f'{page_type}/{filename}.md', "details": f'从关联章节中检测到的页面'})

    # 提取矛盾/冲突
    conflict_match = re.search(r"### 矛盾/冲突\s*([\s\S]*?)(?=### |\Z)", response, re.DOTALL)
    if conflict_match:
        content = conflict_match.group(1).strip()
        result["contradictions"] = [line.strip('-* `\'" ').strip() for line in content.split('\n') if line.strip() and not line.startswith('##')]

    # 提取关键事实
    facts_match = re.search(r"### 提取的关键事实\s*([\s\S]*?)(?=### |\Z)", response, re.DOTALL)
    if facts_match:
        content = facts_match.group(1).strip()
        result["facts"] = [line.strip('-* `\'" ').strip() for line in content.split('\n') if line.strip() and not line.startswith('##')]

    # 提取源页面内容
    source_match = re.search(r"### 建议的源页面内容\s*([\s\S]*)", response, re.DOTALL)
    if source_match:
        result["source_page_content"] = source_match.group(1).strip()

    return result

def generate_source_filename(url: str, title: str, final_url: str) -> str:
    """根据 URL、标题和最终 URL 生成安全的源文件名。

    为 arXiv 论文添加出版月份前缀（如 2507_ 表示 2025年07月），
    格式：YYMM_prefix_TITLE.md
    支持 /abs/ 和 /pdf/ 两种 arXiv URL 格式。
    """
    from urllib.parse import urlparse
    import hashlib
    import re

    parsed = urlparse(final_url)
    domain = parsed.netloc.lower()
    parsed_orig = urlparse(url)

    # 检测是否为 arXiv 论文（支持 /abs/ 和 /pdf/）
    is_arxiv = 'arxiv.org' in domain or 'arxiv.org' in parsed_orig.netloc.lower()

    # 从 arXiv URL 提取 ID 和出版月份
    paper_id = ""
    month_prefix = ""

    if is_arxiv:
        # 尝试多种模式提取 arXiv ID
        arxiv_match = None
        # 模式1: /pdf/2402.17152 或 /pdf/2402.17152.pdf 或 /pdf/2402.17152v1
        for check_url in [parsed.path, parsed_orig.path]:
            arxiv_match = re.search(r'/pdf/(\d{4}\.\d{4,5})(?:v\d+)?\.?pdf?$', check_url)
            if arxiv_match:
                break
        # 模式2: /abs/2402.17152 或 /abs/2402.17152v1
        if not arxiv_match:
            for check_url in [parsed.path, parsed_orig.path]:
                arxiv_match = re.search(r'/abs/(\d{4}\.\d{4,5})(?:v\d+)?$', check_url)
                if arxiv_match:
                    break
        # 模式3: 从 HTML 内容中提取的标题中包含 arXiv ID
        if not arxiv_match:
            arxiv_match = re.search(r'(\d{4}\.\d{4,5})', title or '')

        if arxiv_match:
            paper_id = arxiv_match.group(1)
            # arXiv ID 格式: YYMM.NNNNN (e.g., 2507.15551 = 2025年07月)
            num_part = paper_id.split('.')[0]
            if len(num_part) >= 4:
                year = num_part[:2]
                month = num_part[2:4]
                month_prefix = f"{year}{month}_"

    # 技术论文网站
    paper_sites = {
        "arxiv.org": "arxiv",
        "aclanthology.org": "acl",
        "openreview.net": "openreview",
        "neurips.cc": "neurips",
        "iclr.cc": "iclr",
        "aaai.org": "aaai",
        "ieee.org": "ieee",
        "dl.acm.org": "acm",
        "springer.com": "springer",
        "nature.com": "nature",
        "sciencedirect.com": "sciencedirect",
    }

    # 技术博客/媒体网站
    blog_sites = {
        "medium.com": "medium",
        "juejin.cn": "掘金",
        "zhihu.com": "知乎",
        "csdn.net": "CSDN",
        "mp.weixin.qq.com": "微信",
        "machinelearningmastery.com": "MLMastery",
        "towardsdatascience.com": "TDS",
        "substack.com": "substack",
    }

    # 从标题中提取关键词
    keywords = ""
    if title and len(title) > 3:
        # 截取标题前 60 字符
        keywords = title[:60].strip()
    elif not title:
        # 如果没有标题，从 URL 路径提取
        path = parsed.path.strip("/").split("/")[-1]
        if path:
            keywords = path[:60]
        else:
            keywords = domain.replace("www.", "")

    # 清理文件名
    safe_name = re.sub(r'[\\/:*?"<>|]', "_", keywords)
    safe_name = re.sub(r"[\s_]+", "_", safe_name).strip("_")

    # 截断过长部分
    if len(safe_name) > 80:
        safe_name = safe_name[:80]

    # 根据网站类型添加前缀
    if any(s in domain for s in paper_sites):
        prefix = "paper"
    elif any(s in domain for s in blog_sites):
        prefix = "article"
    else:
        # 从域名提取网站名
        site_name = domain.replace("www.", "").split(".")[0]
        prefix = site_name

    # 添加出版月份前缀（仅 arXiv）和短哈希避免冲突
    if is_arxiv and paper_id:
        # 对于 arXiv 论文，使用 arXiv ID 作为哈希（去除点号）
        url_hash = paper_id.replace('.', '')[:8]
    else:
        url_hash = hashlib.md5(final_url.encode()).hexdigest()[:6]

    return f"{month_prefix}{prefix}_{url_hash}_{safe_name}.md"


def html_to_markdown(html: str, url: str = "") -> tuple[str, str]:
    """将 HTML 转换为格式化的 Markdown 文本。返回 (markdown, title)。"""
    if BeautifulSoup is None:
        print("❌ 缺少 beautifulsoup4 库。请安装：pip install beautifulsoup4")
        sys.exit(1)

    soup = BeautifulSoup(html, "html.parser")

    # 移除不需要的元素
    for tag in soup.find_all(["script", "style", "nav", "footer", "header",
                               "iframe", "noscript", "svg", "form", "button"]):
        tag.decompose()

    # 提取标题（优先使用 og:title 或 meta 标题）
    title = ""
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()
    elif soup.title:
        title = soup.title.get_text(strip=True)

    # 清理标题：去除网站后缀（如 " | arXiv", " - 机器之心"）
    clean_title = title
    for sep in [" | ", " — ", " - ", " – ", " · "]:
        if sep in clean_title:
            # 保留第一部分（通常是文章/论文标题）
            parts = clean_title.split(sep)
            candidate = parts[0].strip()
            # 如果第一部分太短，可能是网站名，尝试第二部分
            if len(candidate) > 5:
                clean_title = candidate
                break

    # 提取主内容区域
    main = soup.find("main") or soup.find("article") or soup.find("div", class_=re.compile(r"content|article|post|main", re.I))
    if main:
        soup = main

    # 处理链接 — 转换为脚注格式
    links = []
    for i, a in enumerate(soup.find_all("a", href=True), 1):
        href = a["href"]
        text = a.get_text(strip=True)
        if text and href and not href.startswith("#"):
            links.append(f"[{i}] {text}: {href}")
            a.string = f"{text}[^{i}]"

    # 处理图片
    for img in soup.find_all("img", src=True):
        alt = img.get("alt", "")
        src = img["src"]
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            parsed = urlparse(url)
            src = f"{parsed.scheme}://{parsed.netloc}{src}"
        img.replace_with(f"![{alt}]({src})")

    # 获取文本
    text = soup.get_text("\n", strip=True)

    # 后处理：清理多余空行
    lines = []
    prev_blank = False
    for line in text.split("\n"):
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        prev_blank = is_blank
        lines.append(line)
    text = "\n".join(lines)

    # 构建最终 Markdown
    md_parts = []
    if clean_title:
        md_parts.append(f"# {clean_title}\n")
    if url:
        md_parts.append(f"> 来源：{url}\n")
    md_parts.append(text)

    if links:
        md_parts.append("\n---\n## 页面链接\n" + "\n".join(links))

    return "\n".join(md_parts), clean_title



# ─── Wiki Helpers ────────────────────────────────────────────────────────────

def read_file_safe(path: Path) -> str:
    """读取文件，如果不存在则返回空字符串。"""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def write_file_safe(path: Path, content: str):
    """将内容写入文件，如需要则创建目录。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_index() -> str:
    """读取知识库索引。"""
    return read_file_safe(INDEX_FILE)


def read_all_wiki_pages() -> dict[str, str]:
    """读取 wiki 目录中的所有 Markdown 文件，排除检查点目录。"""
    pages = {}
    for md_file in WIKI_DIR.rglob("*.md"):
        # 排除 .ipynb_checkpoints 目录
        if '.ipynb_checkpoints' in str(md_file):
            continue
        if md_file.name in ("README.md", "index.md", "log.md"):
            continue
        rel_path = md_file.relative_to(WIKI_DIR)
        pages[str(rel_path)] = md_file.read_text(encoding="utf-8")
    return pages


def append_log(operation: str, description: str, details: list[str] = None):
    """向 log.md 追加日志条目。"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n## [{timestamp}] {operation} | {description}\n"
    if details:
        for d in details:
            entry += f"- {d}\n"
    entry += "\n---\n"

    log_content = read_file_safe(LOG_FILE)
    # 在最终闭合行之前插入
    if "*Log continues below this line" in log_content:
        log_content = log_content.replace(
            "*Log continues below this line",
            entry + "\n*Log continues below this line"
        )
    else:
        log_content += "\n" + entry

    write_file_safe(LOG_FILE, log_content)


def build_index() -> str:
    """根据 wiki 目录重建 index.md。"""
    pages = read_all_wiki_pages()
    categories = {
        "concepts": [],
        "methods": [],
        "models": [],
        "entities": [],
        "synthesis": [],
        "sources": []
    }

    for path, content in pages.items():
        parts = path.split("/")
        if len(parts) >= 1:
            cat = parts[0]
            if cat in categories:
                # 提取标题
                title_match = re.search(r'title:\s*["\']?([^"\'\n]+)', content[:500])
                title = title_match.group(1).strip() if title_match else path
                # 提取 tags
                tags_match = re.search(r'tags:\s*\[(.*?)\]', content[:500])
                tags = tags_match.group(1).strip() if tags_match else ""

                categories[cat].append({
                    "path": path,
                    "title": title,
                    "tags": tags,
                    "content": content[:300]
                })

    # 构建 index 内容
    index_parts = []
    index_parts.append(f"# LLM4Rec Wiki — 知识库目录\n\n")
    index_parts.append(f"> 知识库内容目录。由 LLM 自动维护。\n")
    index_parts.append(f"> 最后更新：{datetime.now().strftime('%Y-%m-%d')}\n\n")

    for cat, items in categories.items():
        if items:
            index_parts.append(f"## {cat.capitalize()}\n")
            index_parts.append(f"| 页名 | 摘要 | 标签 |\n")
            index_parts.append(f"|------|------|------|\n")
            for item in items[:50]:  # 避免太长
                title_link = f"[{item['title']}]({item['path']})"
                summary = item['content'].replace('\n', ' ')[:60].strip()
                index_parts.append(f"| {title_link} | {summary}... | {item['tags']} |\n")
            index_parts.append(f"\n")
            index_parts.append(f"- **{len(items)} 个页面**\n\n")

    index_parts.append(f"---\n")
    index_parts.append(f"**统计**：\n")
    total = sum(len(v) for v in categories.values())
    index_parts.append(f"- 总页面数：{total}\n")

    return "\n".join(index_parts)


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_ingest(source_file: str):
    """将新的源文档摄入到知识库中。"""
    source_path = Path(source_file)

    if not source_path.exists():
        print(f"错误：未找到源文件：{source_file}")
        sys.exit(1)

    print(f"📖 正在读取源文件：{source_path.name}")
    source_content = source_path.read_text(encoding="utf-8", errors="replace")

    # 如果太长则截断（LLM 上下文限制）
    max_chars = 10000000
    if len(source_content) > max_chars:
        print(f"⚠️  源文件较大（{len(source_content)} 字符）。截断至 {max_chars} 字符。")
        source_content = source_content[:max_chars]

    # 读取模式和当前知识库状态
    schema = read_file_safe(SCHEMA_FILE)
    index = read_index()
    wiki_pages = read_all_wiki_pages()

    # 构建摄入提示 — 控制上下文大小
    # 只包含索引和少量页面摘要
    wiki_context = "\n\n".join(
        f"=== {path} ===\n{content[:500]}..."
        for path, content in list(wiki_pages.items())[:30]
    )

    system_prompt = f"""你是 LLM 在推荐系统中应用的知识库专家级维护者。
遵循模式（AGENTS.md）中定义的约定。

你的任务是摄入新的源文档并相应更新知识库。"""

    prompt = f"""## 模式与约定
{schema}

## 当前知识库索引
{index}

## 选定的现有知识库页面（用于上下文）
{wiki_context}

## 新源文档
{source_content}

## 指令

请处理此源文档并：

1. **总结**关键贡献、方法和发现
2. **识别**哪些现有知识库页面需要更新（实体、概念、方法、模型）
3. **识别**是否需要创建新的知识库页面
4. **注意**与现有知识库内容的任何矛盾或冲突
5. **提取**关键事实、声明和数据点

请按以下结构化格式响应：

### 源文档摘要
[2-3 段摘要]

### 需要更新的页面
- **wiki/concepts/X.md**：[更新内容及原因]
- **wiki/methods/Y.md**：[更新内容及原因]
- **wiki/models/Z.md**：[更新内容及原因]

### 需要创建的新页面
- **wiki/TYPE/new_page.md**：[标题和简要描述]

### 矛盾/冲突
- [与现有知识库内容的任何冲突，或"未发现冲突"]

### 提取的关键事实
- [事实 1]
- [事实 2]
- [等等]

### 建议的源页面内容
[编写 wiki/sources/{source_path.stem}.md 的完整 Markdown 内容，包括前置元数据]
"""

    print("🤖 正在使用 LLM 处理（可能需要一些时间）...")
    response = call_llm(prompt, system_prompt, max_tokens=200000)

    if not response:
        print("❌ LLM 返回空响应。")
        sys.exit(1)

    # 显示响应
    print("\n" + "=" * 60)
    print(response)
    print("=" * 60)

    # 解析 LLM 响应
    parsed = parse_llm_response(response)
    print("\n🔍 解析的变更：")
    if parsed["create_pages"]:
        print(f"  ✅ 待创建页面 ({len(parsed['create_pages'])}):")
        for p in parsed["create_pages"]:
            print(f"    - {p['path']}")
    if parsed["update_pages"]:
        print(f"  ✅ 待更新页面 ({len(parsed['update_pages'])}):")
        for p in parsed["update_pages"]:
            print(f"    - {p['path']}")
    if parsed["contradictions"]:
        print(f"  ⚠️  矛盾/冲突 ({len(parsed['contradictions'])}):")
        for c in parsed["contradictions"]:
            print(f"    - {c}")

    # 在写入文件之前请求用户确认
    print("\n💡 请审查上面提议的更改。")
    auto_confirm = os.environ.get("WIKI_AUTO_CONFIRM", "false").lower() == "true"

    if auto_confirm or input("是否将这些更改应用到知识库？(y/n): ").lower() == "y":
        # 创建源摘要页面
        source_page_path = WIKI_DIR / "sources" / f"{source_path.stem}.md"

        today = datetime.now().strftime("%Y-%m-%d")
        frontmatter = f"""---
title: "{source_path.stem.replace('_', ' ').title()}"
category: "sources"
tags: ["source", "{today}"]
created: "{today}"
updated: "{today}"
sources: ["../../raw/sources/{source_path.name}"]
related: []
confidence: "high"
status: "stable"
---

"""
        write_file_safe(source_page_path, frontmatter + response)
        print(f"\n✅ 已创建源摘要页面：{source_page_path.relative_to(WIKI_ROOT)}")

        # 根据解析结果创建/更新页面
        pages_created = 0
        pages_updated = 0
        new_page_paths = []  # 记录新创建和更新的页面路径

        # 创建新页面
        for page_info in parsed["create_pages"]:
            # LLM 返回的路径如 "wiki/models/QARM.md" 或 "models/QARM.md"
            # 需要提取出相对于 WIKI_DIR 的路径
            relative_path = page_info["path"].strip()
            # 移除可能存在的 "wiki/" 前缀
            while relative_path.startswith("wiki/"):
                relative_path = relative_path[5:]

            page_path = WIKI_DIR / relative_path
            
            # 检查页面是否已存在
            if page_path.exists():
                existing_content = page_path.read_text(encoding="utf-8")
                # 判断是否为占位符/草稿（小文件且内容不完整）
                is_placeholder = (
                    len(existing_content) < 2000 or
                    "本文档包含关于" in existing_content or
                    "从关联章节中检测到的页面" in existing_content or
                    "本页面由 LLM 自动生成" in existing_content
                )
                
                if is_placeholder:
                    print(f"  🔄 更新占位符页面：{page_path.relative_to(WIKI_ROOT)}")
                    update_details = page_info["details"]
                    
                    # 读取现有页面并追加
                    update_marker = f"\n\n## 更新于 {today}\n\n**来源**: {source_path.name}\n{update_details}\n"

                    if update_marker not in existing_content:
                        new_content = existing_content + update_marker
                        page_path.write_text(new_content, encoding="utf-8")
                        pages_updated += 1
                        new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                    else:
                        print(f"  ↻ 页面已更新过：{page_path.relative_to(WIKI_ROOT)}")
                    continue
                else:
                    print(f"  ↻ 页面已存在且完整，跳过：{page_path.relative_to(WIKI_ROOT)}")
                    continue

            # 使用相对路径获取类别
            try:
                rel_path_parts = page_path.relative_to(WIKI_DIR).parts
                page_category = rel_path_parts[0] if len(rel_path_parts) > 0 else "unknown"
            except ValueError:
                # 如果无法计算相对路径，使用第一个目录名
                page_category = page_path.name if page_path.is_file() else page_path.name
                # 找到第一个非文件的父目录
                for parent in page_path.parents:
                    if parent == WIKI_DIR:
                        break
                    page_category = parent.name
            page_name = page_path.stem.replace('_', ' ').title()

            # 提取标题和描述
            title = page_name
            description = page_info["details"].strip()

            # 定义中文标点符号用于分割
            separators = ["：", ": ", ":"]

            for sep in separators:
                if sep in description:
                    parts = description.split(sep, 1)
                    if len(parts) == 2:
                        # 如果第一部分是有效的中文标题，使用它
                        candidate = parts[0].strip()
                        if len(candidate) > 2 and len(candidate) < 50:
                            # 检查是否包含中文
                            if any('\u4e00' <= c <= '\u9fff' for c in candidate):
                                title = candidate
                                description = parts[1].strip()
                                break

            # 如果标题还是不变且没有分隔符，使用 description 的开头作为标题
            if title == page_name:
                # 从描述中提取前几个词作为标题
                words = description.split()[:3]
                if words:
                    title = words[0].strip()
                    if len(title) < 5:
                        title = ' '.join(words[:2]).strip()

            # 清理标题：只保留中文和字母数字
            title = re.sub(r'[^\w\u4e00-\u9fff\s\-]', '', title)
            title = title.strip()
            if not title or len(title) < 3:
                title = page_name

            # 🆕 调用 LLM 生成完整的页面内容（而非占位符）
            print(f"  🤖 正在调用 LLM 生成完整的 {page_category} 页面：{title} ...")
            simple_title = page_name.replace('_', ' ')

            page_gen_prompt = f"""你是 LLM4Rec 知识库专家。请为以下新概念/模型/方法/实体撰写完整的中文百科页面。

## 页面信息
- **标题**：{title}
- **类别**：{page_category}
- **描述**：{description}
- **来源文档**：{source_path.name}

## 当前源文档内容

{source_content[:8000]}

## 当前知识库索引（参考）

{index[:3000]}

请输出完整的 Markdown 页面（含 frontmatter）。要求：
1. **全部内容为中文**
2. frontmatter 中 status 为 "draft"，confidence 为 "medium"
3. 包含完整结构：摘要、要点列表、详细说明（分 3-5 个小节）、关联页面、开放问题、参考文献
4. 结合你的领域知识撰写内容，不局限于源文档
5. 保持与现有 wiki 页面风格一致（参见类似页面）
6. 相关页面链接使用相对路径（如 ../models/XXX.md）"""

            generated_content = call_llm(page_gen_prompt, "你是推荐系统和大语言模型领域的专家，擅长撰写详实、准确的知识库百科页面。", max_tokens=16384)

            if generated_content and len(generated_content) > 500:
                # 确保 frontmatter 正确
                if not generated_content.strip().startswith('---'):
                    page_content = f"""---
title: "{title}"
category: "{page_category}"
tags: ["new", "{today}"]
created: "{today}"
updated: "{today}"
sources: ["../sources/{source_path.stem}.md"]
related: []
confidence: "medium"
status: "draft"
---

""" + generated_content
                else:
                    page_content = generated_content

                write_file_safe(page_path, page_content)
                pages_created += 1
                new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                print(f"  ✅ 已创建完整页面：{page_path.relative_to(WIKI_ROOT)}（{len(page_content)} 字符）")
            else:
                # LLM 生成失败，降级为占位符
                print(f"  ⚠️  LLM 生成内容不足，使用占位符模板")
                simple_title = page_name.replace('_', ' ')
                desc_text = description if description and description != "从关联章节中检测到的页面" else f"本文档包含关于 {simple_title} 的关键信息。"

                page_content = f"""---
title: "{title}"
category: "{page_category}"
tags: ["new", "{today}"]
created: "{today}"
updated: "{today}"
sources: ["../sources/{source_path.stem}.md"]
related: []
confidence: "medium"
status: "draft"
---

# {title}

{desc_text}

**来源**: 源文档：{source_path.name}

---

## 相关主题

- [源文档](../sources/{source_path.stem}.md)

## 扩展阅读

- [知识库首页](../README.md)

---

*本页面由 LLM 自动生成，内容可能需要人工审查和补充。*
"""
                write_file_safe(page_path, page_content)
                pages_created += 1
                new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                print(f"  ✅ 已创建页面（占位符）：{page_path.relative_to(WIKI_ROOT)}")

        # 更新页面
        for page_info in parsed["update_pages"]:
            # LLM 返回的路径如 "wiki/models/QARM.md" 或 "models/QARM.md"
            # 需要提取出相对于 WIKI_DIR 的路径
            relative_path = page_info["path"].strip()
            # 移除可能存在的 "wiki/" 前缀
            while relative_path.startswith("wiki/"):
                relative_path = relative_path[5:]

            page_path = WIKI_DIR / relative_path
            update_details = page_info["details"]

            if page_path.exists():
                # 读取现有页面
                existing_content = page_path.read_text(encoding="utf-8")

                # 简单更新：在末尾添加新内容
                update_marker = f"\n\n## 更新于 {today}\n\n**来源**: {source_path.name}\n{update_details}\n"

                # 检查是否已存在相同更新
                if update_marker not in existing_content:
                    new_content = existing_content + update_marker
                    page_path.write_text(new_content, encoding="utf-8")
                    pages_updated += 1
                    new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                    print(f"  ✅ 已更新页面：{page_path.relative_to(WIKI_ROOT)}")
                else:
                    print(f"  ↻ 页面已更新过：{page_path.relative_to(WIKI_ROOT)}")
            else:
                # 页面不存在，调用 LLM 生成完整内容
                print(f"  🆕 创建缺失页面：{page_path.relative_to(WIKI_ROOT)}")
                page_category = relative_path.split("/")[0]
                page_name = page_path.stem.replace('_', ' ').title()

                # 提取标题
                title = page_name
                if ": " in update_details:
                    parts = update_details.split(": ", 1)
                    candidate = parts[0].strip()
                    if len(candidate) > 2 and len(candidate) < 50 and any('\u4e00' <= c <= '\u9fff' for c in candidate):
                        title = candidate

                # 🆕 调用 LLM 生成完整页面
                print(f"  🤖 正在调用 LLM 生成页面内容：{title} ...")

                page_gen_prompt = f"""你是 LLM4Rec 知识库专家。请为以下概念/实体撰写完整的中文百科页面。

## 页面信息
- **标题**：{title}
- **类别**：{page_category}
- **描述**：{update_details}
- **来源文档**：{source_path.name}

## 源文档内容

{source_content[:8000]}

请输出完整的 Markdown 页面（含 frontmatter）。要求：
1. **全部内容为中文**
2. frontmatter 中 status 为 "draft"，confidence 为 "medium"
3. 包含完整结构：摘要、要点列表、详细说明（分 3-5 个小节）、关联页面、开放问题、参考文献
4. 结合你的领域知识撰写内容
5. 保持与现有 wiki 页面风格一致
6. 相关页面链接使用相对路径"""

                generated = call_llm(page_gen_prompt, "你是推荐系统专家，擅长撰写知识库页面。", max_tokens=16384)

                if generated and len(generated) > 500:
                    if not generated.strip().startswith('---'):
                        page_content = f"""---
title: "{title}"
category: "{page_category}"
tags: ["new", "{today}"]
created: "{today}"
updated: "{today}"
sources: ["../sources/{source_path.stem}.md"]
related: []
confidence: "medium"
status: "draft"
---

""" + generated
                    else:
                        page_content = generated
                    write_file_safe(page_path, page_content)
                    pages_created += 1
                    new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                    print(f"  ✅ 已创建完整页面：{page_path.relative_to(WIKI_ROOT)}（{len(page_content)} 字符）")
                else:
                    # 降级为占位符
                    print(f"  ⚠️  LLM 生成内容不足，使用占位符")
                    page_content = f"""---
title: "{title}"
category: "{page_category}"
tags: ["new", "{today}"]
created: "{today}"
updated: "{today}"
sources: ["../sources/{source_path.stem}.md"]
related: []
confidence: "medium"
status: "draft"
---

# {title}

{update_details}

**来源**: 源文档：{source_path.name}

---

## 相关主题

- [源文档](../sources/{source_path.stem}.md)

## 扩展阅读

- [知识库首页](../README.md)

---

*本页面由 LLM 自动生成，内容可能需要人工审查和补充。*
"""
                    write_file_safe(page_path, page_content)
                    pages_created += 1
                    new_page_paths.append(str(page_path.relative_to(WIKI_DIR)))
                    print(f"  ✅ 已创建页面（占位符）：{page_path.relative_to(WIKI_ROOT)}")

        # 更新索引
        print(f"\n📝 更新知识库索引...")
        # Re-read all pages and rebuild index
        index_content = build_index()
        write_file_safe(INDEX_FILE, index_content)
        print(f"  ✅ 知识库索引已更新")

        # 记录操作日志
        details = [
            f"源文件：{source_path.name}",
            f"已创建页面：{pages_created}",
            f"已更新页面：{pages_updated}",
        ]
        append_log("ingest", f"已处理源文件：{source_path.name}", details)

        print("\n" + "=" * 60)
        print(f"✅ 摄入完成！")
        print(f"  新建页面：{pages_created}")
        print(f"  更新页面：{pages_updated}")
        print("=" * 60)
    else:
        print("⏭️  未应用更改。")


def _enrich_draft_pages(created_paths: list[str], source_content: str, today: str):
    """对状态为 draft 的新页面，调用 LLM 搜集资料自动补充内容。"""
    if not created_paths:
        return

    print(f"  ℹ️  发现 {len(created_paths)} 个新页面。如需自动补充内容，建议后续单独运行补充命令。")
    # 注意：LLM 补充耗时较长，不再在 ingest 中自动执行
    # 用户可后续通过以下方式手动补充：
    #   1. 手动编辑页面
    #   2. 通过后续 ingest 更多相关源文档逐步更新
    #   3. 等待下一次相关源文档的 ingest 自动触发


def cmd_query(question: str, stream: bool = False):
    """查询知识库并获取综合回答。"""
    print(f"🔍 查询：{question}")

    # 读取知识库上下文
    index = read_index()
    wiki_pages = read_all_wiki_pages()

    # 构建查询提示
    wiki_context = "\n\n".join(
        f"=== {path} ===\n{content[:3000]}"
        for path, content in wiki_pages.items()
    )

    system_prompt = """你是 LLM 在推荐系统中应用的知识库专家级助手。
通过综合知识库中的信息来回答问题。始终引用支持你声明的知识库页面。
如果知识库信息不足，请明确说明并建议缺失的内容。"""

    prompt = f"""## 知识库索引
{index}

## 知识库页面内容
{wiki_context}

## 问题
{question}

## 指令

通过引用上面的知识库页面来综合一个全面的回答。

1. 以直接回答问题开始
2. 为每个声明引用具体的知识库页面（例如："[来源：wiki/concepts/X.md]"）
3. 包含相关细节、比较和上下文
4. 指出任何不确定性或知识库中的空白
5. 如果有用，建议探索相关的知识库页面

请以结构良好的 Markdown 格式提供你的答案。
"""

    print("🤖 正在从知识库综合回答...\n")

    if stream:
        for chunk in call_llm_stream(prompt, system_prompt):
            print(chunk, end="", flush=True)
        print("\n")
    else:
        response = call_llm(prompt, system_prompt, max_tokens=8192)
        print(response)

    # 如果有实质内容则保存到综合文件夹
    if response and len(response) > 200:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        summary_path = WIKI_DIR / "summary" / f"summary_{timestamp}.md"
        write_file_safe(summary_path, f"# 查询总结\n\n## 问题\n{question}\n\n## 回答\n{response}")
        print(f"\n💾 已保存查询结果：{summary_path.relative_to(WIKI_ROOT)}")


def cmd_lint(auto_fix: bool = False):
    """运行知识库健康检查。"""
    print("🔍 正在运行知识库健康检查...")

    # 读取所有页面（已排除 checkpoints）
    pages = read_all_wiki_pages()

    # 读取 index
    index = read_index()

    print("🤖 正在分析知识库健康状况...")

    # 检查问题
    issues = []
    fixes_applied = []

    # 检查 1: 检查点文件（如果 auto_fix 则自动删除）
    checkpoint_files = []
    for path in WIKI_DIR.rglob("*checkpoint*"):
        if path.is_file():
            checkpoint_files.append(str(path.relative_to(WIKI_ROOT)))
            if auto_fix:
                try:
                    path.unlink()
                    fixes_applied.append(f"已删除检查点文件: {path.relative_to(WIKI_ROOT)}")
                except Exception as e:
                    issues.append(f"❌ {path.relative_to(WIKI_ROOT)}: 删除失败 - {e}")
            else:
                issues.append(f"❌ {path.relative_to(WIKI_ROOT)}: 应该删除检查点文件")

    # 检查 2: 空页面（只有 frontmatter 没有正文，或只有占位符文本）
    placeholder_titles = [
        "从关联章节中检测到的页面",
        "源论文摘要页面包含论文元数据核心贡献方法概述关键发现和与现有研究的关联",
        "源论文摘要页面本次任务重点",
        "创建此源文档的摘要页面见下文完整内容",
    ]
    for path, content in pages.items():
        # 排除检查点
        if '.ipynb_checkpoints' in path:
            continue
        # 检查是否只有 frontmatter
        body = content.split('---', 2)[-1].strip() if '---' in content else content.strip()
        if not body:
            issues.append(f"⚠️  {path}: 空页面（只有 frontmatter）")
            continue
        # 检查占位符标题
        for placeholder in placeholder_titles:
            if placeholder in content[:500]:
                issues.append(f"⚠️  {path}: 占位符页面（标题包含'{placeholder[:20]}...'）")
                break

    # 检查 3: frontmatter 缺失
    for path, content in pages.items():
        if '.ipynb_checkpoints' in path:
            continue
        if not content.strip().startswith('---'):
            issues.append(f"❌ {path}: 缺少 frontmatter")

    # 检查 4: 缺少 related 链接
    orphan_pages = []
    for path, content in pages.items():
        if '.ipynb_checkpoints' in path:
            continue
        related_match = re.search(r'related:\s*\[(.*?)\]', content[:500])
        if related_match:
            related_content = related_match.group(1).strip()
            if not related_content or related_content == '[]':
                orphan_pages.append(path)
    if orphan_pages:
        issues.append(f"ℹ️  {len(orphan_pages)} 个页面缺少 related 链接（可能是孤立页面）: {', '.join(orphan_pages[:5])}{'...' if len(orphan_pages) > 5 else ''}")

    # 检查 5: 索引一致性
    index_pages = set()
    for line in index.split('\n'):
        if '](' in line:
            match = re.search(r'\]\(([^)]+)\)', line)
            if match:
                index_pages.add(match.group(1))

    missing_from_index = set(pages.keys()) - index_pages
    if missing_from_index:
        issues.append(f"⚠️  {len(missing_from_index)} 个页面未在 index.md 中: {', '.join(list(missing_from_index)[:5])}{'...' if len(missing_from_index) > 5 else ''}")

    extra_in_index = index_pages - set(pages.keys())
    if extra_in_index:
        issues.append(f"⚠️  index.md 包含 {len(extra_in_index)} 个不存在的页面: {', '.join(list(extra_in_index)[:5])}{'...' if len(extra_in_index) > 5 else ''}")

    # 检查 6: 损坏的相对链接
    broken_links = []
    for path, content in pages.items():
        if '.ipynb_checkpoints' in path:
            continue
        links = re.findall(r'\]\(\.\./([^)]+)\)', content)
        for link in links:
            # 跳过目录链接（以 / 结尾）
            if link.endswith('/'):
                continue
            # 解析相对路径
            page_dir = Path(path).parent
            target = page_dir / link
            target_norm = Path(os.path.normpath(str(target)))
            # 检查目标是否存在
            target_path = WIKI_DIR / target_norm
            if not target_path.exists():
                broken_links.append(f"{path} → {link}")

    if broken_links:
        # 去重
        unique_broken = sorted(set(broken_links))
        issues.append(f"⚠️  发现 {len(unique_broken)} 个可能损坏的链接: {', '.join(unique_broken[:5])}{'...' if len(unique_broken) > 5 else ''}")

    # 打印报告
    print("\n" + "=" * 60)
    print("# 📊 LLM4Rec 知识库健康检查报告")
    print("=" * 60)

    if fixes_applied:
        print(f"\n✅ 自动修复了 {len(fixes_applied)} 个问题:")
        for fix in fixes_applied:
            print(f"  - {fix}")

    if issues:
        print(f"\n检测到 {len(issues)} 个问题:\n")
        for issue in issues[:30]:  # 最多显示 30 个
            print(issue)
        if len(issues) > 30:
            print(f"... 还有 {len(issues) - 30} 个问题未显示")
    else:
        print("\n✅ 知识库健康状况良好！")

    print("\n" + "=" * 60)

    if auto_fix and fixes_applied:
        print(f"\n💡 自动修复完成。建议重新运行 lint 验证: python tools/llm_wiki.py lint")


def cmd_summarize():
    """生成知识库摘要。"""
    print("📊 正在生成知识库摘要...")
    
    pages = read_all_wiki_pages()
    
    # 分类统计
    categories = {}
    for path in pages.keys():
        if path.startswith('wiki/'):
            path = path[5:]  # 移除 'wiki/'
        parts = path.split('/')
        if parts:
            cat = parts[0]
            categories[cat] = categories.get(cat, 0) + 1
    
    # 统计
    total = sum(categories.values())
    
    # 生成摘要
    summary = f"""
知识库统计：
  总页面数：{total}
  {json.dumps(categories, ensure_ascii=False, indent=2)[1:-1]}

该知识库已系统覆盖 LLM 在推荐系统中的核心范式转移，重点聚焦于**生成式检索/推荐**、**语义 ID 与表示对齐**、以及 **LLM 角色解耦（Ranker/Generator/Reasoner）**。在方法与模型层面，
提示微调（P5、InstructRec、TALLRec）、RAG 增强、多目标/定量对齐（QARM 系列）及层次化规划（HiGR）均有详实记录；结合工业界实践（腾讯、快手、YouTube）与评估基准，初步构建了从传统
判别式 ID 匹配向生成式语义理解演进的分类体系。然而，当前内容在**工程落地与系统优化**方面仍显薄弱，缺乏对推理加速（量化/蒸馏/KV Cache）、在线持续学习、冷启动策略、以及公平性/隐私安
全等关键挑战的深入探讨，且部分页面仍为占位符或仅含元数据。

未来最有价值的摄入方向应优先聚焦：1）**顶会最新综述与标准化基准**（如 SIGIR/KDD/RecSys 2024-2025 的 LLM4Rec Survey 与 Open Benchmark），以统一评估协议与指标；2）**轻量化与高效部
署技术**（MoE 架构、模型压缩、流式推理优化），弥补工业级延迟与算力瓶颈；3）**实时推荐与在线微调机制**（Online Continual Learning/RLHF for RecSys），增强动态用户行为适配能力；4）
**开源框架与工业技术博客**（如 RecBole-LLM、大厂架构分享），补充从算法原型到生产环境的完整链路与两阶段检索（GSU/ESU）的工程细节。
"""
    
    print(summary)


def validate_api_key():
    """验证 API 密钥。"""
    try:
        import os
        api_key = os.environ.get("DASHSCOPE_API_KEY", "").strip()
        
        if not api_key:
            print("❌ 未找到 DASHSCOPE_API_KEY 环境变量")
            return False
        
        if api_key.startswith("sk-sp-"):
            endpoint = "https://coding.dashscope.aliyuncs.com/v1"
            print(f"🔑 检测到 Coding Plan 密钥，使用模型：qwen3.6-plus")
            model = os.environ.get("BAILIAN_MODEL", "qwen3.6-plus")
        else:
            endpoint = "https://dashscope.aliyuncs.com/compatible-mode/v1"
            print(f"🔑 检测到标准 API 密钥，使用模型：qwen-max")
            model = os.environ.get("BAILIAN_MODEL", "qwen-max")
        
        # 测试调用
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url=endpoint,
        )
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "hi"}],
            max_tokens=10
        )
        
        if response.choices and response.choices[0].message.content:
            print(f"✅ API 密钥有效！（模型：{model}）")
            if api_key.startswith("sk-sp-"):
                print("   密钥类型：Coding Plan")
            else:
                print("   密钥类型：标准 API")
            print(f"   响应：{response.choices[0].message.content}")
            return True
        else:
            print("❌ API 密钥无效")
            return False
    except Exception as e:
        print(f"❌ API 密钥验证失败：{e}")
        return False


def cmd_validate():
    """验证 API 密钥和连接状态。"""
    validate_api_key()


def cmd_fetch(url: str, auto_ingest: bool = True):
    """从 URL 抓取网页内容，保存为源文件并分析更新知识库。"""
    print(f"🌐 正在从 URL 获取内容：{url}")
    print(f"📁 保存目录：{RAW_DIR / 'sources'}")

    # 1. 检测是否为 PDF URL
    is_pdf = is_pdf_url(url)
    final_url = url
    markdown = ""
    title = ""
    paper_text = ""  # 用于 LLM 提取的纯文本

    if is_pdf:
        print("📄 检测到 PDF URL，尝试转换为 HTML 页面...")
        html_url, source_type = convert_pdf_to_html_url(url)

        if source_type == 'html' and html_url != url:
            # 成功转换为 HTML URL
            print(f"✅ 已转换为 HTML 页面：{html_url}")
            html, final_url, _ = fetch_webpage(html_url)
            print("📝 正在将 HTML 转换为 Markdown...")
            markdown, title = html_to_markdown(html, final_url)
        else:
            # 无法转换，直接下载并解析 PDF
            print(f"⚠️  无法转换为 HTML，将直接下载并解析 PDF 文件...")
            paper_text, title = download_and_parse_pdf(url)
            final_url = url
            if not paper_text:
                print("❌ PDF 解析失败，无法继续。")
                return
    else:
        # 非 PDF URL，正常抓取
        html, final_url, _ = fetch_webpage(url)
        print("📝 正在将 HTML 转换为 Markdown...")
        markdown, title = html_to_markdown(html, final_url)

    if title:
        print(f"📄 检测到标题：{title}")

    # 2. 对 arXiv 论文，调用 LLM 生成完整的中文论文摘要（类似 p5_paper_summary.md 格式）
    if 'arxiv.org' in final_url.lower() or paper_text:
        print("🤖 正在调用 LLM 生成完整的中文论文摘要...")
        # 如果有 paper_text（PDF 解析的全文），使用全文；否则使用 HTML 页面内容
        paper_content = paper_text if paper_text else markdown
        summary_prompt = f"""你是一位专业的论文摘要助手，专注于推荐系统和大语言模型领域。
请将以下论文内容提取为**结构化的中文 Markdown 格式**，参照以下模板：

```
# {{论文标题（中文翻译）}}

**来源类型**：论文摘要
**作者**：{{作者列表}}
**年份**：{{年份}}
**会议/期刊**：{{会议或期刊名称，如无则写"arXiv"}}
**arXiv**：{{arXiv 编号}}

## 摘要

{{一段简洁的中文摘要，2-3 句话概括论文核心}}

## 主要贡献

1. **{{贡献点 1}}**：{{详细描述}}
2. **{{贡献点 2}}**：{{详细描述}}
3. **{{贡献点 3}}**：{{详细描述}}

## 方法

### 架构
{{模型/方法的核心架构描述}}

### 关键技术
{{关键技术细节，如训练策略、损失函数、数据处理等}}

## 实验结果

{{主要实验结果和性能对比，包含具体数字}}

## 局限性

{{论文提到的局限性或潜在改进方向}}

## 与 LLM4Rec 的相关性

{{这篇论文与 LLM 推荐系统领域的相关性和影响}}
```

要求：
1. **全部内容必须为中文**（论文标题保留英文原文，附中文翻译）
2. 保留核心方法、实验数据和结论
3. 保持简洁精炼（总长度控制在 1500-2500 字）
4. 实验结果必须包含具体的数字和对比

论文内容：
{paper_content[:60000]}"""
        summary_response = call_llm(summary_prompt, "你是一位推荐系统和 LLM 领域的专家助手，擅长将英文论文提炼为结构化的中文摘要。", max_tokens=16384)
        if summary_response:
            markdown = summary_response
            print(f"✅ LLM 已生成中文论文摘要（{len(markdown)} 字符）")
        else:
            print("⚠️  LLM 生成失败，将使用原始内容")

    # 3. 检查内容长度，如果太长则让 LLM 提取核心内容（非论文内容才需要）
    if not ('arxiv.org' in final_url.lower() or paper_text) and len(markdown) > 80000:
        print(f"⚠️  内容较长（{len(markdown)} 字符），将使用 LLM 提取核心内容...")
        extract_prompt = f"""你是一个专业的论文/文章内容提取助手。请将以下内容精炼提取为结构化的 Markdown 格式：

要求：
1. 保留核心观点、方法、实验数据和结论
2. 保留主要的章节结构
3. 去除重复、广告、导航等无关内容
4. 保持关键信息的完整性
5. 输出为 **中文** Markdown 格式

内容：
{markdown[:80000]}"""
        extracted = call_llm(extract_prompt, "你是一个内容提取专家。将长文章精炼为结构化中文 Markdown。", max_tokens=16384)
        if extracted:
            markdown = extracted
            print(f"✅ LLM 已精炼内容至 {len(markdown)} 字符")
        else:
            print("⚠️  LLM 提取失败，将使用原始内容")
            markdown = markdown[:80000]

    # 4. 生成智能文件名
    source_filename = generate_source_filename(url, title, final_url)
    source_path = RAW_DIR / "sources" / source_filename

    # 5. 检查是否已存在
    if source_path.exists():
        print(f"⚠️  文件已存在：{source_filename}")
        overwrite = input("是否覆盖？(y/n): ").lower()
        if overwrite != "y":
            print("⏭️  已跳过。")
            return

    # 6. 保存源文件
    today = datetime.now().strftime("%Y-%m-%d")
    fetch_header = f"""---
title: "{title or final_url}"
url: "{final_url}"
original_url: "{url}"
fetched: "{today}"
---

"""
    write_file_safe(source_path, fetch_header + markdown)
    print(f"✅ 已保存源文件：{source_path.relative_to(WIKI_ROOT)}")

    # 7. 如果启用自动摄入，调用 ingest
    if auto_ingest:
        print("\n" + "=" * 60)
        print("🤖 正在分析内容并更新知识库...")
        print("=" * 60 + "\n")
        cmd_ingest(str(source_path))
    else:
        print(f"\n💡 源文件已保存。稍后可运行以下命令进行分析：")
        print(f"   python tools/llm_wiki.py ingest {source_path.relative_to(WIKI_ROOT)}")


# ─── CLI Entry Point ─────────────────────────────────────────────────────────

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="LLM4Rec Wiki — 维护 LLM+RecSys 知识库",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  %(prog)s ingest raw/sources/paper.md
  %(prog)s query "P5 是如何工作的？"
  %(prog)s lint
  %(prog)s summarize

环境变量：
  DASHSCOPE_API_KEY   你的百炼 API 密钥（必需）
  BAILIAN_MODEL       模型名称（默认：qwen-max）
  WIKI_AUTO_CONFIRM   自动应用更改（默认：false）
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="要运行的命令")

    # 摄入
    ingest_parser = subparsers.add_parser("ingest", help="摄入新的源文件")
    ingest_parser.add_argument("source", help="源文件路径")

    # 查询
    query_parser = subparsers.add_parser("query", help="查询知识库")
    query_parser.add_argument("question", help="要问的问题")
    query_parser.add_argument("--stream", action="store_true", help="流式输出响应")

    # 健康检查
    lint_parser = subparsers.add_parser("lint", help="健康检查知识库")
    lint_parser.add_argument("--fix", action="store_true", help="自动修复可修复的问题（如删除检查点文件）")

    # 摘要
    subparsers.add_parser("summarize", help="摘要知识库状态")

    # 验证
    subparsers.add_parser("validate", help="验证 API 密钥和连接状态")

    # 网页抓取
    fetch_parser = subparsers.add_parser("fetch", help="从 URL 抓取网页内容并分析更新知识库")
    fetch_parser.add_argument("url", help="网页 URL 地址")
    fetch_parser.add_argument("--no-ingest", action="store_true",
                              help="仅保存源文件，不自动分析摄入")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "validate":
        cmd_validate()
    elif args.command == "summarize":
        cmd_summarize()
    elif args.command == "lint":
        cmd_lint(auto_fix=getattr(args, 'fix', False))
    elif args.command == "ingest":
        cmd_ingest(args.source)
    elif args.command == "query":
        cmd_query(args.question, stream=args.stream)
    elif args.command == "fetch":
        cmd_fetch(args.url, auto_ingest=not args.no_ingest)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
