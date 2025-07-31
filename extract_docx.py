#!/usr/bin/env python3
"""
Extract text content from Word document to understand the real format
"""

import sys
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    """Extract text content from .docx file"""
    try:
        # Open the .docx file as a zip
        with zipfile.ZipFile(docx_path, 'r') as docx:
            # Read the main document XML
            xml_content = docx.read('word/document.xml')
            
        # Parse the XML
        root = ET.fromstring(xml_content)
        
        # Define namespace
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        # Extract all text elements
        text_elements = []
        for text_elem in root.findall('.//w:t', namespace):
            if text_elem.text:
                text_elements.append(text_elem.text)
        
        # Join all text
        full_text = ''.join(text_elements)
        
        # Split into lines and clean up
        lines = []
        current_line = ""
        
        for char in full_text:
            if char == '\n' or char == '\r':
                if current_line.strip():
                    lines.append(current_line.strip())
                current_line = ""
            else:
                current_line += char
        
        if current_line.strip():
            lines.append(current_line.strip())
        
        return lines
        
    except Exception as e:
        print(f"Error extracting text: {e}")
        return []

def main():
    docx_path = "/home/sotsys-252/Downloads/Content File- Web Development Consulting.docx"
    
    print("📄 Extracting text from Word document...")
    lines = extract_text_from_docx(docx_path)
    
    if not lines:
        print("❌ Failed to extract text")
        return
    
    print(f"✅ Extracted {len(lines)} lines of text")
    print("="*60)
    
    # Print first 50 lines to see the structure
    for i, line in enumerate(lines[:50], 1):
        print(f"{i:3d}: {line}")
    
    if len(lines) > 50:
        print(f"\n... and {len(lines) - 50} more lines")
    
    # Save to text file for analysis
    output_path = "/home/sotsys-252/Desktop/page-content-update/extracted_content.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')
    
    print(f"\n📁 Full content saved to: {output_path}")

if __name__ == "__main__":
    main()