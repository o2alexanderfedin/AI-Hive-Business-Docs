#!/bin/bash

# Get the current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Define allowed branch patterns for gitflow
allowed_patterns=(
    "^feature/.*"
    "^bugfix/.*"
    "^release/.*"
    "^hotfix/.*"
    "^support/.*"
    "^develop$"
    "^main$"
    "^master$"
)

# Check if current branch matches any allowed pattern
branch_valid=false
for pattern in "${allowed_patterns[@]}"; do
    if [[ "$current_branch" =~ $pattern ]]; then
        branch_valid=true
        break
    fi
done

# If on main/master, always fail (should not commit directly)
if [[ "$current_branch" == "main" ]] || [[ "$current_branch" == "master" ]]; then
    echo "❌ ERROR: Direct commits to $current_branch branch are not allowed!"
    echo ""
    echo "Please use git flow commands to create a proper branch:"
    echo ""
    echo "For new features:"
    echo "  git flow feature start <feature-name>"
    echo ""
    echo "For bug fixes:"
    echo "  git flow bugfix start <bugfix-name>"
    echo ""
    echo "For urgent production fixes:"
    echo "  git flow hotfix start <hotfix-name>"
    echo ""
    echo "For release preparation:"
    echo "  git flow release start <version>"
    echo ""
    echo "Note: Always use 'git flow' commands instead of creating branches manually."
    echo "This ensures proper branch tracking and gitflow workflow compliance."
    exit 1
fi

# If branch doesn't match gitflow pattern
if [ "$branch_valid" = false ]; then
    echo "❌ ERROR: Current branch '$current_branch' does not follow gitflow naming conventions!"
    echo ""
    echo "Please use git flow commands to create a proper branch:"
    echo ""
    echo "For new features:"
    echo "  git flow feature start <feature-name>"
    echo ""
    echo "For bug fixes:"
    echo "  git flow bugfix start <bugfix-name>"
    echo ""
    echo "For urgent production fixes:"
    echo "  git flow hotfix start <hotfix-name>"
    echo ""
    echo "For long-term support:"
    echo "  git flow support start <version> <base>"
    echo ""
    echo "Valid gitflow branch patterns:"
    echo "  • feature/*  - for new features"
    echo "  • bugfix/*   - for bug fixes"
    echo "  • release/*  - for release preparation"
    echo "  • hotfix/*   - for urgent production fixes"
    echo "  • support/*  - for long-term support branches"
    echo "  • develop    - for integration branch"
    echo ""
    echo "Note: Always use 'git flow' commands instead of creating branches manually."
    exit 1
fi

# All good!
exit 0
