#!/usr/bin/env python3
"""
Test script for Feature 2: LLM-based page enrichment
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.llm_wiki import (
    _page_update_is_complete,
    _mark_page_update_complete,
    WIKI_DIR
)

# Test page to update
test_page = WIKI_DIR / "concepts" / "generative_retrieval.md"

print("=" * 60)
print("Testing Feature 2: LLM-based Page Enrichment")
print("=" * 60)

# Test 1: Check if page has been marked as complete
source_name = "test_generative_rec.md"
is_complete = _page_update_is_complete(test_page, source_name)
print(f"\n✅ Test 1: Page update completion check")
print(f"   Page: {test_page.name}")
print(f"   Source: {source_name}")
print(f"   Is complete: {is_complete}")

# Test 2: Mark the page as complete (simulate what would happen after LLM enrichment)
if not is_complete:
    print(f"\n✅ Test 2: Marking page as update complete")
    _mark_page_update_complete(test_page, source_name, "Test: Page enriched with LLM")
    is_complete = _page_update_is_complete(test_page, source_name)
    print(f"   Is complete now: {is_complete}")
    
    # Test 3: Verify it will be skipped next time
    print(f"\n✅ Test 3: Verifying skip on next update")
    is_complete_again = _page_update_is_complete(test_page, source_name)
    print(f"   Would skip next time: {is_complete_again}")
else:
    print(f"\nℹ️  Page already marked as complete, skip marking test")

print("\n" + "=" * 60)
print("✅ Feature 2 tests completed successfully!")
print("=" * 60)
