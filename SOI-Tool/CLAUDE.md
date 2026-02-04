# Document to HTML Converter Project

## Project Overview
This project contains a web-based IDE for converting structured documents with section markers into HTML code. The main tool processes documents with `[SECTION_NAME]...[SECTION_NAME END]` markers and generates corresponding HTML sections with intelligent fallback content and comprehensive image handling.

## Key Files
- `web_ide_final.html` - Main web IDE with AI-powered content parsing (v3.9.1)
- `CLAUDE.md` - Project documentation and instructions
- `package.json` & `package-lock.json` - Node.js dependencies
- `vercel.json` - Deployment configuration

## Main Features
- **Document Processing**: Converts documents with descriptive section markers
- **AI Integration**: Uses Groq API for intelligent content parsing (fallback to rule-based parsing)
- **Default Content Generation**: All sections generate professional static HTML when content is empty
- **Multiple Section Types**: Supports 19 different section types with smart parsing
- **File Upload**: Supports both Word documents (.docx) and text files
- **Live Preview**: Real-time HTML preview with Bootstrap styling
- **Image Fallback System**: Comprehensive broken image handling with static HTML images
- **Technology Stack Parsing**: Advanced category-based technology parsing
- **Descriptive Section Names**: All sections use clear, descriptive naming conventions

## Section Types Supported (19 Total)

### Updated Section Names (v3.5+):
- **HERO_BANNER_SECTION**: Main landing section with title, description, bullet points, and contact form
- **FAQ_SECTION**: Frequently asked questions with expandable accordion answers
- **CTA_SIMPLE_SECTION**: Simple call-to-action sections with buttons
- **CTA_WITH_LIST_SECTION**: Advanced CTA with statistics and dual buttons
- **SERVICES_GRID_SECTION**: Grid layout of services with images and descriptions
- **SERVICES_GRID_SECTION_CENTER**: Centered grid layout for services
- **SERVICES_ACCORDION_SECTION**: Collapsible accordion for services (single/multiple sections)
- **CONTENT_WITH_FORM_SECTION**: Contact forms with customizable fields
- **PORTFOLIO_SECTION**: Project showcase with technology stacks
- **TESTIMONIAL_SECTION**: Customer testimonials with author attribution
- **TECHNOLOGY_STACK_SECTION**: Technology stack display with categories and icons (supports pipe and colon formats)
- **INDUSTRIES_WE_SERVE_SECTION**: Industry-specific content with 12 default categories
- **PROCESS_SECTION**: Development process steps
- **FEATURED_IN_SECTION**: Brand recognition section with media logos
- **FLEXIBLE_PACKAGE_SECTION**: Pricing packages with features, costs, and call-to-action buttons
- **WHY_CHOOSE_BOX**: Why choose us section with key benefits
- **GUARANTEED_SECTION**: Company differentiators and guarantees section
- **AWARDS_SECTION**: Awards and recognition showcase section
- **FLEXIBLE_PACKAGES_WRAPPER**: Alternative pricing packages layout with three-tier structure
- **TESTIMONIAL_SECTION_CLUTCH**: Clutch-style testimonials with project summaries

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

[FLEXIBLE_PACKAGE_SECTION]
Our Flexible Packages for Mobile App Maintenance Services
Space-O Technologies offers three flexible mobile app maintenance packages to suit businesses of all sizes.

Package: Standard
Basic Maintenance for Smooth Performance
Price: $999
- 35–40 Hours
- iOS, Android
- Swift, Kotlin, React Native, and Flutter
- Dedicated Project Manager
- Manual and Automated QA
- Email Communication

Package: Advanced
Enhanced Support for Growing Mobile Apps
Price: $1499
- 65–70 Hours
- iOS, Android
- Swift, Kotlin, React Native, and Flutter
- Dedicated Project Manager
- Manual and Automated QA
- Skype, Zoom, and WhatsApp Support
- Best for Advanced App Change Requests

