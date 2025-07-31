# Document to HTML Converter Project

## Project Overview
This project contains a web-based IDE for converting structured documents with section markers into HTML code. The main tool processes documents with `[SECTION]...[SECTION END]` markers and generates corresponding HTML sections.

## Key Files
- `web_ide_final.html` - Main web IDE with AI-powered content parsing
- `web_ide_simple.html` - Simplified version for basic parsing
- `docx_content_tool.py` - Python backend for document processing
- `server.py` - Local development server

## Main Features
- **Document Processing**: Converts documents with section markers like `[HERO]...[HERO END]`
- **AI Integration**: Uses Groq API for intelligent content parsing (fallback to rule-based parsing)
- **Multiple Section Types**: Supports 15 different section types with smart parsing
- **File Upload**: Supports both Word documents (.docx) and text files
- **Live Preview**: Real-time HTML preview with Bootstrap styling
- **QA Testing**: Comprehensive test suite with 44+ tests for reliability

## Section Types Supported (15 Total)
- **HERO**: Main landing section with title, description, optional bullet intro titles, and contact form
- **FAQ**: Frequently asked questions with expandable answers
- **CTA_SIMPLE**: Simple call-to-action sections with buttons
- **CTA_TWO**: Advanced CTA with statistics and dual buttons
- **SERVICES_GRID**: Grid layout of services with images and descriptions
- **SERVICES_ACCORDION**: Collapsible accordion for services (supports single/multiple sections)
- **BENEFITS_TWO**: Benefits section with title/description pairs
- **CONTENT_FORM**: Contact forms with customizable fields
- **PORTFOLIO**: Project showcase with technology stacks
- **TESTIMONIAL**: Customer testimonials with author attribution
- **TECHNOLOGY**: Technology stack display
- **PROCESS**: Step-by-step process descriptions
- **INDUSTRIES**: Industry-specific content
- **CTA_ENHANCED**: Enhanced call-to-action variants
- **BENEFITS**: Standard benefits listing

## Document Format
Documents should use section markers:
```
[HERO]
Web Development Services
Join 100+ brands who trust Space-O Technologies to power their digital presence.

How We Help You-
●Custom web development using modern technologies
●Mobile-first, responsive design
●Performance-optimized code

[HERO END]

[CTA_TWO]
Ready to Build a Web Solution?
Whether you're a startup or enterprise, we offer customized services.

350+
Web Solutions Delivered

20+
Frameworks Mastered

Request Proposal View Portfolio
[CTA_TWO END]

[BENEFITS_TWO]
Why Choose Our Services
Professional web development with proven results

Expertise
Over 15 years of experience in web development

Quality
High-quality, tested solutions that meet standards
[BENEFITS_TWO END]
```

## Accordion Behavior
- **3 or fewer items**: Single accordion section
- **More than 3 items**: Multiple sections with alternating column layouts
- **IDs**: Uses consistent `one`, `two`, `three` across all sections
- **Active State**: First item is active/open by default
- **Images**: All images have `loading="lazy" decoding="async"` attributes

## AI Configuration
- **Provider**: Groq (free tier)
- **Model**: llama-3.1-70b-versatile
- **Fallback**: Rule-based parsing when AI fails
- **API Key**: Stored in localStorage

## HTML Output
- **Clean Output**: No HTML comments in generated code
- **Bootstrap Compatible**: Uses Bootstrap classes for styling
- **Responsive**: Mobile-friendly layouts
- **SEO Friendly**: Proper heading structure and semantic HTML

## Recent Updates & Fixes
- **HERO Section**: Smart bullet intro title detection (e.g., "How We Help You-")
- **BENEFITS_TWO**: Changed from BENEFITS2 for better regex compatibility
- **CTA_TWO**: New advanced CTA section with statistics and dual buttons
- **CONTENT_FORM**: Contact form section with customizable fields
- **Section Priority**: Fixed CTA_TWO vs CTA detection order
- **END Marker Filtering**: Improved section detection accuracy

## Development Notes
- **Smart Parsing**: Intelligently detects bullet intro titles vs regular content
- **No Manual Formatting**: Avoids manual bullet points (●) in HTML output
- **Consistent IDs**: Accordion IDs remain consistent across multiple sections
- **Image Optimization**: All images include lazy loading attributes
- **Clean HTML**: No HTML comments in generated output
- **Bootstrap Compatible**: Uses Bootstrap classes for responsive design

## Testing & QA
Comprehensive test suite available:
- `qa_unit_tests.html` - Section detection tests (15 sections)
- `qa_html_generation_tests.html` - HTML output validation
- `qa_edge_cases_tests.html` - Error handling & edge cases (13 tests)
- `qa_regression_tests.html` - No breaking changes verification
- `qa_test_master.html` - Master dashboard for all tests

## Common Commands
```bash
# Start development server
python server.py

# Alternative server on port 8001  
python -m http.server 8001

# Run Python tool directly
python3 docx_content_tool.py your_document.txt

# Test specific sections
python3 docx_content_tool.py test_hero_bullet_intro.txt
```

## Troubleshooting
- **AI Parsing Fails**: Check Groq API key in AI Settings
- **Section Not Detected**: Ensure proper [SECTION]...[SECTION END] format
- **BENEFITS2 Not Working**: Use BENEFITS_TWO instead
- **CTA vs CTA_TWO**: System automatically prioritizes CTA_TWO
- **Images Not Loading**: Check image paths (uses WordPress-style paths)
- **Bullet Intro Missing**: Ensure line before bullets ends with dash/colon or is under 50 chars

## Supported Section List
```
HERO, FAQ, CTA_SIMPLE, CTA_ENHANCED, CTA_TWO, PROCESS, TECHNOLOGY, 
INDUSTRIES, SERVICES_GRID, SERVICES_ACCORDION, PORTFOLIO, TESTIMONIAL, 
BENEFITS, BENEFITS_TWO, CONTENT_FORM
```