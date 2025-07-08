# Project Assets

This directory contains shared assets used across all documentation in the O2.services AI Hive project.

## Directory Structure

```
assets/
├── css/              # Stylesheets
│   └── styles.css    # Common styles for all markdown documents
├── images/           # Shared images, logos, and graphics
└── fonts/            # Custom fonts (if needed)
```

## Usage

### For Business Documents

From files in `business-documents/market-analysis/`:
```html
<link rel="stylesheet" href="../../assets/css/styles.css">
```

### For Presentations

From files in `presentations/[subfolder]/`:
```html
<link rel="stylesheet" href="../../assets/css/styles.css">
```

From files directly in `presentations/`:
```html
<link rel="stylesheet" href="../assets/css/styles.css">
```

## CSS Features

The `styles.css` file provides:

1. **Mermaid Diagram Wrapper**
   - Carved-in visual effect with inset shadows
   - Consistent padding and margins
   - Subtle background color

2. **Table Styling**
   - Consistent borders and spacing
   - Black text for readability
   - Professional appearance

3. **Color Scheme**
   - Muted, professional color palette
   - High contrast for accessibility
   - Consistent across all diagrams

## Guidelines

- Keep assets organized by type (css, images, fonts)
- Use descriptive filenames
- Document any new CSS classes or features
- Consider performance - optimize images before adding
- Maintain consistency across all documentation types
