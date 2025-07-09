# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.11] - 2025-07-08

### Changed
- Improved contact information formatting in conclusion slide
- Added line breaks between contact items for better readability
- Converted website to clickable link format

## [1.0.10] - 2025-07-08

### Added
- New slide 4e: Market Opportunities showcasing startup enablement
- Per-project cost reduction metric (47-1,612x) highlighted in slide 4c
- Market segmentation by adoption barrier in README
- Bootstrap funding benefits for startups
- Entry strategies for different market segments

### Changed
- Updated README with accurate metrics from slide deck
- Reorganized target markets prioritizing startups (lowest barrier to entry)
- Enhanced README with AI Hive capabilities and proven projects
- Updated slide 8 conclusion with accurate metrics (up to 50x faster, 30x more projects)
- Added nested bullets for time-based vs per-project cost reductions

### Enhanced
- README now includes development methodologies section
- Added real-world project examples to README
- Updated roadmap with current timeline and milestones

## [1.0.9] - 2025-07-08

### Added
- AI Audio Notes Market Analysis project example to slide 7
- Web resource links for all methodologies and practices
- Living Documentation section emphasizing always-current docs
- Test coverage metrics (80%+) and testability focus
- Links for SOLID, TDD/BDD, TRIZ, Agile, DevOps, Emergent Design
- SCRUM Framework details (Epics, User Stories, Kanban)
- eXtreme Programming (XP) practices with AI-AI pair programming
- Emergent Design principles and manifesto references

### Changed
- Split slide 4 into focused sub-slides (4a-4d) for better organization
- Split slide 5 into sub-slides (5a-5c) covering SCRUM, XP, and Emergent Design
- Updated slide 5 pair programming to AI-AI only (not human-AI)
- Updated slide 7 project descriptions with accurate information
- Removed hallucinated DynamicSwarmWorkshop project

### Removed
- Deleted slides 8 and 9 (examples) per user request
- Renumbered slide 10 to slide 8 (conclusion)

### Fixed
- Cleaned up obsolete git flow feature branches
- Updated Claude settings with git remote prune permission

## [1.0.8] - 2025-07-08

### Added
- Comprehensive global pricing comparison with US, India, Vietnam, and Poland
- Annual salary calculations for all teams
- Human factor differentiators (mood, motivation, ramp-up time)
- Vietnam team data for broader comparison

### Changed
- Restructured slide-04 with detailed team cost breakdowns
- Standardized all teams to 10 people for fair comparison
- Updated AI Hive pricing to $100-500/day (was $200-500)
- Added workload dependency note for AI Hive pricing
- Emphasized AI Hive works ~50x faster than human teams
- Highlighted 24x7x365 availability with no downtime

## [1.0.7] - 2025-07-08

### Added
- Pre-commit hook to check for Claude/Anthropic references
- Advanced agent capabilities section highlighting unique features

### Changed
- Removed monetary information from slide-02 diagram
- Updated slide-02 to clarify "Example Supporting Roles"
- Updated slide-03 to show all roles (except stakeholder) as hybrid
- Changed slide-03 diagram from top-down to left-right layout
- Enhanced agent capabilities with research and architecture abilities

### Security
- Added automated checking to prevent AI provider name mentions

## [1.0.6] - 2025-07-08

### Changed
- Removed all color schemes from Mermaid diagrams across presentation slides
- Diagrams now use default monochrome styling for consistency
- Updated slides: 02-classical-team, 03-agent-augmented, 08-simple-example, 09-complex-example

## [1.0.5] - 2024-07-08

### Fixed
- Removed non-functional navigation links from slides
- First slide no longer shows inactive "Prev" link
- Last slide no longer shows inactive "Next" link
- Cleaner navigation with only working links

## [1.0.4] - 2024-07-08

### Added
- Clickable email link with mailto protocol
- Clickable links for company name and website
- Explicit line breaks for consistent formatting

### Changed
- Enhanced cover slide interactivity for better user experience

## [1.0.3] - 2024-07-08

### Changed
- Improved cover slide contact information formatting
- Added "Contact Information" heading for clarity
- Each contact detail now on separate line for better readability
- Added visual separators for professional appearance

## [1.0.2] - 2024-07-08

### Fixed
- Added missing contact information to slide cover
- Cover slide now includes email, phone, and website

## [1.0.1] - 2024-07-08

### Changed
- Updated author information to Alex Fedin
- Updated contact email to af@o2.services
- Added phone number +1 (425) 351-1652
- Personalized all business contact details in documentation

## [1.0.0] - 2024-07-08

### Added
- Initial release of AI Hive business documentation
- Complete pitch deck "From Team to Agents" with 10 slides
- Mermaid diagrams for team structures and architectures
- Navigation system between all documentation files
- Linting configuration with markdownlint
- Pre-commit hooks for code quality
- Gitflow branch enforcement to ensure proper development workflow
- Project README with overview and structure
- CLAUDE.md with project guidelines and rules

### Security
- Gitflow enforcement prevents direct commits to main/master branches
- All commits must go through feature branches
