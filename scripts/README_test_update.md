# test_update.sh 使用说明

## 功能

扫描 `raw/sources` 目录中的所有源文档，检查是否在 `wiki/sources` 中有对应的已生成文档。如果缺失，则：

1. 提取文档的 arxiv URL（从 frontmatter 或文件名中）
2. 调用 `tools/llm_wiki.py fetch <url>` 重新抓取并生成规范的源文档
3. 删除原始文档（避免重复）

## 用法

### 预览模式（推荐先运行）

```bash
bash scripts/test_update.sh --dry-run
```

这会列出所有需要处理的文件，但不会实际执行任何操作。

### 执行模式

```bash
bash scripts/test_update.sh
```

这会实际执行 fetch 和删除操作。

### 后台执行（推荐，因为耗时较长）

```bash
nohup bash scripts/test_update.sh > scripts/test_update.log 2>&1 &
```

查看进度：
```bash
tail -f scripts/test_update.log
```

## 工作原理

1. **检测缺失文件**：对比 `raw/sources/` 和 `wiki/sources/` 目录
2. **提取 URL**：
   - 优先从 frontmatter 的 `url` 字段提取
   - 其次从 `original_url` 字段提取
   - 最后从文件名中的 arxiv ID 构造 URL（如 `2507_paper_25071555_...` → `https://arxiv.org/abs/2507.1555`）
3. **执行 fetch**：调用 `llm_wiki.py fetch <url> --no-ingest` 生成新格式的源文档
4. **清理**：删除原始文档

## 注意事项

- ⏱️ **耗时较长**：每个文件需要调用 LLM 生成中文摘要，建议后台执行
- 🔒 **不会覆盖**：如果 `wiki/sources/` 中已存在同名文件，会跳过
- ⚠️ **无法处理的文件**：没有 arxiv URL 的文件（如 `llm4rec_survey_2024.md`、`FEATURE_IMPLEMENTATION_SUMMARY.md`）会被跳过
- ✅ **安全**：仅在 fetch 成功后才删除原始文件，失败会保留

## 输出示例

```
==============================================
🔄 重新生成缺失的 wiki/sources 文档
==============================================

[1] 📄 处理: 2604_paper_26040268_MBGR_...
  🔗 URL: https://arxiv.org/abs/2604.02684
  🤖 正在调用 llm_wiki.py fetch...
  ✅ fetch 成功
  🗑️  删除原始文档: 2604_paper_26040268_MBGR_...

==============================================
📊 处理完成统计
==============================================
总文件数: 40
已处理: 4
已存在（跳过）: 36
失败: 0
==============================================
```

## 后续步骤

脚本执行完成后，建议：

1. 检查生成的新文件：`ls raw/sources/`
2. 运行 ingest 处理新文件：`python tools/llm_wiki.py ingest raw/sources/<new_file>.md`
3. 运行 lint 检查知识库健康：`python tools/llm_wiki.py lint`
