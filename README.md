# 📄 Document to HTML Converter

> **A powerful web-based IDE that converts structured documents with section markers into professional, responsive HTML code with CSS styling.**

[![Version](https://img.shields.io/badge/version-3.9-blue.svg)](https://github.com/upendranathdubey92/Doc-to-HTML)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-production-success.svg)](https://github.com/upendranathdubey92/Doc-to-HTML)

---

## 🎯 What is This Tool?

The **Document to HTML Converter** is an all-in-one web application that transforms structured Word documents or text files into production-ready HTML sections with professional styling. Perfect for:

- 🎨 **Marketing Teams** - Quickly convert content briefs into landing page HTML
- 💻 **Developers** - Generate boilerplate HTML/CSS from specifications
- ✍️ **Content Writers** - See content transformed into styled web sections instantly
- 🏢 **Agencies** - Speed up client deliverables with automated HTML generation

### Key Capabilities

- ✅ Upload `.doc`, `.docx`, or `.txt` files
- ✅ Parse 19 different section types automatically
- ✅ Generate clean, Bootstrap-compatible HTML
- ✅ Export matching CSS with responsive breakpoints
- ✅ Live preview with professional styling
- ✅ AI-powered parsing with rule-based fallback
- ✅ One-click copy to clipboard
- ✅ Download as HTML files

---

## 🚀 How It Works

### Simple 4-Step Process

```
📄 Upload Document → 🔍 Parse Sections → ✨ Generate HTML/CSS → 📋 Copy & Use
```

#### Step 1: Prepare Your Document
Add section markers to your Word document or text file:

```text
[HERO_BANNER_SECTION]
Your content here...
[HERO_BANNER_SECTION END]

[SERVICES_GRID_SECTION]
Your services content...
[SERVICES_GRID_SECTION END]
```

#### Step 2: Upload to the Tool
- Open `web_ide_final.html` in your browser
- Drag & drop your document or click "Upload Document"
- The tool automatically detects all sections

#### Step 3: Generate HTML & CSS
- Click **"Generate HTML Code"** - Get complete HTML output
- Click **"Generate CSS Code"** - Get all necessary CSS styles
- Preview the result in the live preview pane

#### Step 4: Copy & Deploy
- Click the **copy button** to copy HTML/CSS
- Paste into your website or CMS
- All styling and responsiveness included!

---

## 📦 Supported Section Types

The tool supports **19 different section types** covering all common website needs:

### 🎨 Hero & CTA Sections (3)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `HERO_BANNER_SECTION` | Main landing banner with contact form | Homepage hero sections |
| `CTA_SIMPLE_SECTION` | Simple call-to-action with button | Mid-page conversions |
| `CTA_WITH_LIST_SECTION` | CTA with statistics and dual buttons | Feature-rich CTAs |

### 🛠️ Service Sections (3)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `SERVICES_GRID_SECTION` | Grid layout of services with images | Services overview |
| `SERVICES_GRID_SECTION_CENTER` | Centered grid for services | Focused service display |
| `SERVICES_ACCORDION_SECTION` | Collapsible service accordion | Long service lists |

### 💼 Business Sections (5)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `PORTFOLIO_SECTION` | Project showcase with tech stacks | Case studies |
| `TESTIMONIAL_SECTION` | Customer testimonials with photos | Social proof |
| `TESTIMONIAL_SECTION_CLUTCH` | Clutch-style testimonials with ratings | B2B testimonials |
| `PROCESS_SECTION` | Step-by-step process display | How it works |
| `INDUSTRIES_WE_SERVE_SECTION` | Industry-specific content grid | Target markets |

### 💻 Technical Sections (2)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `TECHNOLOGY_STACK_SECTION` | Tech stack with icons and categories | Technology showcase |
| `WHY_CHOOSE_BOX` | Benefits with icons | Unique value props |

### 💰 Pricing & Features (2)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `FLEXIBLE_PACKAGE_SECTION` | Single pricing card layout | Simple pricing |
| `FLEXIBLE_PACKAGES_WRAPPER` | 3-tier pricing cards layout | Compare plans |

### 📋 Information Sections (4)
| Section Type | Description | Use Case |
|-------------|-------------|----------|
| `FAQ_SECTION` | Expandable FAQ accordion | Common questions |
| `CONTENT_WITH_FORM_SECTION` | Contact form with content | Lead generation |
| `FEATURED_IN_SECTION` | Brand logos and media mentions | Credibility |
| `AWARDS_SECTION` | Awards and recognition showcase | Achievements |
| `GUARANTEED_SECTION` | Company differentiators | Trust builders |

---

## 📝 Document Format Examples

### Example 1: Hero Banner Section

```text
[HERO_BANNER_SECTION]
Professional Web Development Services
Transform your digital presence with our expert web development solutions tailored to your business needs.

How We Help You-
●Custom web development using modern technologies
●Mobile-first, responsive design
●Performance-optimized code
●Dedicated support and maintenance
[HERO_BANNER_SECTION END]
```

**Output:** Full hero section with heading, description, bullet points, rating badges, and contact form.

---

### Example 2: Pricing Packages (3-Tier Layout)

```text
[FLEXIBLE_PACKAGES_WRAPPER]
Our Flexible Packages for Mobile App Maintenance Services
Choose the package that best fits your business needs and budget.

Package: Standard
Basic Maintenance for Smooth Performance
Price: $999
- 35–40 Hours
- iOS, Android
- Swift, Kotlin, React Native
- Dedicated Project Manager
- Email Communication

Package: Advanced
Enhanced Support for Growing Mobile Apps
Price: $1499
- 65–70 Hours
- iOS, Android
- Swift, Kotlin, React Native, and Flutter
- Dedicated Project Manager
- Skype, Zoom, and WhatsApp Support

Package: Pro
Premium Support with Feature Expansion
Price: $2499
- 100–120 Hours
- iOS, Android
- Swift, Kotlin, React Native, and Flutter
- Dedicated Project Manager
- 24/7 Priority Support
[FLEXIBLE_PACKAGES_WRAPPER END]
```

**Output:** 3 pricing cards side-by-side with "Most Popular" badge on Advanced package, hover effects, and responsive design.

---

### Example 3: Technology Stack

```text
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
[TECHNOLOGY_STACK_SECTION END]
```

**Output:** Professional tech stack display with icons, categories, and responsive grid layout.

---

## 🎨 Key Features

### ✨ Smart Content Parsing

- **AI-Powered**: Uses Groq API (llama-3.1-70b-versatile) for intelligent content extraction
- **Rule-Based Fallback**: Automatic fallback when AI is unavailable
- **Empty Section Handling**: Generates professional default content for empty sections
- **Multi-Format Support**: Handles pipe-separated tables and list formats

### 🎯 Professional Output

- **Bootstrap Compatible**: Uses Bootstrap 4/5 classes for styling
- **Responsive Design**: Mobile-first with breakpoints for all screen sizes
- **SEO Friendly**: Proper heading structure and semantic HTML
- **Clean Code**: No HTML comments, properly indented, production-ready

### 🖼️ Advanced Image Handling

- **Global Error Handler**: Automatic fallback for broken images
- **Smart Placeholders**: Context-aware placeholder images
- **Lazy Loading**: Optimized image loading for performance
- **Dynamic Alt Text**: Automatically updates based on content

### 📱 Responsive Breakpoints

All generated CSS includes responsive breakpoints:
- `576px` - Small devices (phones)
- `768px` - Medium devices (tablets)
- `992px` - Large devices (desktops)
- `1200px` - Extra large devices
- `1400px` - 2X large devices

### 🎛️ User-Friendly Interface

- **Drag & Drop Upload**: Easy file upload interface
- **Live Preview**: See results in real-time
- **One-Click Copy**: Copy HTML and CSS to clipboard instantly
- **Download Option**: Save as HTML file
- **Error Handling**: Clear feedback for parsing issues

---

## 🚀 Quick Start Guide

### Option 1: Local Development (Recommended)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/upendranathdubey92/Doc-to-HTML.git
   cd Doc-to-HTML
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Start Local Server**
   ```bash
   # Using http-server (recommended)
   npx http-server -p 9000

   # Or use alternative port
   npx http-server -p 8001
   ```

4. **Open the Application**
   ```
   http://localhost:9000/web_ide_final.html
   ```

### Option 2: Direct File Access

Simply open `web_ide_final.html` in any modern web browser (Chrome, Firefox, Edge, Safari).

⚠️ **Note:** Some features require a local server due to browser security restrictions.

---

## 🔧 Configuration

### AI Settings (Optional)

1. Click **"AI Settings"** button in the interface
2. Enter your Groq API key (get free key at [groq.com](https://groq.com))
3. The tool will use AI for smarter content parsing
4. Works perfectly without AI using rule-based parsing

### Customization

All styling and behavior is self-contained in `web_ide_final.html`. You can customize:
- CSS classes and styling (line 400-1300)
- Section templates (line 1467-1530)
- Default content (within each `generate*Section` method)
- Parsing logic (within each `parse*Section` method)

---

## 📖 Usage Examples

### For Content Writers

1. Write content in Word using section markers
2. Upload to tool
3. Review generated HTML preview
4. Copy HTML/CSS and send to developer

### For Developers

1. Receive Word doc from content team
2. Upload to tool
3. Get production-ready HTML/CSS
4. Integrate into website/CMS
5. Customize styling as needed

### For Agencies

1. Create content templates with section markers
2. Fill in client-specific content
3. Generate custom landing pages in minutes
4. Export and deploy to client sites

---

## 🛠️ Troubleshooting

### Common Issues

**Issue:** Copy button not working
- **Cause:** Browser clipboard API restrictions
- **Fix:** Tool automatically falls back to legacy copy method
- **Refresh:** Hard refresh browser (Ctrl+Shift+R)

**Issue:** Section not detected
- **Cause:** Incorrect section marker format
- **Fix:** Ensure exact format: `[SECTION_NAME]` and `[SECTION_NAME END]`
- **Check:** Section name must be one of the 19 supported types

**Issue:** Features scrambled in pricing section
- **Cause:** Parser matching partial words (e.g., "pro" in "Project")
- **Fix:** Fixed in v3.9 - update to latest version

**Issue:** Empty CSS output
- **Cause:** Section type not in CSS map
- **Fix:** All 19 sections now included in v3.9

**Issue:** Images broken
- **Cause:** Image URLs not accessible
- **Fix:** Global error handler provides automatic fallbacks

### Getting Help

- 📖 **Documentation**: See `CLAUDE.md` for detailed technical docs
- 🐛 **Bug Reports**: [Open an issue](https://github.com/upendranathdubey92/Doc-to-HTML/issues)
- 💬 **Questions**: [Start a discussion](https://github.com/upendranathdubey92/Doc-to-HTML/discussions)

---

## 📊 Version History

### v3.9 (Current - January 2026)
- ✅ Added `FLEXIBLE_PACKAGES_WRAPPER` section
- ✅ Fixed package parser (no more false "Pro" detection)
- ✅ Added comprehensive pricing card support
- ✅ Fixed copy button clipboard API issues
- ✅ Created content writer templates

### v3.8 (January 2026)
- ✅ Enhanced `TECHNOLOGY_STACK_SECTION` with dual-format parsing
- ✅ Support for pipe-separated and colon-separated formats
- ✅ Individual `<li>` elements for each technology
- ✅ Advanced debugging and console logging

### v3.7 (December 2025)
- ✅ Fixed BENEFITS section image paths
- ✅ Uses exact static HTML images
- ✅ Dynamic alt text updates

### v3.6 (December 2025)
- ✅ Global image error handler
- ✅ Comprehensive fallback system

### v3.5 (November 2025)
- ✅ Updated all sections to descriptive names
- ✅ Removed old short names (HERO → HERO_BANNER_SECTION)

### Earlier Versions
- **v3.4**: Enhanced image fallback system
- **v3.3**: Technology section format fixes
- **v3.2**: Default HTML for all sections
- **v3.1**: Core parsing fixes
- **v3.0**: Major refactor with 14 sections

---

## 📁 Project Structure

```
Doc-to-HTML/
├── web_ide_final.html              # Main application (373KB)
├── README.md                       # This file
├── CLAUDE.md                       # Technical documentation (17KB)
├── package.json                    # Node.js dependencies
├── package-lock.json               # Dependency lock file
├── vercel.json                     # Vercel deployment config
├── FLEXIBLE_PACKAGES_WRAPPER_TEMPLATE.md    # Pricing template (11KB)
└── FLEXIBLE_PACKAGES_TEMPLATE_FOR_WORD.txt  # Simple template (5.4KB)
```

### File Details

- **web_ide_final.html**: Monolithic all-in-one file with embedded CSS, JavaScript, and all parsing logic
- **CLAUDE.md**: Detailed technical documentation for developers
- **README.md**: User-facing documentation (this file)
- **Templates**: Pre-formatted examples for content writers

---

## 🌐 Deployment Options

### Deploy to Vercel (Recommended)

1. Connect repository to Vercel
2. No build configuration needed
3. Automatic deployments on push
4. Free SSL certificate included

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Deploy to Netlify

1. Drag & drop `web_ide_final.html` to Netlify
2. Or connect Git repository
3. Set publish directory to `/`

### Deploy to GitHub Pages

1. Enable Pages in repository settings
2. Select `main` branch
3. Access at: `https://username.github.io/Doc-to-HTML/web_ide_final.html`

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/upendranathdubey92/Doc-to-HTML.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Update `web_ide_final.html`
   - Test thoroughly with sample documents
   - Update documentation if needed

4. **Commit Changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push & Create PR**
   ```bash
   git push origin feature/amazing-feature
   ```

### Development Guidelines

- ✅ Test with all 19 section types
- ✅ Ensure responsive design works
- ✅ Check browser compatibility (Chrome, Firefox, Safari, Edge)
- ✅ Update version number in comments
- ✅ Add to version history in CLAUDE.md

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Upendra Nath Dubey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Bootstrap** - Responsive CSS framework
- **Groq** - AI-powered content parsing
- **Font Awesome** - Professional icon library
- **Quill** - Rich text editor integration
- **All Contributors** - Thank you for making this tool better!

---

## 📞 Support & Contact

- 📧 **Email**: [Insert your email]
- 🐙 **GitHub**: [@upendranathdubey92](https://github.com/upendranathdubey92)
- 💼 **LinkedIn**: [Insert LinkedIn URL]
- 🌐 **Website**: [Insert website URL]

---

## 🎯 Use Cases

### 1. Marketing Landing Pages
Convert marketing briefs into HTML landing pages with hero sections, CTAs, testimonials, and pricing tables.

### 2. Documentation Sites
Generate service pages, FAQ sections, and technology stack displays from simple text documents.

### 3. Agency Deliverables
Speed up client deliverables by converting content documents into production-ready HTML.

### 4. Internal Tools
Convert internal specifications into styled HTML sections for internal dashboards and tools.

### 5. E-commerce
Create product features, pricing tables, and customer testimonials from product specs.

---

## 🚀 Roadmap

### Planned Features

- [ ] More section types (Blog posts, Team members, Case studies)
- [ ] Custom CSS theme builder
- [ ] Export as React/Vue components
- [ ] Bulk document processing
- [ ] API endpoint for programmatic access
- [ ] WordPress plugin version
- [ ] Figma/Sketch import
- [ ] Multi-language support

---

## ⭐ Star History

If you find this tool useful, please consider giving it a star on GitHub! ⭐

---

## 📈 Statistics

- **Version**: 3.9
- **Total Sections**: 19
- **File Size**: 373KB (all-in-one)
- **Lines of Code**: ~7,800
- **Browser Support**: Chrome, Firefox, Safari, Edge
- **Dependencies**: Zero runtime dependencies (self-contained)

---

<div align="center">

**Made with ❤️ by developers, for developers**

[⬆ Back to Top](#-document-to-html-converter)

</div>
