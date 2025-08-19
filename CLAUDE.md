# Document to HTML Converter Project

## Project Overview
This project contains a web-based IDE for converting structured documents with section markers into HTML code. The main tool processes documents with `[SECTION_NAME]...[SECTION_NAME END]` markers and generates corresponding HTML sections with intelligent fallback content and comprehensive image handling.

## Key Files
- `web_ide_final.html` - Main web IDE with AI-powered content parsing (v3.7)
- `CLAUDE.md` - Project documentation and instructions
- `package.json` & `package-lock.json` - Node.js dependencies
- `vercel.json` - Deployment configuration

## Main Features
- **Document Processing**: Converts documents with descriptive section markers
- **AI Integration**: Uses Groq API for intelligent content parsing (fallback to rule-based parsing)
- **Default Content Generation**: All sections generate professional static HTML when content is empty
- **Multiple Section Types**: Supports 14 different section types with smart parsing
- **File Upload**: Supports both Word documents (.docx) and text files
- **Live Preview**: Real-time HTML preview with Bootstrap styling
- **Image Fallback System**: Comprehensive broken image handling with static HTML images
- **Technology Stack Parsing**: Advanced category-based technology parsing
- **Descriptive Section Names**: All sections use clear, descriptive naming conventions

## Section Types Supported (14 Total)

### Updated Section Names (v3.5+):
- **HERO_BANNER_SECTION**: Main landing section with title, description, bullet points, and contact form
- **FAQ_SECTION**: Frequently asked questions with expandable accordion answers
- **CTA_SIMPLE_SECTION**: Simple call-to-action sections with buttons
- **CTA_WITH_LIST_SECTION**: Advanced CTA with statistics and dual buttons
- **SERVICES_GRID_SECTION**: Grid layout of services with images and descriptions
- **SERVICES_ACCORDION_SECTION**: Collapsible accordion for services (single/multiple sections)
- **BENEFITS_SECTION**: Standard benefits listing with icons and descriptions
- **BENEFITS_TWO**: Benefits section with title/description pairs (unchanged)
- **CONTENT_WITH_FORM_SECTION**: Contact forms with customizable fields
- **PORTFOLIO_SECTION**: Project showcase with technology stacks
- **TESTIMONIAL_SECTION**: Customer testimonials with author attribution
- **TECHNOLOGY_STACK_SECTION**: Technology stack display with categories and icons
- **INDUSTRIES_WE_SERVE_SECTION**: Industry-specific content with 12 default categories
- **PROCESS_SECTION**: Development process steps
- **FEATURED_IN_SECTION**: Brand recognition section with media logos

## Document Format
Documents should use the new descriptive section markers:

```
[HERO_BANNER_SECTION]
Professional Web Development Services
Transform your digital presence with our expert web development solutions.

How We Help You-
●Custom web development using modern technologies
●Mobile-first, responsive design
●Performance-optimized code
[HERO_BANNER_SECTION END]

[TECHNOLOGY_STACK_SECTION]
Technology Stack for Web Development
We leverage cutting-edge technologies to build robust solutions.

Frontend Technologies:
React
Vue.js
Angular
Next.js
TypeScript

Backend Technologies:
Node.js
Python
Django
PHP
Laravel

Database:
PostgreSQL
MongoDB
MySQL
Redis

Cloud & DevOps:
AWS
Google Cloud
Docker
Kubernetes
[TECHNOLOGY_STACK_SECTION END]

[INDUSTRIES_WE_SERVE_SECTION]
[INDUSTRIES_WE_SERVE_SECTION END]

[BENEFITS_SECTION]
B2B Portal Development Services We Offer
Our comprehensive B2B portal development services help businesses streamline operations.

B2B Portal Consulting
Businesses often struggle with selecting the right technology stack for their B2B portal.

UI/UX Design
Our UX designers create intuitive, visually appealing designs to boost engagement.

Custom Development
Our team builds tailored portals that align with your unique business model.
[BENEFITS_SECTION END]

[CTA_WITH_LIST_SECTION]
Ready to Transform Your Business?
Let's discuss your project and explore digital solutions.

350+
Web Solutions Delivered

20+
Frameworks Mastered

Start Your Project View Portfolio
[CTA_WITH_LIST_SECTION END]
```

## Empty Content Handling
**KEY FEATURE**: All sections now generate professional default HTML when empty:

