#!/bin/bash

# Check for references to Claude or Anthropic in staged files
# This is a pre-commit hook to ensure we don't accidentally mention these names

# Get list of staged files
staged_files=$(git diff --cached --name-only --diff-filter=ACM)

# Skip if no files are staged
if [ -z "$staged_files" ]; then
    exit 0
fi

# Initialize flag
found_references=false
problem_files=()

# Check each staged file
for file in $staged_files; do
    # Skip binary files, this script itself, and configuration files
    if [[ "$file" == *.png ]] || [[ "$file" == *.jpg ]] || [[ "$file" == *.jpeg ]] || \
       [[ "$file" == *.gif ]] || [[ "$file" == *.ico ]] || [[ "$file" == *.pdf ]] || \
       [[ "$file" == *"check-no-claude-anthropic.sh" ]] || \
       [[ "$file" == *".config/pre-commit-config.yaml" ]] || \
       [[ "$file" == *".claude/"* ]] || \
       [[ "$file" == "CLAUDE.md" ]]; then
        continue
    fi

    # Check if file exists (might be deleted)
    if [ ! -f "$file" ]; then
        continue
    fi

    # Search for Claude or Anthropic (case insensitive)
    if grep -i -E "(claude|anthropic)" "$file" > /dev/null 2>&1; then
        found_references=true
        problem_files+=("$file")
    fi
done

# If references found, show warning and details
if [ "$found_references" = true ]; then
    echo "⚠️  WARNING: References to Claude or Anthropic found in staged files!"
    echo ""
    echo "As per CLAUDE.md guidelines:"
    echo "  'DO NOT mention Claude, Anthropic, or any specific AI provider names anywhere in the documents.'"
    echo ""
    echo "Files containing references:"
    for file in "${problem_files[@]}"; do
        echo "  • $file"
        # Show the specific lines with context
        echo "    Lines with references:"
        grep -n -i -E "(claude|anthropic)" "$file" | sed 's/^/      /'
        echo ""
    done
    echo "Please remove these references before committing."
    echo ""
    echo "Note: This is a warning. The commit will proceed, but you should fix these references."
    echo "      To fix, either amend this commit or create a follow-up commit."
    echo ""
fi

# Exit successfully (warning only, don't block commit)
exit 0
