#!/usr/bin/env python3
"""
Update all Mermaid diagrams in market analysis documents to use CSS classes
for consistent styling with inset shadows.
"""

import os
import re

def update_mermaid_diagrams(file_path):
    """Update Mermaid diagrams in a single file to use CSS classes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the existing styled div blocks with Mermaid diagrams
    pattern = r'<div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">\s*\n\s*```mermaid\n(.*?)\n```\s*\n\s*</div>'

    def replace_with_class(match):
        diagram_content = match.group(1)
        return f'''<div class="mermaid-diagram-wrapper">

```mermaid
{diagram_content}
```

</div>'''

    # Replace all occurrences
    updated_content = re.sub(pattern, replace_with_class, content, flags=re.DOTALL)

    # Check if any changes were made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

def add_css_link_to_files(directory):
    """Add CSS link to the top of each markdown file if not already present."""
    css_link = '<link rel="stylesheet" href="styles.css">\n\n'

    for filename in os.listdir(directory):
        if filename.endswith('.md') and filename != 'README.md':
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if CSS link already exists
            if '<link rel="stylesheet" href="styles.css">' not in content:
                # Add CSS link after the navigation line
                lines = content.split('\n')
                insert_index = 0

                # Find the first non-navigation line
                for i, line in enumerate(lines):
                    if line.strip() and not line.startswith('[🏠'):
                        insert_index = i
                        break

                lines.insert(insert_index, css_link.strip())

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))

                print(f"Added CSS link to {filename}")

def main():
    # Define the directory containing market analysis files
    market_analysis_dir = os.path.expanduser('~/Projects/O2.services.AI-Hive/business-documents/market-analysis')

    # First, add CSS links to all files
    print("Adding CSS links to markdown files...")
    add_css_link_to_files(market_analysis_dir)

    # Then update the diagram styling
    print("\nUpdating Mermaid diagram styling...")
    updated_files = []

    # Process all markdown files in the directory
    for filename in os.listdir(market_analysis_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(market_analysis_dir, filename)
            if update_mermaid_diagrams(file_path):
                updated_files.append(filename)

    # Print results
    if updated_files:
        print(f"\nSuccessfully updated {len(updated_files)} files:")
        for file in sorted(updated_files):
            print(f"  - {file}")
    else:
        print("\nNo files needed updating.")

if __name__ == "__main__":
    main()