- **Empty sections** like `[HERO_BANNER_SECTION][HERO_BANNER_SECTION END]` automatically generate professional static content
- **Image-only sections** with just images between tags also use default HTML
- **Missing content** in any section triggers intelligent fallback content
- **Consistent branding** across all default content
- **Static HTML Images**: Uses exact same image paths as default sections to prevent broken images

## Technology Section Format
The TECHNOLOGY_STACK_SECTION supports category-based parsing:
- **Categories** end with `:` (e.g., "Frontend Technologies:")
- **Technologies** listed under each category
- **Automatic icon mapping** with fallback support
- **Multiple upload path attempts** (2023/08/, 2024/02/, etc.)
- **Proper HTML structure** matching user specifications

## Image Handling System (v3.7)
**Comprehensive image management**:
- **Global error handler** `handleImageError()` for all images
- **Static HTML Images**: BENEFITS_SECTION uses exact same image paths as default static HTML
- **Dynamic Alt Text**: Alt attributes update based on actual content titles
- **Smart placeholders** based on image type:
  - Technology icons → default-tech.svg
  - Benefits/Services → Uses static HTML images from default section
  - Client testimonials → default-client.png
  - Generic fallback → Base64 encoded SVG
- **No Broken Images**: All sections use proven static HTML image paths

## HTML Output
- **Clean Output**: No HTML comments in generated code
- **Bootstrap Compatible**: Uses Bootstrap classes for styling
- **Responsive**: Mobile-friendly layouts
- **SEO Friendly**: Proper heading structure and semantic HTML
- **Image Optimization**: All images include lazy loading and error handling
- **Professional Default Content**: Every section has meaningful fallback HTML
- **Consistent Structure**: Generated HTML matches static HTML exactly

## Recent Updates & Fixes (v3.7)

### Major Features Added:
- **Section Name Updates (v3.5)**: All sections now use descriptive names for clarity
- **BENEFITS Image Fix (v3.6-v3.7)**: Uses exact same static HTML images as default section
- **Default Static HTML**: All 14 sections generate professional content when empty
- **Broken Image Fixes**: Comprehensive image fallback system with global error handler
- **Technology Section Overhaul**: Category-based parsing with proper HTML structure
- **Empty Section Processing**: Fixed core parsing to handle all sections even when empty

### Specific Improvements:
- **HERO_BANNER_SECTION**: Complete default HTML with professional content and contact form
- **BENEFITS_SECTION**: Uses exact static HTML images, only updates alt text dynamically
- **FAQ_SECTION**: 5 comprehensive default FAQ items about web development
- **CTA_WITH_LIST_SECTION**: Professional call-to-action with statistics and dual buttons
- **TECHNOLOGY_STACK_SECTION**: Category-based parsing with proper HTML structure and icons
- **INDUSTRIES_WE_SERVE_SECTION**: 12 industry categories with proper images and links
- **PROCESS_SECTION**: 6-step development process with professional content
- **FEATURED_IN_SECTION**: 6 brand logos with proper media recognition content

### Technical Fixes:
- **parseRealDocument**: Fixed condition to process ALL sections even when empty
- **Image Error Handling**: Global `handleImageError()` function for all broken images
- **Static HTML Images**: BENEFITS section uses identical image paths as default section
- **Section Name Consistency**: All sections use descriptive `_SECTION` suffix
- **Version Management**: Updated to v3.7 with comprehensive tracking

## Development Notes
- **Descriptive Section Names**: All sections use clear, self-explanatory names
- **Smart Parsing**: Intelligently detects bullet intro titles vs regular content
- **No Manual Formatting**: Avoids manual bullet points (●) in HTML output
- **Consistent IDs**: Accordion IDs remain consistent across multiple sections
- **Static Image Strategy**: Uses proven working image paths from default HTML
- **Professional Defaults**: All empty sections generate business-appropriate content
- **Bootstrap Compatible**: Uses Bootstrap classes for responsive design
- **Category-Based Tech Parsing**: Dynamically handles technology categories ending with ':'

## Common Commands
```bash
# Start development server (recommended)
npx http-server -p 9000

# Alternative port
npx http-server -p 8001

# Kill existing processes (Windows)
taskkill //F //PID [PID_NUMBER]

# Check what's running on port
netstat -ano | findstr :9000
```

## Testing Guide

### Testing Empty Sections:
1. Create document with empty sections: `[HERO_BANNER_SECTION][HERO_BANNER_SECTION END]`
2. Upload to web IDE at `http://localhost:9000/web_ide_final.html`
3. Generate HTML Code - should show professional default content
4. All 14 section types work with empty content

