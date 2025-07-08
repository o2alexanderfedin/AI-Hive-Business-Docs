#!/usr/bin/env python3
"""
Update all Mermaid pie charts in market analysis documents to use custom colors.
"""

import os
import re

def update_pie_charts(file_path):
    """Update Mermaid pie charts in a single file to use custom colors."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Professional color palette with lighter colors for better text readability
    # All colors are light enough for black text to be clearly visible
    color_init = "%%{init: {'theme': 'base', 'themeVariables': {'pie1': '#6B7F95', 'pie2': '#5DBCB6', 'pie3': '#84D4F5', 'pie4': '#B3B2D8', 'pie5': '#E5C4CA', 'pie6': '#FFD54F', 'pie7': '#FFB74D', 'pie8': '#E1B3C4', 'pieTextColor': '#000000', 'pieTitleTextColor': '#000000', 'pieSectionTextSize': '14px', 'pieLegendTextColor': '#000000', 'pieLegendTextSize': '14px', 'pieStrokeColor': '#000000', 'pieStrokeWidth': '1px', 'pieOuterStrokeWidth': '1px', 'pieOuterStrokeColor': '#000000'}}}%%"

    # First, remove any existing color init lines
    content = re.sub(r'%%\{init:.*?pie\d+.*?\}%%\n', '', content)

    # Pattern to match pie charts
    # Looking for pie charts that start with "pie title" or just "pie"
    pattern = r'(```mermaid\n)(pie\s+(?:title\s+"[^"]+"\s*\n|title\s+[^\n]+\n)?)'

    def add_color_init(match):
        mermaid_start = match.group(1)
        pie_content = match.group(2)
        # Add color init after mermaid start
        return f"{mermaid_start}{color_init}\n{pie_content}"

    # Replace all occurrences
    updated_content = re.sub(pattern, add_color_init, content, flags=re.MULTILINE)

    # Check if any changes were made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

def main():
    # Define the directory containing market analysis files
    market_analysis_dir = os.path.expanduser('~/Projects/O2.services.AI-Hive/business-documents/market-analysis')

    print("Updating pie chart colors in market analysis documents...")
    updated_files = []

    # Process all markdown files in the directory
    for filename in os.listdir(market_analysis_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(market_analysis_dir, filename)
            if update_pie_charts(file_path):
                updated_files.append(filename)

    # Print results
    if updated_files:
        print(f"\nSuccessfully updated {len(updated_files)} files:")
        for file in sorted(updated_files):
            print(f"  - {file}")
    else:
        print("\nNo pie charts found to update.")

if __name__ == "__main__":
    main()
