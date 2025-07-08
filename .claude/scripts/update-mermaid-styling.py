#!/usr/bin/env python3
"""
Update Mermaid diagram styling in markdown files
Wraps all Mermaid code blocks with HTML divs for better styling
"""

import os
import re
import sys

def wrap_mermaid_diagram(content):
    """Wrap Mermaid diagrams with styled HTML blocks"""
    # Pattern to match Mermaid code blocks
    pattern = r'```mermaid\n(.*?)\n```'

    def replace_diagram(match):
        diagram_content = match.group(1)
        return f'''<div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">

```mermaid
{diagram_content}
```

</div>'''

    # Replace all Mermaid diagrams
    updated_content = re.sub(pattern, replace_diagram, content, flags=re.DOTALL)
    return updated_content

def process_file(filepath):
    """Process a single markdown file"""
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has Mermaid diagrams
    if '```mermaid' not in content:
        print(f"  No Mermaid diagrams found")
        return False

    # Check if diagrams are already wrapped
    if '<div style="background-color: #f5f5f5' in content:
        print(f"  Diagrams already styled")
        return False

    # Update content
    updated_content = wrap_mermaid_diagram(content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"  ✓ Updated diagrams")
    return True

def main():
    """Process all market analysis markdown files"""
    market_analysis_dir = "business-documents/market-analysis"

    if not os.path.exists(market_analysis_dir):
        print(f"Error: Directory {market_analysis_dir} not found")
        sys.exit(1)

    # Get all markdown files
    md_files = [f for f in os.listdir(market_analysis_dir) if f.endswith('.md')]
    md_files.sort()

    updated_count = 0

    print(f"Found {len(md_files)} markdown files")
    print("-" * 50)

    for filename in md_files:
        filepath = os.path.join(market_analysis_dir, filename)
        if process_file(filepath):
            updated_count += 1

    print("-" * 50)
    print(f"✅ Updated {updated_count} files")

if __name__ == "__main__":
    main()
