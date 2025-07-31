# 🌐 Page Content Update Web IDE

A browser-based IDE for processing document files and generating HTML sections automatically.

## 🚀 Quick Start

### Method 1: Launch with Python Server
```bash
python3 launch_ide.py
```
This will automatically:
- Start a local web server
- Open your browser to the IDE
- Display the interface ready to use

### Method 2: Manual Launch
```bash
python3 -m http.server 8000
```
Then open: `http://localhost:8000/web_ide.html`

## ✨ Features

### 📁 File Upload
- **Drag & Drop**: Drop .txt, .doc, .docx files directly
- **File Browser**: Click to browse and select files
- **File Info**: Shows file name, size, and type
- **Content Preview**: Automatically loads content into editor

### 🛠️ Content Processing
- **6 Section Types**: Hero, FAQ, CTA, Process, Technology, Industries
- **Selective Generation**: Choose which sections to generate
- **Real-time Processing**: Instant HTML generation
- **Error Handling**: Clear validation and error messages

### 💻 Code Editor Interface
- **VS Code Style**: Dark theme with syntax highlighting
- **Split Panes**: Input content on left, generated HTML on right
- **Responsive Design**: Works on desktop and tablet
- **Professional Layout**: Sidebar controls, status bar

### 📋 Output Management
- **Copy to Clipboard**: One-click code copying
- **Download HTML**: Save generated code as .html file
- **Formatted Output**: Clean, indented HTML structure
- **Section Comments**: Clear section markers in output

## 🎯 How to Use

### Step 1: Prepare Your Content
Create a text file with labeled sections:
```
[HERO]
Heading: Your Service Title
Description: Your service description...
Bullet 1: First benefit
Bullet 2: Second benefit

[FAQ]
Heading: Frequently Asked Questions
Question 1: What is this service?
Answer 1: This service helps you...
```

### Step 2: Upload or Paste Content
- **Upload**: Drag your file to the upload area
- **Paste**: Copy content directly into the input editor
- **Edit**: Modify content in the input pane

### Step 3: Select Sections
- ✅ Check which sections you want to generate
- Choose from: Hero, FAQ, CTA, Process, Technology, Industries
- All sections selected by default

### Step 4: Generate HTML
- 🔄 Click "Generate HTML" button
- ⏱️ Processing indicator shows progress
- ✅ Generated HTML appears in output pane

### Step 5: Use Your Code
- 📋 **Copy**: Click "Copy Code" for clipboard
- 💾 **Download**: Click "Download" for HTML file
- 🔗 **Deploy**: Use generated code in your website

## 📋 Supported Document Format

### Section Labels
Use square brackets to label each section:
- `[HERO]` - Hero section with form
- `[FAQ]` - Frequently asked questions
- `[CTA_SIMPLE]` - Call-to-action section
- `[PROCESS]` - Process steps with numbers
- `[TECHNOLOGY]` - Technology stack showcase
- `[INDUSTRIES]` - Industries served section

### Content Fields
Each section supports specific fields:

#### Hero Section
```
Heading: Main service title
Description: Service description paragraph
Bullet 1: First benefit point
Bullet 2: Second benefit point
Form Heading: Contact form title
Form Button: Button text
```

#### FAQ Section
```
Heading: FAQ section title
Question 1: First question?
Answer 1: Answer to first question
Question 2: Second question?
Answer 2: Answer to second question
```

#### Technology Section
```
Heading: Technology section title
Description: Technology description
Technologies: React, Node.js, Python, AWS
```

## 🔧 Technical Details

### Architecture
- **Frontend**: Pure HTML, CSS, JavaScript
- **Processing**: Client-side JavaScript engine
- **Templates**: Embedded HTML section templates
- **Assets**: Predefined technology and industry data

### Browser Support
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

### File Support
- ✅ **Text Files** (.txt) - Full support
- ⚠️ **Word Documents** (.doc, .docx) - Basic text extraction
- 📋 **Copy/Paste** - Direct content input

### Performance
- ⚡ **Client-side processing** - No server required
- 🔄 **Real-time generation** - Instant preview
- 💾 **Lightweight** - Single HTML file
- 🚀 **Fast startup** - No build process

## 🎨 Interface Features

### Professional Design
- 🌙 **Dark Theme**: Easy on the eyes for long sessions
- 🎯 **VS Code Style**: Familiar developer interface
- 📱 **Responsive**: Works on different screen sizes
- ⚡ **Fast Performance**: Smooth interactions

### User Experience
- 🎯 **Drag & Drop**: Intuitive file handling
- 📋 **One-click Copy**: Easy code copying
- 💾 **Auto Download**: Instant file generation
- ✅ **Clear Status**: Real-time processing feedback

### Code Quality
- 🏗️ **Perfect Structure**: Maintains exact HTML classes
- 🎨 **Bootstrap Ready**: Uses correct responsive classes
- 🔗 **SEO Friendly**: Proper heading hierarchy
- 📱 **Mobile Optimized**: Responsive grid systems

## 🚨 Troubleshooting

### Common Issues

**"Port already in use"**
- Try a different port: `python3 -m http.server 8001`
- Or kill existing process and retry

**"File not loading"**
- Check file format (should be plain text)
- Try copy/paste instead of file upload
- Ensure file isn't corrupted

**"No sections generated"**
- Verify section labels: `[HERO]`, `[FAQ]`, etc.
- Check that content follows format examples
- Ensure at least one section is selected

**"Browser compatibility"**
- Use modern browser (Chrome, Firefox, Safari, Edge)
- Enable JavaScript
- Clear browser cache if issues persist

## 🔄 Updates & Extensions

### Current Version: 1.0
- ✅ 6 section types implemented
- ✅ File upload & processing
- ✅ Copy/download functionality
- ✅ Real-time generation

### Future Enhancements
- 🔜 More section types (Services Grid, Portfolio, etc.)
- 🔜 Custom template editing
- 🔜 Export to multiple formats
- 🔜 Advanced file format support

## 🆘 Support

If you encounter issues:
1. Check the browser console for errors
2. Verify your content format matches examples
3. Try the command-line tool as fallback
4. Refresh the page and try again

The web IDE provides the same powerful content processing as the command-line tool, but with an intuitive browser interface that makes it easy to generate professional HTML sections from your documents.