Package: Pro
Premium Support with Feature Expansion
Price: $2499
- 100–120 Hours
- iOS, Android
- Swift, Kotlin, React Native, and Flutter
- Dedicated Project Manager
- Manual and Automated QA
- Skype, Zoom, WhatsApp, and Phone Support
- Ideal for Continuous Maintenance and New Feature Development
[FLEXIBLE_PACKAGE_SECTION END]
```

## Empty Content Handling
**KEY FEATURE**: All sections now generate professional default HTML when empty:

- **Empty sections** like `[HERO_BANNER_SECTION][HERO_BANNER_SECTION END]` automatically generate professional static content
- **Image-only sections** with just images between tags also use default HTML
- **Missing content** in any section triggers intelligent fallback content
- **Consistent branding** across all default content
- **Static HTML Images**: Uses exact same image paths as default sections to prevent broken images

## Technology Section Format (Enhanced v3.8)
The TECHNOLOGY_STACK_SECTION supports **two parsing formats** for maximum flexibility:

### **Format 1: Pipe-Separated (Table Format)**
```
Front-End Programming | JavaScript | Angular | React | Vue.js | CSS | HTML
Back-End Programming | Java | Python | .Net | Node.js | Go | PHP | Ruby on Rails
Mobile App Technologies | Kotlin | Swift | C++ | Flutter | Xamarin | Ionic | React Native
Database Management | PostgreSQL | MySQL | MongoDB | Redis
```

### **Format 2: Colon-Separated (List Format)**  
```
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
```

### **Key Features:**
- **Left Column**: Category names display in `technology-name` div
- **Right Column**: Each technology gets separate `<li>` element in `technology-icon-wrapper`
- **Automatic icon mapping** with React.svg fallback for all technologies
- **Enhanced debugging** with comprehensive console logging
- **Flexible parsing** handles both formats seamlessly
- **Dynamic alt text** updates based on technology names

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

## Recent Updates & Fixes (v3.9)

### Latest Features (v3.9):
- **FLEXIBLE_PACKAGE_SECTION**: New pricing packages section with three-card layout
- **Package Parsing**: Dynamic parsing of package names, descriptions, prices, and features
- **Responsive Pricing Cards**: Mobile-optimized pricing layout with hover effects
- **Most Popular Badge**: Automatic "Most Popular" badge for advanced packages
- **Feature Lists**: Bullet-point features with check mark icons
- **Call-to-Action Buttons**: Get Started buttons with hover animations

### Major Features (v3.8):
- **TECHNOLOGY_STACK_SECTION Enhancement**: Complete rewrite with dual format support
- **Pipe Format Support**: Category | Tech1 | Tech2 | Tech3 table format parsing
- **Colon Format Support**: Category: followed by technology list format
- **Enhanced HTML Structure**: Proper left/right column separation with technology-name and technology-icon-wrapper
- **Advanced Debugging**: Comprehensive console logging for troubleshooting
- **Individual Technology Elements**: Each tech gets separate <li> element for better styling

### Major Features Added (v3.5-v3.7):
- **Section Name Updates (v3.5)**: All sections now use descriptive names for clarity
- **BENEFITS Image Fix (v3.6-v3.7)**: Uses exact same static HTML images as default section
- **Default Static HTML**: All 14 sections generate professional content when empty
- **Broken Image Fixes**: Comprehensive image fallback system with global error handler
- **Empty Section Processing**: Fixed core parsing to handle all sections even when empty

### Specific Improvements:
- **HERO_BANNER_SECTION**: Complete default HTML with professional content and contact form
- **BENEFITS_SECTION**: Uses exact static HTML images, only updates alt text dynamically
- **FAQ_SECTION**: 5 comprehensive default FAQ items about web development
- **CTA_WITH_LIST_SECTION**: Professional call-to-action with statistics and dual buttons
- **TECHNOLOGY_STACK_SECTION**: Dual-format parsing (pipe/colon) with proper HTML structure, individual tech elements, and enhanced debugging
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
- **Word Comment Markers in Output**: Fixed in v3.9.1 - comment markers like [a], [b], [c], [1], [2] are now automatically filtered out
- **Empty Sections Not Generating**: Check version is v3.7 or later
- **Broken Images in BENEFITS**: Fixed in v3.7 - uses static HTML images
- **Old Section Names Not Working**: Update to new descriptive names (v3.5+)
- **Technology Section Issues**: Ensure categories end with ':' (colon)
- **Server Issues**: Try different ports (8000, 8001, 9000) if port conflicts occur

## Supported Section List (All 19 Sections)
```
HERO_BANNER_SECTION, FAQ_SECTION, CTA_SIMPLE_SECTION, CTA_WITH_LIST_SECTION,
TECHNOLOGY_STACK_SECTION, INDUSTRIES_WE_SERVE_SECTION, SERVICES_GRID_SECTION,
SERVICES_GRID_SECTION_CENTER, SERVICES_ACCORDION_SECTION, PORTFOLIO_SECTION,
TESTIMONIAL_SECTION, CONTENT_WITH_FORM_SECTION, PROCESS_SECTION, FEATURED_IN_SECTION,
FLEXIBLE_PACKAGE_SECTION, WHY_CHOOSE_BOX, GUARANTEED_SECTION, AWARDS_SECTION,
FLEXIBLE_PACKAGES_WRAPPER, TESTIMONIAL_SECTION_CLUTCH
```

## Project Structure
```
Doc-to-HTML/
├── web_ide_final.html          # Main application (v3.9.1) - All-in-one HTML file with embedded JavaScript
├── CLAUDE.md                   # Project documentation and instructions
├── README.md                   # User-facing documentation with quick start guide
├── package.json                # Node.js dependencies and scripts
├── package-lock.json           # Dependency lock file
├── vercel.json                 # Vercel deployment configuration
├── test_hero_with_links.txt    # Test file for hero section with hyperlinks
└── test_multiple_paragraphs.txt # Test file for multiple paragraph parsing
```

**Note**: This is a monolithic architecture where all parsing logic, section generators, and UI code are embedded within the single `web_ide_final.html` file (6850+ lines). All 18 section types are implemented as methods within the `RealDocumentProcessor` class.

## Version History
- **v3.9.1 (Current)**: Bug fix for Word document comment markers
  - **Critical Fix**: Removed Word document comment markers ([a], [b], [c], [1], [2], etc.) from HTML output
  - Added regex filtering to strip lowercase letter and numeric comment markers during .docx parsing
  - Enhanced convertHtmlToTextWithLinks function with comment marker cleanup
- **v3.9**: Major updates and critical bug fixes
  - Added TESTIMONIAL_SECTION_CLUTCH with Clutch-style testimonials, slider functionality, and ratings
  - Added FLEXIBLE_PACKAGES_WRAPPER section with 3-tier pricing card layout
  - **Critical Fix**: Fixed FLEXIBLE_PACKAGES_WRAPPER parser preventing false "Pro" detection in feature text
  - **Critical Fix**: Fixed copy button errors with clipboard API fallback support
  - Added FLEXIBLE_PACKAGES_WRAPPER CSS to sectionCssMap for proper CSS generation
  - Optimized TESTIMONIAL_SECTION_CLUTCH CSS (consolidated media queries, 61% size reduction)
  - Created comprehensive content writer templates (FLEXIBLE_PACKAGES_WRAPPER_TEMPLATE.md, FLEXIBLE_PACKAGES_TEMPLATE_FOR_WORD.txt)
  - Fixed section routing order to prioritize TESTIMONIAL_SECTION_CLUTCH over TESTIMONIAL_SECTION
  - Escaped closing script tags in embedded JavaScript to prevent parser errors
  - All 19 section types now fully functional with proper HTML, CSS, and JavaScript generation
- **v3.8**: TECHNOLOGY_STACK_SECTION enhanced with dual-format parsing (pipe/colon), individual tech elements, advanced debugging
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
- **Version**: v3.9.1 "WORD COMMENT CLEANUP FIX"
- **Status**: Production ready - All 19 sections fully functional
- **Server**: Running on port 8000, 8001, or 9000
- **Latest Fixes**:
  - ✅ Word document comment markers ([a], [b], [c], [1], [2]) now filtered out from HTML output
  - ✅ FLEXIBLE_PACKAGES_WRAPPER parser bug fixed (no more false "Pro" detection)
  - ✅ Copy button clipboard API issues resolved with fallback support
  - ✅ TESTIMONIAL_SECTION_CLUTCH fully integrated with optimized CSS
  - ✅ All 19 sections generate proper HTML and CSS
- **Section Names**: All use descriptive format (e.g., HERO_BANNER_SECTION)
- **Technology Parsing**: Dual-format support (pipe-separated and colon-separated)
- **Pricing Sections**: Both FLEXIBLE_PACKAGE_SECTION and FLEXIBLE_PACKAGES_WRAPPER working
- **Image Handling**: Global error handler with automatic fallbacks
- **Content Templates**: Comprehensive templates for content writers available