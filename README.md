# Document to HTML Converter

🚀 A powerful web-based IDE for converting structured documents into professional HTML sections with AI-powered content parsing.

## ✨ Features

- **📄 Document Processing**: Convert documents with `[SECTION_NAME]...[SECTION_NAME END]` markers
- **🤖 AI Integration**: Uses Groq API for intelligent content parsing with rule-based fallback
- **🎨 Professional Templates**: 14 different section types with Bootstrap styling
- **📱 Responsive Design**: Mobile-first, responsive HTML output
- **🖼️ Smart Image Handling**: Comprehensive broken image fallback system
- **⚡ Live Preview**: Real-time HTML preview with professional styling
- **📊 Technology Stack Parsing**: Advanced category-based technology parsing
- **🔄 Default Content**: All sections generate professional content when empty

## 🛠️ Supported Section Types (14 Total)

- **HERO_BANNER_SECTION**: Landing sections with contact forms
- **FAQ_SECTION**: Expandable FAQ accordions
- **CTA_SIMPLE_SECTION & CTA_WITH_LIST_SECTION**: Call-to-action sections
- **SERVICES_GRID_SECTION & SERVICES_ACCORDION_SECTION**: Service displays
- **BENEFITS_SECTION & BENEFITS_TWO**: Benefits listings
- **TECHNOLOGY_STACK_SECTION**: Technology showcase with icons
- **PORTFOLIO_SECTION**: Project portfolios
- **TESTIMONIAL_SECTION**: Customer testimonials
- **INDUSTRIES_WE_SERVE_SECTION**: Industry-specific content
- **PROCESS_SECTION**: Development process steps
- **CONTENT_WITH_FORM_SECTION**: Custom contact forms
- **FEATURED_IN_SECTION**: Brand recognition sections

## 🚀 Quick Start

### Online Demo
Access the live version: [Document to HTML Converter](https://your-vercel-app.vercel.app)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/document-to-html-converter.git
   cd document-to-html-converter
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   # Option 1: HTTP Server (Recommended)
   npx http-server -p 9000
   
   # Option 2: Alternative port
   npx http-server -p 8001
   ```

4. **Open the application**
   Navigate to `http://localhost:9000/web_ide_final.html`

## 📝 Document Format

Use descriptive section markers in your documents:

```text
[HERO_BANNER_SECTION]
Professional Web Development Services
Transform your digital presence with our expert solutions.

How We Help You-
●Custom web development using modern technologies
●Mobile-first, responsive design
●Performance-optimized code
[HERO_BANNER_SECTION END]

[TECHNOLOGY_STACK_SECTION]
Our Technology Stack
We use cutting-edge technologies for robust solutions.

Frontend Technologies:
React
Vue.js
Angular

Backend Technologies:
Node.js
Python
Django
[TECHNOLOGY_STACK_SECTION END]

[BENEFITS_SECTION]
Our Services
Comprehensive development services for your business.

Consulting Services
Expert guidance for technology decisions.

UI/UX Design
Intuitive designs that boost engagement.
[BENEFITS_SECTION END]
```

## 🤖 AI Configuration

1. **Get a Groq API Key**: Sign up at [Groq](https://groq.com)
2. **Configure in App**: Click "AI Settings" and enter your API key
3. **Model**: Uses `llama-3.1-70b-versatile` (free tier available)
4. **Fallback**: Automatic rule-based parsing when AI is unavailable

## 🎯 Key Features

### Smart Empty Section Handling
- Empty sections automatically generate professional default content
- Image-only sections use static HTML fallbacks
- Consistent branding across all default content

### Advanced Technology Parsing
- Category-based parsing ("Frontend Technologies:", "Backend:", etc.)
- Automatic icon mapping with fallback support
- Professional HTML structure matching specifications

### Comprehensive Image System
- Global error handler for broken images
- Smart placeholders based on content type
- Static HTML images for maximum reliability
- Lazy loading and SEO optimization

## 📁 Project Structure

```
document-to-html-converter/
├── web_ide_final.html          # Main application (v3.7)
├── README.md                   # This file
├── CLAUDE.md                   # Detailed documentation
├── package.json                # Node.js dependencies
├── package-lock.json           # Node.js dependency lock file
└── vercel.json                 # Vercel deployment configuration
```

## 🌐 Deployment

### Vercel (Recommended)
1. Connect your GitHub repository to Vercel
2. Configure build settings:
   - **Build Command**: `npm install`
   - **Output Directory**: `./`
   - **Install Command**: `npm install`
3. Deploy automatically on every push

### Netlify
1. Connect repository to Netlify
2. Set publish directory to root (`./`)
3. Deploy with drag-and-drop or Git integration

### GitHub Pages
1. Enable GitHub Pages in repository settings
2. Select source branch (usually `main`)
3. Access via `https://yourusername.github.io/repository-name/web_ide_final.html`

## 🔄 Version History

- **v3.7**: BENEFITS section uses exact static HTML images
- **v3.6**: Comprehensive broken image fixes
- **v3.5**: Updated to descriptive section names
- **v3.4**: Enhanced image fallback system
- **v3.3**: Technology section improvements
- **v3.2**: Default HTML for all sections
- **v3.1**: Core parsing fixes
- **v3.0**: Major refactor with full section support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: Check `CLAUDE.md` for detailed instructions
- **Issues**: Report bugs via GitHub Issues
- **Questions**: Start a GitHub Discussion

## 🙏 Acknowledgments

- Bootstrap for responsive styling
- Groq for AI-powered parsing
- Font Awesome for icons
- All contributors and testers

---

**Made with ❤️ for developers who need fast, professional HTML generation from structured documents.**