### Testing New Section Names:
- Use descriptive section names like `[TECHNOLOGY_STACK_SECTION]`
- All old section names (`[HERO]`, `[FAQ]`, etc.) no longer work
- Use the test file `test_new_section_names.txt` for validation

### Testing BENEFITS Section:
- Uses exact same image paths as default static HTML
- Alt text updates dynamically based on benefit titles
- No more broken images - proven static HTML approach

## Troubleshooting
- **AI Parsing Fails**: Check Groq API key in AI Settings
- **Section Not Detected**: Ensure proper [SECTION_NAME]...[SECTION_NAME END] format using new names
- **Empty Sections Not Generating**: Check version is v3.7 or later
- **Broken Images in BENEFITS**: Fixed in v3.7 - uses static HTML images
- **Old Section Names Not Working**: Update to new descriptive names (v3.5+)
- **Technology Section Issues**: Ensure categories end with ':' (colon)
- **Server Issues**: Try different ports (8000, 8001, 9000) if port conflicts occur

## Supported Section List (New Names)
```
HERO_BANNER_SECTION, FAQ_SECTION, CTA_SIMPLE_SECTION, CTA_WITH_LIST_SECTION, 
TECHNOLOGY_STACK_SECTION, INDUSTRIES_WE_SERVE_SECTION, SERVICES_GRID_SECTION, 
SERVICES_ACCORDION_SECTION, PORTFOLIO_SECTION, TESTIMONIAL_SECTION, 
BENEFITS_SECTION, BENEFITS_TWO, CONTENT_WITH_FORM_SECTION, PROCESS_SECTION, 
FEATURED_IN_SECTION
```

## Project Structure
```
page-content-update/
├── web_ide_final.html          # Main application (v3.7)
├── CLAUDE.md                   # This documentation
├── server.py                   # Python development server
├── docx_content_tool.py        # Document processing backend
├── package.json                # Node.js dependencies
├── package-lock.json           # Dependency lock file
├── run_ide.sh                  # Server startup script
└── sections/                    # Extracted section generation functions
  ├── faq/faq.js
  ├── cta_simple/cta_simple.js
  ├── cta_with_list/cta_with_list.js
  ├── technology_stack/technology_stack.js
  ├── industries_we_serve/industries_we_serve.js
  ├── services_grid/services_grid.js
  ├── services_accordion/services_accordion.js
  ├── portfolio/portfolio.js
  ├── testimonial/testimonial.js
  ├── benefits/benefits.js
  ├── benefits_two/benefits_two.js
  ├── content_with_form/content_with_form.js
  ├── process/process.js
  ├── featured_in/featured_in.js
  └── hero_banner/hero_banner.js
```

## Version History
- **v3.7**: BENEFITS section uses exact static HTML images, only updates alt text
- **v3.6**: Broken image fixes with global error handler  
- **v3.5**: All section names updated to descriptive format
- **v3.4**: Comprehensive image fallback system
- **v3.3**: Technology section format fixes and category parsing
- **v3.2**: All sections default HTML implementation  
- **v3.1**: Core parsing fixes for empty sections
- **v3.0**: Major refactor with comprehensive section support

## Migration Guide (v3.5+)
If upgrading from older versions, update your document section names:

| **Old Name** | **New Name** |
|-------------|--------------|
| `[HERO]` | `[HERO_BANNER_SECTION]` |
| `[FAQ]` | `[FAQ_SECTION]` |
| `[CTA_TWO]` | `[CTA_WITH_LIST_SECTION]` |
| `[TECHNOLOGY]` | `[TECHNOLOGY_STACK_SECTION]` |
| `[INDUSTRIES]` | `[INDUSTRIES_WE_SERVE_SECTION]` |
| `[BENEFITS]` | `[BENEFITS_SECTION]` |
| `[CONTENT_FORM]` | `[CONTENT_WITH_FORM_SECTION]` |
| And all others... | Add `_SECTION` suffix |

## AI Configuration
- **Provider**: Groq (free tier)
- **Model**: llama-3.1-70b-versatile
- **Fallback**: Rule-based parsing when AI fails
- **API Key**: Stored in localStorage
- **Smart Processing**: Handles empty sections with professional defaults

## Current Status
- **Version**: v3.7 "BENEFITS EXACT STATIC HTML"
- **Status**: Production ready
- **Server**: Running on port 9000
- **All Features**: Fully functional with comprehensive image handling
- **Section Names**: Updated to descriptive format
- **Image Issues**: Resolved using static HTML approach