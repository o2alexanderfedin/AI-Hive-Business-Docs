#!/usr/bin/env python3
"""Update CSS paths in markdown files to use the root-level assets directory."""

import os
import re

def update_css_path_in_file(file_path, relative_path_to_root):
    """Update CSS path in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace the current CSS link with the new path
    # The path needs to go up to the root and then into assets/css/
    css_path = f"{relative_path_to_root}assets/css/styles.css"

    # Match any existing CSS link (both old and new paths)
    content = re.sub(
        r'<link rel="stylesheet" href="[^"]+styles\.css">',
        f'<link rel="stylesheet" href="{css_path}">',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_directory(directory, relative_path_to_root):
    """Process all markdown files in a directory."""
    updated_files = []

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            if update_css_path_in_file(file_path, relative_path_to_root):
                updated_files.append(filename)
                print(f"  ✓ Updated {directory}/{filename}")

    return updated_files

def main():
    """Update CSS paths in all markdown files."""
    print("Updating CSS paths to use root-level assets directory...")

    total_updated = 0

    # Update business-documents/market-analysis files
    # These need to go up two directories (../../)
    market_dir = "business-documents/market-analysis"
    updated = process_directory(market_dir, "../../")
    total_updated += len(updated)

    # Check if there are any markdown files in presentations
    if os.path.exists("presentations"):
        for item in os.listdir("presentations"):
            item_path = os.path.join("presentations", item)
            if os.path.isdir(item_path):
                # For subdirectories in presentations, path is ../../
                updated = process_directory(item_path, "../../")
                total_updated += len(updated)
            elif item.endswith('.md'):
                # For files directly in presentations, path is ../
                if update_css_path_in_file(os.path.join("presentations", item), "../"):
                    print(f"  ✓ Updated presentations/{item}")
                    total_updated += 1

    print(f"\nTotal files updated: {total_updated}")

if __name__ == "__main__":
    main()
