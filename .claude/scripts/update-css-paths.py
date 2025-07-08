#!/usr/bin/env python3
"""Update CSS paths in markdown files to use the central assets directory."""

import os
import re

def update_css_path_in_file(file_path):
    """Update CSS path in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace the old CSS link with the new path
    # The new path needs to go up one directory from market-analysis to business-documents
    # then into assets/css/
    content = re.sub(
        r'<link rel="stylesheet" href="styles\.css">',
        '<link rel="stylesheet" href="../assets/css/styles.css">',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Update CSS paths in all market analysis markdown files."""
    market_analysis_dir = "business-documents/market-analysis"

    print("Updating CSS paths in markdown files...")
    updated_files = []

    for filename in os.listdir(market_analysis_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(market_analysis_dir, filename)
            if update_css_path_in_file(file_path):
                updated_files.append(filename)
                print(f"  ✓ Updated {filename}")

    if updated_files:
        print(f"\nSuccessfully updated {len(updated_files)} files")
    else:
        print("\nNo files needed updating")

if __name__ == "__main__":
    main()
