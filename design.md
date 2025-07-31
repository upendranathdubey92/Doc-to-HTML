# HTML Templates for Document to HTML Converter

This file contains all the HTML template code from the web IDE for reference and backup.

## Complete Web IDE HTML Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Document to HTML Converter</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        .header h1 {
            color: #2d3748;
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            color: #4a5568;
            font-size: 1.1rem;
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .panel {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 600px;
        }

        .panel-header {
            background: linear-gradient(135deg, #4299e1, #3182ce);
            color: white;
            padding: 20px 30px;
            font-size: 1.2rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .panel-content {
            flex: 1;
            padding: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .file-upload-area {
            border: 3px dashed #cbd5e0;
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            margin: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: #f8fafc;
        }

        .file-upload-area:hover, .file-upload-area.dragover {
            border-color: #4299e1;
            background: #ebf8ff;
            transform: translateY(-2px);
        }

        .file-upload-area .icon {
            font-size: 3rem;
            margin-bottom: 15px;
            color: #4299e1;
        }

        .file-upload-area .text {
            font-size: 1.1rem;
            color: #4a5568;
            margin-bottom: 10px;
        }

        .file-upload-area .subtext {
            font-size: 0.9rem;
            color: #718096;
        }

        .file-info {
            background: #e6fffa;
            border: 1px solid #38b2ac;
            border-radius: 10px;
            padding: 15px 20px;
            margin: 20px;
            display: none;
        }

        .file-info-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }

        .file-info-row:last-child {
            margin-bottom: 0;
        }

        .file-info-label {
            font-weight: 600;
            color: #2d3748;
        }

        .file-info-value {
            color: #4a5568;
        }

        #inputContent {
            flex: 1;
            border: none;
            resize: none;
            font-family: 'JetBrains Mono', 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.6;
            padding: 20px;
            background: #f8fafc;
            color: #2d3748;
            outline: none;
        }

        #outputCode {
            flex: 1;
            border: none;
            resize: none;
            font-family: 'JetBrains Mono', 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.5;
            padding: 20px;
            background: #1a202c;
            color: #e2e8f0;
            outline: none;
        }

        .toolbar {
            padding: 20px 30px;
            background: #f7fafc;
            border-top: 1px solid #e2e8f0;
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }

        .btn {
            background: linear-gradient(135deg, #4299e1, #3182ce);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn:hover:not(:disabled) {
            background: linear-gradient(135deg, #3182ce, #2b77cb);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(66, 153, 225, 0.4);
        }

        .btn:disabled {
            background: #cbd5e0;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        #aiConfigBtn {
            background: linear-gradient(135deg, #38b2ac, #319795);
        }

        #aiConfigBtn:hover {
            background: linear-gradient(135deg, #319795, #2c7a7b);
        }

        .status {
            margin-left: auto;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            background: #edf2f7;
            color: #4a5568;
        }

        .status.success {
            background: #c6f6d5;
            color: #276749;
        }

        .status.error {
            background: #fed7d7;
            color: #c53030;
        }

        .ai-config {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            display: none;
        }

        .ai-config h3 {
            color: #2d3748;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            color: #4a5568;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .form-group input[type="text"], .form-group input[type="password"] {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 14px;
            transition: border-color 0.3s ease;
        }

        .form-group input[type="text"]:focus, .form-group input[type="password"]:focus {
            outline: none;
            border-color: #4299e1;
        }

        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .checkbox-group input[type="checkbox"] {
            width: 18px;
            height: 18px;
            accent-color: #4299e1;
        }

        .info-panels {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .info-panel {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        .info-panel h3 {
            color: #2d3748;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .section-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .section-tag {
            background: #e6fffa;
            color: #234e52;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 5px;
            border: 1px solid #38b2ac;
        }

        .section-tag.not-found {
            background: #fed7d7;
            color: #742a2a;
            border-color: #fc8181;
        }

        .section-tag .check {
            font-weight: bold;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        .stat-item {
            text-align: center;
            padding: 15px;
            background: #f8fafc;
            border-radius: 10px;
        }

        .stat-number {
            font-size: 1.8rem;
            font-weight: bold;
            color: #4299e1;
            display: block;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #718096;
            margin-top: 5px;
        }

        .toast {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            z-index: 1000;
            animation: slideIn 0.3s ease;
        }

        .toast.success {
            background: linear-gradient(135deg, #48bb78, #38a169);
        }

        .toast.error {
            background: linear-gradient(135deg, #f56565, #e53e3e);
        }

        .toast.info {
            background: linear-gradient(135deg, #4299e1, #3182ce);
        }

        @keyframes slideIn {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        .loading {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid #cbd5e0;
            border-radius: 50%;
            border-top-color: #4299e1;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .hidden {
            display: none !important;
        }

        /* Responsive Design */
        @media (max-width: 1200px) {
            .main-grid, .info-panels {
                grid-template-columns: 1fr;
            }
            
            .panel {
                height: 400px;
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .toolbar {
                padding: 15px 20px;
            }
            
            .btn {
                padding: 10px 18px;
                font-size: 13px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Enhanced Document to HTML Converter</h1>
            <p>Convert structured documents with section markers into beautiful HTML - Now with AI-powered content understanding!</p>
        </div>

        <div id="aiConfig" class="ai-config">
            <h3>🤖 AI Configuration</h3>
            <div class="form-group">
                <label for="apiKeyInput">Groq API Key (Free tier available):</label>
                <input type="password" id="apiKeyInput" placeholder="Enter your Groq API key..." />
            </div>
            <div class="form-group">
                <div class="checkbox-group">
                    <input type="checkbox" id="useAICheckbox" />
                    <label for="useAICheckbox">Enable AI-powered content parsing</label>
                </div>
            </div>
        </div>

        <div class="info-panels" id="detectedSections" style="display: none;">
            <div class="info-panel">
                <h3>📋 Detected Sections (<span id="sectionCount">0</span>)</h3>
                <div id="sectionTags" class="section-tags"></div>
            </div>
            <div class="info-panel" id="statsPanel" style="display: none;">
                <h3>📊 Content Statistics</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <span id="lineCount" class="stat-number">0</span>
                        <div class="stat-label">Lines</div>
                    </div>
                    <div class="stat-item">
                        <span id="wordCount" class="stat-number">0</span>
                        <div class="stat-label">Words</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-grid">
            <div class="panel">
                <div class="panel-header">
                    📝 Document Input
                </div>
                <div class="panel-content">
                    <div id="fileUpload" class="file-upload-area">
                        <div class="icon">📄</div>
                        <div class="text">Drop Word document here or click to browse</div>
                        <div class="subtext">Supports .docx, .doc, and .txt files</div>
                        <input type="file" id="fileInput" style="display: none;" accept=".docx,.doc,.txt" />
                    </div>
                    <div id="fileInfo" class="file-info">
                        <div class="file-info-row">
                            <span class="file-info-label">File:</span>
                            <span id="fileName" class="file-info-value">-</span>
                        </div>
                        <div class="file-info-row">
                            <span class="file-info-label">Size:</span>
                            <span id="fileSize" class="file-info-value">-</span>
                        </div>
                        <div class="file-info-row">
                            <span class="file-info-label">Type:</span>
                            <span id="fileType" class="file-info-value">-</span>
                        </div>
                        <div class="file-info-row">
                            <span class="file-info-label">Status:</span>
                            <span id="fileStatus" class="file-info-value">-</span>
                        </div>
                    </div>
                    <textarea id="inputContent" placeholder="Or paste your document content here with [SECTION] markers...

Example format:
[HERO]
Web Development Consulting Services
Struggling with slow website performance, unclear tech decisions, or platforms that don't scale with your business? Our web development consulting services are designed to eliminate guesswork and align your digital presence with tangible business outcomes. The result?

●High-performing websites that load faster and deliver smoother user experiences
●Scalable, future-ready architecture designed to support business growth
●Technology stack recommendations that reduce risk and speed up development

[HERO END]

[SERVICES_GRID]
Web Development Consulting Services to Build the Right Foundation
We help businesses make smart, strategic decisions before development begins...
[SERVICES_GRID END]"></textarea>
                </div>
                <div class="toolbar">
                    <button id="processBtn" class="btn" disabled>
                        <span id="processIcon">⚡</span> Convert to HTML
                    </button>
                    <button id="formatBtn" class="btn">
                        📝 Format Content
                    </button>
                    <button id="clearBtn" class="btn">
                        🗑️ Clear All
                    </button>
                    <button id="aiConfigBtn" class="btn">
                        🤖 AI Settings
                    </button>
                    <span id="statusText" class="status">Upload a Word document or paste content to get started</span>
                </div>
            </div>

            <div class="panel">
                <div class="panel-header">
                    💻 HTML Output
                </div>
                <div class="panel-content">
                    <textarea id="outputCode" readonly placeholder="Generated HTML will appear here..."></textarea>
                </div>
                <div class="toolbar">
                    <button id="copyBtn" class="btn" disabled>
                        📋 Copy HTML
                    </button>
                    <button id="downloadBtn" class="btn" disabled>
                        💾 Download
                    </button>
                    <span class="status">Ready for conversion</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Real Document Processing Engine with AI Integration
        class RealDocumentProcessor {
            constructor() {
                this.useAI = false;
            }

            detectSections(content) {
                const sectionRegex = /\[([A-Z_\s]+)\]/g;
                const matches = [...content.matchAll(sectionRegex)];
                return matches.map(match => match[1].trim()).filter(section => !section.endsWith('END'));
            }

            async processContent(content) {
                try {
                    const sections = this.extractSections(content);
                    let generatedHTML = '';
                    let sectionsGenerated = [];

                    for (const [sectionType, sectionContent] of Object.entries(sections)) {
                        if (this.useAI) {
                            try {
                                const aiParsedContent = await this.parseWithAI(sectionContent, sectionType);
                                const html = this.generateHTMLForSection(sectionType, aiParsedContent);
                                generatedHTML += html + '\n\n';
                                sectionsGenerated.push(sectionType);
                            } catch (aiError) {
                                console.warn(`AI parsing failed for ${sectionType}, falling back to rule-based parsing:`, aiError);
                                const parsedContent = this.parseWithRules(sectionContent, sectionType);
                                const html = this.generateHTMLForSection(sectionType, parsedContent);
                                generatedHTML += html + '\n\n';
                                sectionsGenerated.push(sectionType);
                            }
                        } else {
                            const parsedContent = this.parseWithRules(sectionContent, sectionType);
                            const html = this.generateHTMLForSection(sectionType, parsedContent);
                            generatedHTML += html + '\n\n';
                            sectionsGenerated.push(sectionType);
                        }
                    }

                    return {
                        success: true,
                        html: generatedHTML.trim(),
                        sectionsGenerated: sectionsGenerated
                    };
                } catch (error) {
                    return {
                        success: false,
                        error: error.message
                    };
                }
            }

            extractSections(content) {
                const sections = {};
                const lines = content.split('\n');
                let currentSection = null;
                let currentContent = [];

                for (let i = 0; i < lines.length; i++) {
                    const line = lines[i].trim();

                    // Check for section markers
                    if (line.startsWith('[') && line.endsWith(']')) {
                        // Save previous section
                        if (currentSection && currentContent.length > 0) {
                            sections[currentSection] = currentContent.join('\n').trim();
                        }

                        // Start new section - remove brackets and ignore END markers
                        const sectionName = line.slice(1, -1);
                        if (!sectionName.endsWith(' END')) {
                            currentSection = sectionName;
                            currentContent = [];
                        } else {
                            currentSection = null;
                        }
                    } else if (currentSection && line) {
                        // Only add non-empty lines to current section
                        currentContent.push(line);
                    }
                }

                // Save last section
                if (currentSection && currentContent.length > 0) {
                    sections[currentSection] = currentContent.join('\n').trim();
                }

                return sections;
            }

            async parseWithAI(content, sectionType) {
                const apiKey = localStorage.getItem('groqApiKey');
                if (!apiKey) {
                    throw new Error('No API key configured. Please add your Groq API key in AI Settings.');
                }

                const systemPrompt = `You are an expert content parser. Parse the following ${sectionType} section content and extract structured information. Return a JSON object with the appropriate fields for this section type.

For HERO sections, return: {"main_heading": "...", "description": "...", "bullet_points": ["...", "..."], "breadcrumb_title": "...", "form_heading": "..."}
For SERVICES_GRID sections, return: {"main_heading": "...", "description": "...", "services": [{"title": "...", "description": "...", "bullets": ["...", "..."]}]}
For SERVICES_ACCORDION sections, return: {"services": [{"title": "...", "description": "...", "bullets": ["...", "..."]}]}
For FAQ sections, return: {"main_heading": "...", "faqs": [{"question": "...", "answer": "..."}]}
For CTA_SIMPLE sections, return: {"main_heading": "...", "description": "...", "button_text": "..."}

Parse content carefully and extract meaningful information. Preserve the original meaning and structure.`;

                const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${apiKey}`
                    },
                    body: JSON.stringify({
                        model: 'llama-3.1-70b-versatile',
                        messages: [
                            {
                                role: 'system',
                                content: systemPrompt
                            },
                            {
                                role: 'user',
                                content: content
                            }
                        ],
                        temperature: 0.1,
                        max_tokens: 2000
                    })
                });

                if (!response.ok) {
                    throw new Error(`AI API error: ${response.status} ${response.statusText}`);
                }

                const data = await response.json();
                const aiResponse = data.choices[0].message.content;

                try {
                    return JSON.parse(aiResponse);
                } catch (parseError) {
                    // If JSON parsing fails, try to extract JSON from the response
                    const jsonMatch = aiResponse.match(/\{[\s\S]*\}/);
                    if (jsonMatch) {
                        return JSON.parse(jsonMatch[0]);
                    }
                    throw new Error('Invalid JSON response from AI');
                }
            }

            parseWithRules(content, sectionType) {
                const lines = content.split('\n').filter(line => line.trim());

                if (sectionType.includes('HERO')) {
                    return this.parseHeroSection(lines);
                } else if (sectionType.includes('SERVICES_GRID')) {
                    return this.parseServicesGridSection(lines);
                } else if (sectionType.includes('SERVICES_ACCORDION')) {
                    return this.parseServicesAccordionSection(lines);
                } else if (sectionType.includes('FAQ')) {
                    return this.parseFaqSection(lines);
                } else if (sectionType.includes('CTA')) {
                    return this.parseCtaSection(lines);
                }

                return { content: content };
            }

            parseHeroSection(lines) {
                const result = {
                    main_heading: lines[0] || 'Default Heading',
                    description: '',
                    bullet_points: [],
                    breadcrumb_title: lines[0] || 'Default Heading',
                    form_heading: 'Dream It, We Build It'
                };

                let inBullets = false;
                let descriptionLines = [];

                for (let i = 1; i < lines.length; i++) {
                    const line = lines[i];

                    if (line.includes('The result?')) {
                        inBullets = true;
                        // Add everything before "The result?" to description
                        if (line !== 'The result?') {
                            descriptionLines.push(line.split('The result?')[0].trim());
                        }
                        continue;
                    }

                    if (!inBullets) {
                        if (line.trim()) {
                            descriptionLines.push(line);
                        }
                    } else {
                        if (line.match(/^[●\-\*•‑]\s*/)) {
                            const bulletText = line.replace(/^[●\-\*•‑]\s*/, '').trim();
                            result.bullet_points.push(bulletText);
                        }
                    }
                }

                result.description = descriptionLines.join(' ').trim();
                return result;
            }

            parseServicesGridSection(lines) {
                const result = {
                    main_heading: lines[0] || 'Our Services',
                    description: '',
                    services: []
                };

                let currentService = null;
                let awaitingServiceDescription = false;

                for (let i = 1; i < lines.length; i++) {
                    const line = lines[i];

                    // Skip the main description (second line)
                    if (i === 1 && !line.match(/^[●\-\*•‑]\s*/)) {
                        result.description = line;
                        continue;
                    }

                    if (line.match(/^[●\-\*•‑]\s*/)) {
                        // This is a bullet point
                        const bulletText = line.replace(/^[●\-\*•‑]\s*/, '').trim();
                        if (currentService) {
                            if (!currentService.bullets) {
                                currentService.bullets = [];
                            }
                            currentService.bullets.push(bulletText);
                        }
                        awaitingServiceDescription = false;
                    } else {
                        // This is regular text
                        if (!currentService || !awaitingServiceDescription) {
                            // Start new service
                            if (currentService) {
                                result.services.push(currentService);
                            }
                            currentService = {
                                title: line,
                                description: '',
                                bullets: []
                            };
                            awaitingServiceDescription = true;
                        } else {
                            // This is the service description
                            currentService.description = line;
                            awaitingServiceDescription = false;
                        }
                    }
                }

                // Add last service
                if (currentService) {
                    result.services.push(currentService);
                }

                return result;
            }

            parseServicesAccordionSection(lines) {
                const result = {
                    services: []
                };

                let currentService = null;
                let awaitingServiceDescription = false;
                let inBullets = false;

                for (let i = 0; i < lines.length; i++) {
                    const line = lines[i];

                    if (line.match(/^[●\-\*•‑]\s*/)) {
                        // This is a bullet point
                        const bulletText = line.replace(/^[●\-\*•‑]\s*/, '').trim();
                        if (currentService) {
                            if (!currentService.bullets) {
                                currentService.bullets = [];
                            }
                            currentService.bullets.push(bulletText);
                        }
                        inBullets = true;
                        awaitingServiceDescription = false;
                    } else {
                        // This is regular text
                        if (inBullets || !currentService || !awaitingServiceDescription) {
                            // Start new service
                            if (currentService) {
                                result.services.push(currentService);
                            }
                            currentService = {
                                title: line,
                                description: '',
                                bullets: []
                            };
                            awaitingServiceDescription = true;
                            inBullets = false;
                        } else {
                            // This is the service description
                            currentService.description = line;
                            awaitingServiceDescription = false;
                        }
                    }
                }

                // Add last service
                if (currentService) {
                    result.services.push(currentService);
                }

                return result;
            }

            parseFaqSection(lines) {
                const result = {
                    main_heading: lines[0] || 'FAQ',
                    faqs: []
                };

                let currentFaq = null;

                for (let i = 1; i < lines.length; i++) {
                    const line = lines[i];

                    if (line.endsWith('?')) {
                        // Save previous FAQ
                        if (currentFaq) {
                            result.faqs.push(currentFaq);
                        }
                        // Start new FAQ
                        currentFaq = {
                            question: line,
                            answer: ''
                        };
                    } else if (currentFaq) {
                        // Add to current answer
                        if (currentFaq.answer) {
                            currentFaq.answer += ' ';
                        }
                        currentFaq.answer += line;
                    }
                }

                // Add last FAQ
                if (currentFaq) {
                    result.faqs.push(currentFaq);
                }

                return result;
            }

            parseCtaSection(lines) {
                return {
                    main_heading: lines[0] || 'Ready to Get Started?',
                    description: lines[1] || 'Let us help you achieve your goals',
                    button_text: lines[2] || 'Get Started'
                };
            }

            generateHTMLForSection(sectionType, content) {
                if (sectionType.includes('HERO')) {
                    return this.generateHeroSection(content);
                } else if (sectionType.includes('FAQ')) {
                    return this.generateFaqSection(content);
                } else if (sectionType.includes('CTA')) {
                    return this.generateCtaSection(content);
                } else if (sectionType.includes('PROCESS')) {
                    return this.generateProcessSection(content);
                } else if (sectionType.includes('TECHNOLOGY')) {
                    return this.generateTechnologySection(content);
                } else if (sectionType.includes('INDUSTRIES')) {
                    return this.generateIndustriesSection(content);
                } else if (sectionType.includes('SERVICES_GRID')) {
                    return this.generateServicesGridSection(content);
                } else if (sectionType.includes('SERVICES_ACCORDION')) {
                    return this.generateServicesAccordionSection(content);
                } else if (sectionType.includes('PORTFOLIO')) {
                    return this.generatePortfolioSection(content);
                } else if (sectionType.includes('TESTIMONIAL')) {
                    return this.generateTestimonialSection(content);
                } else if (sectionType.includes('BENEFITS')) {
                    return this.generateBenefitsSection(content);
                } else if (sectionType.includes('CONTENT_FORM')) {
                    return this.generateContentFormSection(content);
                }
                return `<div><!-- ${sectionType} section not implemented yet --></div>`;
            }

            generateHeroSection(content) {
                let bulletPoints = '';
                if (content.bullet_points) {
                    for (let bullet of content.bullet_points) {
                        bulletPoints += `    <li>${bullet}</li>\n`;
                    }
                }

                const template = `<section class="pt70 pb40 hero-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-7 col-md-12 banner-text">
<nav aria-label="breadcrumbs" class="rank-math-breadcrumb mb-3 mt-3"><p><a href="/" class="local" style="text-decoration: unset;">Home</a><span class="separator"> &gt; </span><a href="/services/" class="local" style="text-decoration: unset;">Services</a><span class="separator"> &gt; </span><span class="last">{breadcrumb_title}</span></p></nav>
<h1 class="fonts-45 mb-3 font-weight-bold">{main_heading}</h1>
<p class="fonts-18 mb-3">{description} The result?</p>
<ul class="bullet mb-5 fonts-18">
{bullet_points}
</ul>

<div class="rating-section d-flex"><a href="https://goo.gl/maps/1JSqiZssNiDHAppx8" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/google-rating.svg" alt="Google" width="97" height="56" /></a>
<a href="https://clutch.co/profile/space-o-technologies#reviews" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/clutch-rating.svg" alt="Clutch" width="99" height="56" /></a>
<a href="https://www.goodfirms.co/company/space-o-technologies#reviews" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/goodfirm-rating.svg" alt="GoodFirms" width="135" height="56" /></a></div>
</div>
<div class="col-lg-5 col-md-12 text-form-section">
<div class="homen_form">
<p class="fonts-24 font-weight-bold mt-0 mb-2 text-center line-height-1">{form_heading}</p>
<form id="other-form" class="footer_form append-form blur-form" action="" method="post" name="popup-form" novalidate="">
<div class="row">
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-user"></i><input id="name" class="form-control" name="name" required="" size="40" type="text" value="" placeholder="Name*" data-name="Please enter your name" /><small class="error"></small></p>

<div class="clearfix"></div>
</div>
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-envelope"></i><input id="email" class="form-control" name="email" required="" size="40" type="email" value="" placeholder="Email*" data-name="Please enter your email" /><small class="error"></small></p>

<div class="clearfix"></div>
</div>
</div>
<div class="row">
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-phone"></i><input id="number" class="form-control" name="number" required="" size="15" type="tel" value="" placeholder="Phone*" data-name="Please enter your number" /><small class="error"></small><span id="error-msg" class="d-none"></span></p>

<div class="clearfix"></div>
</div>
</div>
<div class="row">
<div class="form-group col-md-12 mb-0 text-left"><textarea id="Comment" class="form-control" cols="40" name="comment" required="" rows="3" placeholder="Write your message.*" data-name="Please enter your description"></textarea><small class="error"></small></div>
</div>
<div class="row">
<div class="form-group col-md-12">
<div class="footer_txt_block mt-2">
<input id="form_type" name="form_type" type="hidden" value="footer_form" />
[spaceo_get_permalink][spaceo_get_referal]
<div id="loadingmessage" class="loader"><img src="/wp-content/uploads/2021/04/ajax-loader.gif" alt="Ajax loader" width="30" height="30" /></div>
<input id="submit" class="btn btn-pop mb0" name="submit" type="submit" value="Book Your Free Consultation " data-medium="BF_1" />

</div>
</div>
</div>
</form></div>
</div>
</div>
</div>
</section>

<section class="pt40 pb40 client-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-2 col-md-12 client-title">Our Valuable Clients</div>
<div class="col-lg-10 col-md-12 client-logo">
<img src="/wp-content/uploads/2023/08/client-logo-01.svg" alt="client-logo" width="100" height="54" />
<img src="/wp-content/uploads/2023/08/client-logo-02.svg" alt="client-logo" width="154" height="54" />
<img src="/wp-content/uploads/2023/08/client-logo-03.svg" alt="client-logo" width="101" height="54" />
<img src="/wp-content/uploads/2023/08/client-logo-04.svg" alt="client-logo" width="130" height="54" />
</div>
</div>
</div>
</section>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'Service Title')
                    .replace('{description}', content.description || 'Service description')
                    .replace('{bullet_points}', bulletPoints.trim())
                    .replace('{breadcrumb_title}', content.breadcrumb_title || content.main_heading || 'Service Title')
                    .replace('{form_heading}', content.form_heading || 'Dream It, We Build It');
            }

            generateFaqSection(content) {
                let faqItems = '';
                if (content.faqs) {
                    content.faqs.forEach((faq, index) => {
                        const collapseId = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'][index] || 'item' + index;
                        const isActive = index === 0 ? 'active' : '';
                        const showCollapse = index === 0 ? 'style="display:block;"' : '';
                        
                        faqItems += `      <div class="card py-4">
        <div class="card-header ${isActive}">
          <h3 class="card-link" data-toggle="collapse" href="#${collapseId}">${faq.question}</h3>
          <div id="${collapseId}" class="collapse" data-parent="#accordion" ${showCollapse}>
            <div class="card card-body">
              ${faq.answer}
            </div>
          </div>
        </div>
      </div>
`;
                    });
                }

                const template = `<div class="faq pt80 pb50" style="background: linear-gradient(var(--bg-color-9), #fff);">
  <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center">{main_heading}</h2>
    <div id="accordion" class="text-left px-4">
${faqItems}
    </div>
  </div>
</div>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'FAQs About Web Development Consulting');
            }

            generateCtaSection(content) {
                const template = `<section class="pt80 pb80 new-cta-section">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title mxw-1000">{main_heading}</p>
<p class="fonts-20 mxw-900">{description}</p>
</div>
<div class="col-md-12 text-center mt-4"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">{button_text}</button></div>
</div>
</div>
</div>
</section>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'Ready to Get Started?')
                    .replace('{description}', content.description || 'Let us help you achieve your goals')
                    .replace('{button_text}', content.button_text || 'Get Started');
            }

            generateProcessSection(content) {
                const template = `<section class="pt80 pb50 process-section bg-light">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
{process_steps}
</div>
</div>
</section>`;

                let processSteps = '';
                if (content.steps) {
                    content.steps.forEach((step, index) => {
                        processSteps += `<div class="col-lg-3 col-md-6 mb-4">
<div class="process-box text-center">
<div class="step-number">${index + 1}</div>
<h3 class="fonts-20 font-weight-bold mb-2">${step.title}</h3>
<p class="fonts-16">${step.description}</p>
</div>
</div>
`;
                    });
                }

                return template
                    .replace('{main_heading}', content.main_heading || 'Our Process')
                    .replace('{description}', content.description || 'How we work')
                    .replace('{process_steps}', processSteps);
            }

            generateTechnologySection(content) {
                const template = `<section class="pt70 pb40 technology-section bg-light">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-45 mb-3 font-weight-bold">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
<div class="col-lg-12">
<div class="tech-stack">
{tech_items}
</div>
</div>
</div>
</div>
</section>`;

                let techItems = '';
                if (content.technologies) {
                    content.technologies.forEach(tech => {
                        techItems += `<div class="tech-item">
<img src="${tech.image}" alt="${tech.name}" width="60" height="60" />
<h4>${tech.name}</h4>
</div>
`;
                    });
                }

                return template
                    .replace('{main_heading}', content.main_heading || 'Technology Stack')
                    .replace('{description}', content.description || 'Technologies we use')
                    .replace('{tech_items}', techItems);
            }

            generateIndustriesSection(content) {
                const template = `<section class="pt80 pb50 industries-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
{industry_items}
</div>
</div>
</section>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'Industries We Serve')
                    .replace('{description}', content.description || 'We serve various industries');
            }

            generateServicesGridSection(content) {
                const serviceImages = [
                    '/wp-content/uploads/2023/09/Architecture-and-Design-Consulting.svg',
                    '/wp-content/uploads/2025/07/ux-performance-optimization.svg',
                    '/wp-content/uploads/2024/02/Legacy-App-Modernization.svg',
                    '/wp-content/uploads/2025/07/code-audits-quality-assurance.svg',
                    '/wp-content/uploads/2023/09/MVP-Development.svg',
                    '/wp-content/uploads/2024/03/Third-party-Integrations.svg'
                ];

                let servicesGrid = '';
                if (content.services) {
                    content.services.forEach((service, index) => {
                        const imageSrc = serviceImages[index] || serviceImages[0];
                        
                        // Generate bullet points if they exist
                        let bulletHtml = '';
                        if (service.bullets && service.bullets.length > 0) {
                            bulletHtml = '<ul class="bullet fonts-16">';
                            service.bullets.forEach(bullet => {
                                bulletHtml += `<li>${bullet}</li>`;
                            });
                            bulletHtml += '</ul>';
                        }
                        
                        servicesGrid += `
<div class="col-lg-4 col-md-6">
<div class="mad_service_box">
<img src="${imageSrc}" alt="${service.title}" width="74" height="74" />
<h3 class="fonts-18 font-weight-semibold">${service.title}</h3>
<p>${service.description}</p>
${bulletHtml}
</div>
</div>
`;
                    });
                }

                const template = `<section class="pt80 pb50 services-section bg-color">
<div class="container-xl">
<h2 class="fonts-40 text-center font-weight-bold mb-3 mxw-1000">{main_heading}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
${servicesGrid}
</div>
</div>
</section>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'Our Services')
                    .replace('{description}', content.description || 'Services we provide');
            }

            generateServicesAccordionSection(content) {
                if (!content.services || content.services.length === 0) {
                    return '<div>No services found</div>';
                }

                const services = content.services;
                const totalServices = services.length;

                // If 3 or fewer services, use single section
                if (totalServices <= 3) {
                    return this.generateSingleAccordionSection(services);
                }

                // If more than 3, split into multiple sections with swapped columns
                return this.generateMultipleAccordionSections(services);
            }

            generateSingleAccordionSection(services) {
                const accordionImages = [
                    '/wp-content/uploads/2025/07/security-compliance-advisory.svg',
                    '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg',
                    '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg'
                ];

                const collapseIds = ['one', 'two', 'three'];
                let accordionItems = '';

                services.forEach((service, index) => {
                    const imageSrc = accordionImages[index] || accordionImages[0];
                    const collapseId = collapseIds[index] || `item_${index}`;
                    const isFirst = index === 0;
                    const cardHeaderClass = isFirst ? 'card-header active' : 'card-header';
                    const collapseClass = isFirst ? 'collapse show' : 'collapse';
                    const displayStyle = isFirst ? 'style="display:block;"' : '';
                    
                    // Generate bullet points if they exist
                    let bulletHtml = '';
                    if (service.bullets && service.bullets.length > 0) {
                        bulletHtml = '<ul class="bullet fonts-14 mb-3">';
                        service.bullets.forEach(bullet => {
                            bulletHtml += `<li>${bullet}</li>`;
                        });
                        bulletHtml += '</ul>';
                    }
                    
                    accordionItems += `<div class="card">
<div class="${cardHeaderClass}" ${displayStyle}>
<h3 class="card-link" data-toggle="collapse" href="#${collapseId}"><img src="${imageSrc}" width="34" height="34" alt="${service.title}" class="left-icons" loading="lazy" decoding="async">${service.title}</h3>
<div id="${collapseId}" class="${collapseClass}" data-parent="#accordion">
<div class="card card-body">
<p>${service.description}</p>
${bulletHtml}
</div>
</div>
</div>
</div>
`;
                });

                return `<section class="techno-stack pb80 bg-color services-tab-new">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
</div>
</div>
</section>`;
            }

            generateMultipleAccordionSections(services) {
                // Split services into groups of 3
                const serviceGroups = [];
                for (let i = 0; i < services.length; i += 3) {
                    serviceGroups.push(services.slice(i, i + 3));
                }

                let sectionsHtml = '';
                
                serviceGroups.forEach((group, groupIndex) => {
                    const accordionImages = [
                        '/wp-content/uploads/2025/07/security-compliance-advisory.svg',
                        '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg',
                        '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg'
                    ];

                    const collapseIds = ['one', 'two', 'three'];
                    let accordionItems = '';

                    group.forEach((service, index) => {
                        const imageSrc = accordionImages[index] || accordionImages[0];
                        const collapseId = collapseIds[index];
                        const isFirst = index === 0;
                        const cardHeaderClass = isFirst ? 'card-header active' : 'card-header';
                        const collapseClass = isFirst ? 'collapse show' : 'collapse';
                        const displayStyle = isFirst ? 'style="display:block;"' : '';
                        
                        // Generate bullet points if they exist
                        let bulletHtml = '';
                        if (service.bullets && service.bullets.length > 0) {
                            bulletHtml = '<ul class="bullet fonts-14 mb-3">';
                            service.bullets.forEach(bullet => {
                                bulletHtml += `<li>${bullet}</li>`;
                            });
                            bulletHtml += '</ul>';
                        }
                        
                        accordionItems += `<div class="card">
<div class="${cardHeaderClass}" ${displayStyle}>
<h3 class="card-link" data-toggle="collapse" href="#${collapseId}"><img src="${imageSrc}" width="34" height="34" alt="${service.title}" class="left-icons" loading="lazy" decoding="async">${service.title}</h3>
<div id="${collapseId}" class="${collapseClass}" data-parent="#accordion">
<div class="card card-body">
<p>${service.description}</p>
${bulletHtml}
</div>
</div>
</div>
</div>
`;
                    });

                    // Swap columns for alternating sections (odd sections have swapped layout)
                    const isSwapped = groupIndex % 2 === 1;
                    
                    if (isSwapped) {
                        // Swapped: Accordion left, Image right
                        sectionsHtml += `<section class="techno-stack pb80 bg-color services-tab-new">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
</div>
</div>
</section>

`;
                    } else {
                        // Normal: Image left, Accordion right
                        sectionsHtml += `<section class="techno-stack pb80 bg-color services-tab-new">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
</div>
</div>
</section>

`;
                    }
                });

                return sectionsHtml;
            }

            generatePortfolioSection(content) {
                const template = `<section class="pt80 pb60 portfolio-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
{portfolio_items}
</div>
</div>
</section>`;

                let portfolioItems = '';
                if (content.projects) {
                    content.projects.forEach(project => {
                        portfolioItems += `<div class="col-lg-4 col-md-6 mb-4">
<div class="portfolio-box">
<h3 class="fonts-20 font-weight-bold mb-2">${project.title}</h3>
<p class="fonts-16">${project.description}</p>
</div>
</div>
`;
                    });
                }

                return template
                    .replace('{main_heading}', content.main_heading || 'Our Portfolio')
                    .replace('{description}', content.description || 'Recent projects')
                    .replace('{portfolio_items}', portfolioItems);
            }

            generateTestimonialSection(content) {
                const template = `<section class="pt80 pb80 testimonial-section bg-light">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
{testimonial_items}
</div>
</div>
</section>`;

                let testimonialItems = '';
                if (content.testimonials) {
                    content.testimonials.forEach(testimonial => {
                        testimonialItems += `<div class="col-lg-4 col-md-6 mb-4">
<div class="testimonial-box">
<p class="fonts-16 mb-3">"${testimonial.content}"</p>
<h4 class="fonts-18 font-weight-bold">${testimonial.author}</h4>
<span class="fonts-14 text-muted">${testimonial.position}</span>
</div>
</div>
`;
                    });
                }

                return template
                    .replace('{main_heading}', content.main_heading || 'What Our Clients Say')
                    .replace('{description}', content.description || 'Client testimonials')
                    .replace('{testimonial_items}', testimonialItems);
            }

            generateBenefitsSection(content) {
                const template = `<section class="pt80 pb50 benefits-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
{benefit_items}
</div>
</div>
</section>`;

                let benefitItems = '';
                if (content.benefits) {
                    content.benefits.forEach(benefit => {
                        benefitItems += `<div class="col-lg-4 col-md-6 mb-4">
<div class="benefit-box text-center">
<h3 class="fonts-20 font-weight-bold mb-2">${benefit.title}</h3>
<p class="fonts-16">${benefit.description}</p>
</div>
</div>
`;
                    });
                }

                return template
                    .replace('{main_heading}', content.main_heading || 'Why Choose Us')
                    .replace('{description}', content.description || 'Our benefits')
                    .replace('{benefit_items}', benefitItems);
            }

            generateContentFormSection(content) {
                const template = `<section class="pt80 pb80 content-form-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-6">
<h2 class="fonts-40 font-weight-bold mb-3">{main_heading}</h2>
<p class="fonts-18 mb-4">{description}</p>
{content_text}
</div>
<div class="col-lg-6">
<div class="contact-form">
<form class="form">
<div class="form-group">
<input type="text" placeholder="Your Name" class="form-control" required>
</div>
<div class="form-group">
<input type="email" placeholder="Your Email" class="form-control" required>
</div>
<div class="form-group">
<textarea placeholder="Your Message" class="form-control" rows="5" required></textarea>
</div>
<button type="submit" class="btn btn-primary">Send Message</button>
</form>
</div>
</div>
</div>
</div>
</section>`;

                return template
                    .replace('{main_heading}', content.main_heading || 'Contact Us')
                    .replace('{description}', content.description || 'Get in touch')
                    .replace('{content_text}', content.content || 'Contact information');
            }
        }

        // Enhanced IDE Interface
        class EnhancedIDEInterface {
            constructor() {
                this.processor = new RealDocumentProcessor();
                this.currentFile = null;
                this.generatedCode = '';
                
                this.initializeElements();
                this.bindEvents();
                this.showWelcomeMessage();
            }

            initializeElements() {
                this.fileUpload = document.getElementById('fileUpload');
                this.fileInput = document.getElementById('fileInput');
                this.fileInfo = document.getElementById('fileInfo');
                this.fileName = document.getElementById('fileName');
                this.fileSize = document.getElementById('fileSize');
                this.fileType = document.getElementById('fileType');
                this.fileStatus = document.getElementById('fileStatus');
                this.inputContent = document.getElementById('inputContent');
                this.outputCode = document.getElementById('outputCode');
                this.processBtn = document.getElementById('processBtn');
                this.clearBtn = document.getElementById('clearBtn');
                this.copyBtn = document.getElementById('copyBtn');
                this.downloadBtn = document.getElementById('downloadBtn');
                this.formatBtn = document.getElementById('formatBtn');
                this.statusText = document.getElementById('statusText');
                this.detectedSections = document.getElementById('detectedSections');
                this.sectionTags = document.getElementById('sectionTags');
                this.sectionCount = document.getElementById('sectionCount');
                this.statsPanel = document.getElementById('statsPanel');
                this.lineCount = document.getElementById('lineCount');
                this.wordCount = document.getElementById('wordCount');
                this.processIcon = document.getElementById('processIcon');
                this.aiConfigBtn = document.getElementById('aiConfigBtn');
                this.aiConfig = document.getElementById('aiConfig');
                this.apiKeyInput = document.getElementById('apiKeyInput');
                this.useAICheckbox = document.getElementById('useAICheckbox');
            }

            bindEvents() {
                // File upload events
                this.fileUpload.addEventListener('click', () => this.fileInput.click());
                this.fileInput.addEventListener('change', (e) => this.handleFileSelect(e));
                
                // Drag and drop events
                this.fileUpload.addEventListener('dragover', (e) => this.handleDragOver(e));
                this.fileUpload.addEventListener('dragleave', (e) => this.handleDragLeave(e));
                this.fileUpload.addEventListener('drop', (e) => this.handleFileDrop(e));

                // Input content change
                this.inputContent.addEventListener('input', () => this.handleContentChange());

                // Button events
                this.processBtn.addEventListener('click', () => this.processContent());
                this.clearBtn.addEventListener('click', () => this.clearAll());
                this.copyBtn.addEventListener('click', () => this.copyCode());
                this.downloadBtn.addEventListener('click', () => this.downloadCode());
                this.formatBtn.addEventListener('click', () => this.formatContent());
                this.aiConfigBtn.addEventListener('click', () => this.toggleAIConfig());
                
                // AI configuration events
                this.useAICheckbox.addEventListener('change', (e) => {
                    this.processor.useAI = e.target.checked;
                    localStorage.setItem('useAI', e.target.checked);
                });
                
                this.apiKeyInput.addEventListener('input', (e) => {
                    localStorage.setItem('groqApiKey', e.target.value);
                });
                
                // Load saved settings
                this.loadAISettings();
            }
            
            loadAISettings() {
                const savedApiKey = localStorage.getItem('groqApiKey');
                const savedUseAI = localStorage.getItem('useAI');
                
                if (savedApiKey) {
                    this.apiKeyInput.value = savedApiKey;
                }
                
                if (savedUseAI !== null) {
                    this.useAICheckbox.checked = savedUseAI === 'true';
                    this.processor.useAI = savedUseAI === 'true';
                }
            }
            
            toggleAIConfig() {
                if (this.aiConfig.style.display === 'none') {
                    this.aiConfig.style.display = 'block';
                } else {
                    this.aiConfig.style.display = 'none';
                }
            }

            showWelcomeMessage() {
                this.showToast('🎉 Enhanced IDE ready! Now supports real Word documents!', 'success');
            }

            handleDragOver(e) {
                e.preventDefault();
                this.fileUpload.classList.add('dragover');
            }

            handleDragLeave(e) {
                e.preventDefault();
                this.fileUpload.classList.remove('dragover');
            }

            handleFileDrop(e) {
                e.preventDefault();
                this.fileUpload.classList.remove('dragover');
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    this.handleFile(files[0]);
                }
            }

            handleFileSelect(e) {
                const files = e.target.files;
                if (files.length > 0) {
                    this.handleFile(files[0]);
                }
            }

            handleFile(file) {
                this.currentFile = file;
                
                // Show file info
                this.fileName.textContent = file.name;
                this.fileSize.textContent = this.formatFileSize(file.size);
                this.fileType.textContent = file.type || 'Unknown';
                this.fileStatus.textContent = 'Processing...';
                this.fileInfo.style.display = 'block';

                // Read file content
                const reader = new FileReader();
                reader.onload = (e) => {
                    let content = e.target.result;
                    
                    // Handle Word document content (continuous text)
                    if (file.name.endsWith('.docx') || file.name.endsWith('.doc')) {
                        content = this.processWordContent(content);
                        this.fileStatus.textContent = 'Word document processed ✅';
                        this.showToast('📄 Word document processed successfully!', 'success');
                    } else {
                        this.fileStatus.textContent = 'Text file loaded ✅';
                        this.showToast('📝 Text file loaded successfully!', 'success');
                    }
                    
                    this.inputContent.value = content;
                    this.handleContentChange();
                };
                reader.onerror = () => {
                    this.fileStatus.textContent = 'Error reading file ❌';
                    this.showToast('❌ Error reading file', 'error');
                };
                reader.readAsText(file);
            }

            processWordContent(content) {
                // Clean document content from metadata, encryption data, and formatting artifacts
                let cleanContent = content
                    // Remove meta data patterns
                    .replace(/Normal text|Heading[1-6]/g, '')
                    .replace(/URL:\s*http[^\s]+/g, '')
                    .replace(/Meta Title:[^\n]+/g, '')
                    .replace(/Meta Description:[^\n]+/g, '')
                    // Remove document formatting artifacts
                    .replace(/^[^[]*(?=\[)/s, '') // Remove everything before first section marker
                    .replace(/\s+/g, ' ') // Normalize whitespace
                    // Add proper line breaks for sections
                    .replace(/\[([A-Z_\s]+)\]/g, '\n\n[$1]\n')
                    // Add line breaks after sentences for readability
                    .replace(/([.!?])\s*([A-Z][a-z])/g, '$1\n$2')
                    // Clean up extra whitespace
                    .replace(/\n{3,}/g, '\n\n')
                    .trim();
                
                // Ensure content starts with a section marker
                if (!cleanContent.startsWith('[')) {
                    const firstSectionMatch = cleanContent.match(/\[([A-Z_\s]+)\]/);
                    if (firstSectionMatch) {
                        const sectionIndex = cleanContent.indexOf(firstSectionMatch[0]);
                        cleanContent = cleanContent.substring(sectionIndex);
                    }
                }
                
                return cleanContent;
            }

            formatFileSize(bytes) {
                if (bytes === 0) return '0 Bytes';
                const k = 1024;
                const sizes = ['Bytes', 'KB', 'MB', 'GB'];
                const i = Math.floor(Math.log(bytes) / Math.log(k));
                return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
            }

            handleContentChange() {
                const content = this.inputContent.value.trim();
                const hasContent = content.length > 0;
                this.processBtn.disabled = !hasContent;
                
                if (hasContent) {
                    // Update stats
                    const lines = content.split('\n').length;
                    const words = content.split(/\s+/).length;
                    this.lineCount.textContent = lines;
                    this.wordCount.textContent = words;
                    this.statsPanel.style.display = 'block';
                    
                    // Auto-detect sections
                    const detectedSections = this.processor.detectSections(content);
                    this.updateDetectedSections(detectedSections);
                    
                    if (detectedSections.length > 0) {
                        this.statusText.innerHTML = `✅ Content ready - ${detectedSections.length} sections detected`;
                    } else {
                        this.statusText.innerHTML = '⚠️ No valid sections detected - check format';
                    }
                } else {
                    this.detectedSections.style.display = 'none';
                    this.statsPanel.style.display = 'none';
                    this.statusText.textContent = 'Upload a Word document or paste content to get started';
                }
            }

            updateDetectedSections(sections) {
                if (sections.length === 0) {
                    this.detectedSections.style.display = 'none';
                    return;
                }

                this.detectedSections.style.display = 'block';
                this.sectionCount.textContent = sections.length;
                this.sectionTags.innerHTML = '';
                
                // Show all supported sections
                const allSections = ['HERO', 'SERVICES_GRID', 'SERVICES_ACCORDION', 'FAQ', 'CTA_SIMPLE', 'PROCESS', 'TECHNOLOGY', 'INDUSTRIES', 'PORTFOLIO', 'TESTIMONIAL', 'BENEFITS'];
                
                allSections.forEach(section => {
                    const tag = document.createElement('span');
                    tag.className = 'section-tag';
                    
                    const isFound = sections.some(s => s.includes(section) || section.includes(s));
                    if (!isFound) {
                        tag.className += ' not-found';
                    }
                    
                    const check = document.createElement('span');
                    check.className = 'check';
                    check.textContent = isFound ? '✓' : '○';
                    
                    tag.appendChild(check);
                    tag.appendChild(document.createTextNode(section));
                    this.sectionTags.appendChild(tag);
                });
            }

            async processContent() {
                const content = this.inputContent.value.trim();

                if (!content) {
                    this.showToast('Please provide content to process', 'error');
                    return;
                }

                this.statusText.innerHTML = '<span class="loading"></span> Processing content with AI...';
                this.processBtn.disabled = true;
                this.processIcon.textContent = '⏳';

                try {
                    // Process with enhanced AI engine
                    const result = await this.processor.processContent(content);
                    
                    if (result.success) {
                        this.generatedCode = result.html;
                        this.outputCode.value = result.html;
                        this.copyBtn.disabled = false;
                        this.downloadBtn.disabled = false;
                        
                        this.statusText.innerHTML = `<span class="success">✅</span> Generated ${result.sectionsGenerated.length} sections successfully`;
                        this.showToast(`🎉 Successfully generated ${result.sectionsGenerated.length} HTML sections!`, 'success');
                    } else {
                        this.statusText.innerHTML = `<span class="error">❌</span> Processing failed`;
                        this.showToast(`❌ Error: ${result.error}`, 'error');
                    }
                } catch (error) {
                    this.statusText.innerHTML = `<span class="error">❌</span> Processing failed`;
                    this.showToast(`❌ Error: ${error.message}`, 'error');
                } finally {
                    this.processBtn.disabled = false;
                    this.processIcon.textContent = '⚡';
                }
            }

            formatContent() {
                const content = this.inputContent.value;
                if (!content.trim()) return;
                
                // Format content for better readability
                const formatted = content
                    .replace(/\[([A-Z_\s]+)\]/g, '\n\n[$1]\n')
                    .replace(/([.!?])\s*([A-Z][a-z])/g, '$1\n$2')
                    .replace(/\n{3,}/g, '\n\n')
                    .trim();
                
                this.inputContent.value = formatted;
                this.handleContentChange();
                this.showToast('📝 Content formatted!', 'success');
            }

            clearAll() {
                this.inputContent.value = '';
                this.outputCode.value = '';
                this.fileInfo.style.display = 'none';
                this.detectedSections.style.display = 'none';
                this.statsPanel.style.display = 'none';
                this.currentFile = null;
                this.generatedCode = '';
                this.fileInput.value = '';
                
                this.processBtn.disabled = true;
                this.copyBtn.disabled = true;
                this.downloadBtn.disabled = true;
                
                this.statusText.textContent = 'Upload a Word document or paste content to get started';
                this.showToast('🗑️ All content cleared', 'success');
            }

            copyCode() {
                if (!this.generatedCode) return;
                
                navigator.clipboard.writeText(this.generatedCode).then(() => {
                    this.showToast('📋 Code copied to clipboard!', 'success');
                }).catch(() => {
                    this.outputCode.select();
                    document.execCommand('copy');
                    this.showToast('📋 Code copied to clipboard!', 'success');
                });
            }

            downloadCode() {
                if (!this.generatedCode) return;
                
                const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
                const filename = `generated-sections-${timestamp}.html`;
                
                const blob = new Blob([this.generatedCode], { type: 'text/html' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                this.showToast(`💾 HTML file downloaded: ${filename}`, 'success');
            }

            showToast(message, type = 'info') {
                const toast = document.createElement('div');
                toast.className = `toast ${type}`;
                toast.textContent = message;
                document.body.appendChild(toast);
                
                setTimeout(() => {
                    toast.remove();
                }, 4000);
            }
        }

        // Initialize Enhanced IDE
        document.addEventListener('DOMContentLoaded', () => {
            new EnhancedIDEInterface();
        });
    </script>
</body>
</html>
```

This file contains the complete web IDE HTML code from your project for backup and reference purposes.