#!/usr/bin/env python3
"""
Update all markdown tables in market analysis documents to use the same
styled wrapper as diagrams for consistent visual presentation.
"""

import os
import re

def wrap_table(table_text):
    """Wrap a table with the styled div wrapper."""
    return f'''<div class="mermaid-diagram-wrapper">

{table_text}

</div>'''

def find_and_wrap_tables(content):
    """Find all markdown tables and wrap them with styled divs."""
    lines = content.split('\n')
    new_lines = []
    in_table = False
    table_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if line is part of a table (contains | and isn't already in a div)
        if '|' in line and not line.strip().startswith('<'):
            # Check if this is the start of a new table
            if not in_table:
                # Look for header separator line to confirm it's a table
                if i + 1 < len(lines) and '|' in lines[i + 1] and re.match(r'^[\s\|:\-]+$', lines[i + 1]):
                    in_table = True
                    table_lines = [line]
                else:
                    # Not a table, just a line with |
                    new_lines.append(line)
            else:
                # Continue collecting table lines
                table_lines.append(line)
        else:
            # Not a table line
            if in_table:
                # End of table, wrap it
                # Check if already wrapped
                if i > 0 and '<div class="mermaid-diagram-wrapper">' in lines[i-len(table_lines)-1]:
                    # Already wrapped, just add the lines
                    new_lines.extend(table_lines)
                else:
                    # Wrap the table
                    wrapped_table = wrap_table('\n'.join(table_lines))
                    new_lines.append(wrapped_table)
                in_table = False
                table_lines = []

            new_lines.append(line)

        i += 1

    # Handle case where file ends with a table
    if in_table and table_lines:
        wrapped_table = wrap_table('\n'.join(table_lines))
        new_lines.append(wrapped_table)

    return '\n'.join(new_lines)

def process_file(file_path):
    """Process a single markdown file to wrap tables."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if no tables found
    if '|' not in content:
        return False

    # Check if tables are already wrapped
    original_content = content

    # Process the content
    updated_content = find_and_wrap_tables(content)

    # Check if any changes were made
    if updated_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True

    return False

def main():
    # Define the directory containing market analysis files
    market_analysis_dir = os.path.expanduser('~/Projects/O2.services.AI-Hive/business-documents/market-analysis')

    print("Updating table styling in market analysis documents...")
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
        print("\nNo tables found to update.")

if __name__ == "__main__":
    main()
