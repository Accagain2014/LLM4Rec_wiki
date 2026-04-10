#!/bin/bash
# test_update.sh - 扫描 raw/sources 目录，为没有生成 wiki/sources 文档的文件重新执行 fetch
# 用法: bash scripts/test_update.sh [--dry-run]
#   --dry-run: 仅预览，不实际执行

set -e

export WIKI_AUTO_CONFIRM=true

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
RAW_SOURCES_DIR="$PROJECT_DIR/raw/sources"
WIKI_SOURCES_DIR="$PROJECT_DIR/wiki/sources"
LLM_WIKI_SCRIPT="$PROJECT_DIR/tools/llm_wiki.py"

source venv_llm4rec_wiki/bin/activate

DRY_RUN=false
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
fi

echo "=============================================="
echo "🔄 重新生成缺失的 wiki/sources 文档"
echo "=============================================="
echo ""

# 获取 raw/sources 中的所有 .md 文件
cd "$PROJECT_DIR"

TOTAL=0
PROCESSED=0
SKIPPED=0
FAILED=0

for raw_file in "$RAW_SOURCES_DIR"/*.md; do
    # 跳过非文件条目
    [ -f "$raw_file" ] || continue
    
    filename=$(basename "$raw_file")
    TOTAL=$((TOTAL + 1))
    
    # 检查 wiki/sources 中是否已存在同名文件
    wiki_file="$WIKI_SOURCES_DIR/$filename"
    if [ -f "$wiki_file" ]; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    
    # 文件缺失，需要处理
    echo "[$((PROCESSED + 1))] 📄 处理: $filename"
    
    # 尝试从文件 frontmatter 中提取 arxiv URL
    # 优先使用 url 字段，如果没有则尝试 original_url
    arxiv_url=$(grep -m1 '^url:' "$raw_file" | sed 's/^url: *//; s/^"//; s/"$//' | tr -d '"' || echo "")
    
    if [ -z "$arxiv_url" ]; then
        arxiv_url=$(grep -m1 '^original_url:' "$raw_file" | sed 's/^original_url: *//; s/^"//; s/"$//' | tr -d '"' || echo "")
    fi
    
    # 如果 frontmatter 中没有 URL，尝试从文件名中提取 arxiv ID 并构造 URL
    if [ -z "$arxiv_url" ]; then
        # 匹配文件名中的 arxiv ID 模式，如 2507_paper_25071555_... 中的 25071555
        arxiv_id=$(echo "$filename" | grep -oP '\d{4}\.\d{4,5}' | head -1 || echo "")
        if [ -n "$arxiv_id" ]; then
            arxiv_url="https://arxiv.org/abs/$arxiv_id"
        fi
    fi
    
    if [ -z "$arxiv_url" ]; then
        echo "  ⚠️  无法提取 arxiv URL，跳过"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    
    echo "  🔗 URL: $arxiv_url"
    
    if [ "$DRY_RUN" = true ]; then
        echo "  [DRY RUN] 将执行: python $LLM_WIKI_SCRIPT fetch $arxiv_url"
        echo "  [DRY RUN] 完成后将删除: $raw_file"
        PROCESSED=$((PROCESSED + 1))
        continue
    fi
    
    # 执行 fetch 命令（使用 --no-ingest 仅保存源文件）
    echo "  🤖 正在调用 llm_wiki.py fetch..."
    if python "$LLM_WIKI_SCRIPT" fetch "$arxiv_url"; then
        echo "  ✅ fetch 成功"
        
        # 删除原始文档
        echo "  🗑️  删除原始文档: $filename"
        rm "$raw_file"
        
        PROCESSED=$((PROCESSED + 1))
    else
        echo "  ❌ fetch 失败，保留原始文档"
        FAILED=$((FAILED + 1))
    fi
    
    echo ""
done

echo ""
echo "=============================================="
echo "📊 处理完成统计"
echo "=============================================="
echo "总文件数: $TOTAL"
echo "已处理: $PROCESSED"
echo "已存在（跳过）: $SKIPPED"
echo "失败: $FAILED"
echo "=============================================="
