#!/bin/bash
# setup.sh — LLM4Rec Wiki 快速启动设置

set -e

echo "🚀 正在设置 LLM4Rec Wiki..."

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3。请安装 Python 3.8+。"
    exit 1
fi

echo "✅ Python $(python3 --version)"

# 创建虚拟环境（可选但推荐）
if [ ! -d "venv" ]; then
    echo "📦 正在创建虚拟环境..."
    python3 -m venv venv
    echo "✅ 虚拟环境已创建"
fi

# 激活并安装依赖
echo "📦 正在安装依赖..."
source venv/bin/activate
pip install -q -r requirements.txt
echo "✅ 依赖已安装"

# 设置 .env 文件
if [ ! -f ".env" ]; then
    echo "🔑 正在从模板创建 .env 文件..."
    cp .env.example .env
    echo "⚠️  请编辑 .env 并添加你的 DASHSCOPE_API_KEY"
    echo "   获取密钥地址：https://bailian.console.aliyun.com/"
else
    echo "✅ .env 文件已存在"
fi

# 使CLI可执行
chmod +x tools/llm_wiki.py

# 初始化git仓库（如果尚未完成）
if [ ! -d ".git" ]; then
    echo "📝 正在初始化 git 仓库..."
    git init
    git add -A
    echo "✅ Git 仓库已初始化"
fi

echo ""
echo "🎉 设置完成！"
echo ""
echo "后续步骤："
echo "  1. 编辑 .env 并添加你的 DASHSCOPE_API_KEY"
echo "  2. 激活环境：source venv/bin/activate"
echo "  3. 尝试命令：python tools/llm_wiki.py summarize"
echo ""
