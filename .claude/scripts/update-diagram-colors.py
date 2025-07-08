#!/usr/bin/env python3
"""
Update non-pie Mermaid diagrams to use muted colors similar to pie charts.
Also updates text colors to black for better readability.
"""

import os
import re

def create_theme_init():
    """Create the theme initialization with muted colors."""
    # Using a similar palette to the pie charts but adapted for flowcharts
    return """%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#6B7F95',
    'primaryTextColor': '#000000',
    'primaryBorderColor': '#4A5A6A',
    'lineColor': '#4A5A6A',
    'secondaryColor': '#5DBCB6',
    'secondaryTextColor': '#000000',
    'secondaryBorderColor': '#3D9A94',
    'tertiaryColor': '#84D4F5',
    'tertiaryTextColor': '#000000',
    'tertiaryBorderColor': '#5ABCD8',
    'background': '#F5F5F5',
    'mainBkg': '#6B7F95',
    'secondBkg': '#5DBCB6',
    'tertiaryBkg': '#84D4F5',
    'mainContrastColor': '#000000',
    'darkMode': false,
    'fontFamily': 'Arial, sans-serif',
    'fontSize': '14px',
    'labelBackground': '#E8E8E8',
    'textColor': '#000000',
    'nodeBkg': '#B3B2D8',
    'nodeTextColor': '#000000',
    'nodeBorder': '#8A89C0',
    'clusterBkg': '#E5C4CA',
    'clusterBorder': '#CDA2AB',
    'defaultLinkColor': '#4A5A6A',
    'titleColor': '#000000',
    'edgeLabelBackground': '#F5F5F5',
    'actorBorder': '#4A5A6A',
    'actorBkg': '#B3B2D8',
    'actorTextColor': '#000000',
    'actorLineColor': '#4A5A6A',
    'signalColor': '#000000',
    'signalTextColor': '#000000',
    'activationBorderColor': '#4A5A6A',
    'activationBkgColor': '#E5C4CA',
    'sequenceNumberColor': '#000000',
    'sectionBkgColor': '#FFD54F',
    'altSectionBkgColor': '#FFB74D',
    'sectionBkgColor2': '#E1B3C4',
    'taskBorderColor': '#4A5A6A',
    'taskBkgColor': '#B3B2D8',
    'taskTextColor': '#000000',
    'taskTextLightColor': '#000000',
    'taskTextOutsideColor': '#000000',
    'taskTextClickableColor': '#000000',
    'activeTaskBorderColor': '#6B7F95',
    'activeTaskBkgColor': '#84D4F5',
    'gridColor': '#C0C0C0',
    'doneTaskBkgColor': '#5DBCB6',
    'doneTaskBorderColor': '#3D9A94',
    'critBorderColor': '#E27D00',
    'critBkgColor': '#FFB74D',
    'todayLineColor': '#E27D00',
    'labelColor': '#000000',
    'errorBkgColor': '#E1B3C4',
    'errorTextColor': '#000000'
  }
}}%%"""

def update_diagram(content, diagram_type):
    """Update a diagram with the new theme."""
    # Pattern to match diagrams without existing init
    pattern = rf'(```mermaid\n)({diagram_type}(?:\s+[^\n]+)?\n)'

    def add_theme_init(match):
        mermaid_start = match.group(1)
        diagram_content = match.group(2)
        # Check if init already exists
        if '%%{init:' in content[match.start():match.end() + 100]:
            return match.group(0)
        return f"{mermaid_start}{create_theme_init()}\n{diagram_content}"

    return re.sub(pattern, add_theme_init, content, flags=re.MULTILINE)

def remove_existing_fills(content):
    """Remove existing style fill directives that might conflict."""
    # Remove style fill lines that set bright colors
    content = re.sub(r'\s*style\s+\w+\s+fill:#[0-9A-Fa-f]{6}(?:,color:#[0-9A-Fa-f]{6})?\s*\n', '\n', content)
    return content

def process_file(file_path):
    """Process a single file to update diagram colors."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Skip if no mermaid diagrams
    if '```mermaid' not in content:
        return False

    # First remove any existing fill styles that might override our theme
    content = remove_existing_fills(content)

    # Update different diagram types
    for diagram_type in ['graph', 'flowchart', 'gantt', 'journey', 'scatter', 'sequenceDiagram', 'classDiagram', 'stateDiagram', 'erDiagram']:
        content = update_diagram(content, diagram_type)

    # Check if any changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    # Define the directory containing market analysis files
    market_analysis_dir = os.path.expanduser('~/Projects/O2.services.AI-Hive/business-documents/market-analysis')

    print("Updating diagram colors in market analysis documents...")
    updated_files = []

    # Process all markdown files in the directory
    for filename in os.listdir(market_analysis_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(market_analysis_dir, filename)
            if process_file(file_path):
                updated_files.append(filename)

    # Print results
    if updated_files:
        print(f"\nSuccessfully updated {len(updated_files)} files:")
        for file in sorted(updated_files):
            print(f"  - {file}")
    else:
        print("\nNo diagrams found to update.")

if __name__ == "__main__":
    main()
