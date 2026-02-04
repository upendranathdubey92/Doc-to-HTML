# Document to HTML Converter Tools

## 🔷 MCB Tool (Monocubed)
**Location**: `MCB-Tool/web_ide_mcb.html`
**Port**: 8080
**URL**: http://localhost:8080/MCB-Tool/web_ide_mcb.html

### Features:
- 18 Monocubed-specific sections
- Blue branding (#1C72EB)
- MCB-style.css
- Technology stack with 380+ icons
- FAQ with bullet support
- Section-specific CSS classes

---

## 🟢 SOI Tool (Space-O Technologies)
**Location**: `SOI-Tool/web_ide_final.html`
**Port**: 8080
**URL**: http://localhost:8080/SOI-Tool/web_ide_final.html

### Features:
- 19 Space-O sections
- Green branding (#28A745)
- Built-in styles
- Comprehensive section types

---

## 🚀 Quick Start

### Start Server:
```bash
npx http-server -p 8080 -c-1
```

### Access Tools:
- **MCB**: http://localhost:8080/MCB-Tool/web_ide_mcb.html
- **SOI**: http://localhost:8080/SOI-Tool/web_ide_final.html

---

## 📁 Project Structure
```
Doc-to-HTML/
├── MCB-Tool/                   # Monocubed tool
│   ├── web_ide_mcb.html        # Main MCB tool (FIXED)
│   ├── MCB-style.css
│   ├── MCB-README.md
│   └── [all MCB files]
│
├── SOI-Tool/                   # Space-O tool
│   ├── web_ide_final.html      # Main SOI tool
│   ├── CLAUDE.md
│   └── README.md
│
├── package.json
├── vercel.json
└── INDEX.md                    # This file
```

---

## ✅ Status
- **MCB Tool**: ✅ Fixed (no smart quotes)
- **SOI Tool**: ✅ Working
- **Separation**: ✅ Complete
- **Server**: Running on port 8080
