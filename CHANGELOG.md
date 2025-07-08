# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.8] - 2025-07-08

### Added
- Comprehensive global pricing comparison with US, India, Vietnam, and Poland
- Annual salary calculations for all teams
- Human factor differentiators (mood, motivation, ramp-up time)
- Vietnam team data for broader comparison

### Changed
- Restructured slide-04 with detailed team cost breakdowns
- Standardized all teams to 10 people for fair comparison
- Updated AI Swarm pricing to $100-500/day (was $200-500)
- Added workload dependency note for AI Swarm pricing
- Emphasized AI Swarm works ~50x faster than human teams
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
