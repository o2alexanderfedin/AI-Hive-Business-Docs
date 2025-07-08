#!/usr/bin/env python3
"""Update the primary color in Mermaid diagrams from #6B7F95 to a lighter shade."""

import os
import re

# Define the market analysis directory
MARKET_ANALYSIS_DIR = "business-documents/market-analysis"

# Color replacements
OLD_PRIMARY = "#6B7F95"
NEW_PRIMARY = "#A8B8D0"  # Lighter blue-gray

OLD_BORDER = "#4A5A6A"
NEW_BORDER = "#8A9AB2"  # Lighter border to match

def update_colors_in_file(file_path):
    """Update colors in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace primary color
    content = content.replace(f"'primaryColor': '{OLD_PRIMARY}'", f"'primaryColor': '{NEW_PRIMARY}'")
    content = content.replace(f"'mainBkg': '{OLD_PRIMARY}'", f"'mainBkg': '{NEW_PRIMARY}'")
    content = content.replace(f"'activeTaskBorderColor': '{OLD_PRIMARY}'", f"'activeTaskBorderColor': '{NEW_PRIMARY}'")

    # Replace border colors for consistency
    content = content.replace(f"'primaryBorderColor': '{OLD_BORDER}'", f"'primaryBorderColor': '{NEW_BORDER}'")
    content = content.replace(f"'lineColor': '{OLD_BORDER}'", f"'lineColor': '{NEW_BORDER}'")
    content = content.replace(f"'defaultLinkColor': '{OLD_BORDER}'", f"'defaultLinkColor': '{NEW_BORDER}'")
    content = content.replace(f"'actorBorder': '{OLD_BORDER}'", f"'actorBorder': '{NEW_BORDER}'")
    content = content.replace(f"'actorLineColor': '{OLD_BORDER}'", f"'actorLineColor': '{NEW_BORDER}'")
    content = content.replace(f"'activationBorderColor': '{OLD_BORDER}'", f"'activationBorderColor': '{NEW_BORDER}'")
    content = content.replace(f"'taskBorderColor': '{OLD_BORDER}'", f"'taskBorderColor': '{NEW_BORDER}'")

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to update colors in all markdown files."""
    print("Updating primary color to lighter shade in market analysis documents...")

    updated_files = []

    # Process all markdown files
    for filename in os.listdir(MARKET_ANALYSIS_DIR):
        if filename.endswith('.md') and filename != '01-executive-summary.md':
            file_path = os.path.join(MARKET_ANALYSIS_DIR, filename)
            if update_colors_in_file(file_path):
                updated_files.append(filename)
                print(f"  ✓ Updated {filename}")

    if updated_files:
        print(f"\nSuccessfully updated {len(updated_files)} files")
    else:
        print("\nNo files needed updating")

if __name__ == "__main__":
    main()
