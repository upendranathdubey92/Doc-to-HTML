#!/usr/bin/env python3
"""
Parse the real document format and convert to structured format
"""

import re

def parse_real_document_format(content):
    """Parse the continuous text format from Word documents"""
    
    # First, split by section markers
    sections = {}
    
    # Find all section markers and their positions
    section_pattern = r'\[([A-Z_\s]+)\]'
    matches = list(re.finditer(section_pattern, content))
    
    for i, match in enumerate(matches):
        section_name = match.group(1).strip()
        start_pos = match.end()
        
        # Find the end position (next section or end of content)
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)
        
        # Extract section content
        section_content = content[start_pos:end_pos].strip()
        
        # Parse the section content based on its type
        parsed_content = parse_section_content(section_name, section_content)
        sections[section_name] = parsed_content
    
    return sections

def parse_section_content(section_name, content):
    """Parse content based on section type"""
    parsed = {}
    
    if section_name == 'HERO':
        return parse_hero_section(content)
    elif section_name == 'SERVICES GRID':
        return parse_services_grid(content)
    elif section_name == 'SERVICES_ACCORDION':
        return parse_services_accordion(content)
    elif section_name == 'CTA_SIMPLE' or section_name == 'CTA SIMPLE':
        return parse_cta_simple(content)
    elif section_name == 'PORTFOLIO':
        return parse_portfolio(content)
    elif section_name == 'TESTIMONIAL':
        return parse_testimonial(content)
    elif section_name == 'BENEFITS':
        return parse_benefits(content)
    elif section_name == 'CONTENT_FORM':
        return parse_content_form(content)
    elif section_name == 'PROCESS':
        return parse_process(content)
    elif section_name == 'TECHNOLOGY':
        return parse_technology(content)
    elif section_name == 'INDUSTRIES':
        return parse_industries(content)
    elif section_name == 'FAQ':
        return parse_faq(content)
    else:
        # Generic parsing
        parsed['raw_content'] = content
        return parsed

def parse_hero_section(content):
    """Parse HERO section"""
    parsed = {}
    
    # Split content into sentences/parts
    parts = content.split('The result?')
    if len(parts) >= 2:
        main_part = parts[0].strip()
        bullets_part = parts[1].strip()
        
        # Extract title (first sentence/part)
        sentences = main_part.split('.')
        if sentences:
            parsed['main_heading'] = sentences[0].strip()
            parsed['description'] = '. '.join(sentences[1:]).strip()
        
        # Extract bullet points (they usually start with capital letters)
        bullet_lines = [line.strip() for line in bullets_part.split('.') if line.strip() and len(line.strip()) > 10]
        parsed['bullet_points'] = bullet_lines[:4]  # Take first 4 as bullets
    else:
        # Fallback parsing
        lines = content.split('.')
        parsed['main_heading'] = lines[0].strip() if lines else "Service Title"
        parsed['description'] = '. '.join(lines[1:]).strip() if len(lines) > 1 else "Service description"
        parsed['bullet_points'] = []
    
    # Set defaults
    parsed['form_heading'] = 'Dream It, We Build It'
    parsed['form_button_text'] = 'Book Your Free Consultation'
    
    return parsed

def parse_services_grid(content):
    """Parse SERVICES GRID section"""
    parsed = {}
    
    # Find the main title and description
    lines = content.split('.')
    parsed['main_heading'] = lines[0].strip() if lines else "Our Services"
    
    # Look for description after title
    desc_start = content.find(parsed['main_heading']) + len(parsed['main_heading'])
    desc_part = content[desc_start:desc_start + 200].strip()
    parsed['description'] = desc_part.split('.')[0] + '.' if desc_part else "Our service offerings"
    
    # Extract services (look for patterns like "ServiceName ServiceDescription")
    services = []
    
    # Common service indicators
    service_keywords = [
        'Technology & Architecture Consulting',
        'UI/UX & Performance Optimization',
        'Modernization & Legacy System Assessment',
        'Code Audits & Quality Assurance',
        'Product Strategy & MVP Scoping',
        'Third-Party Integration Consulting'
    ]
    
    for keyword in service_keywords:
        if keyword in content:
            start_pos = content.find(keyword)
            # Get description after the service name
            after_title = content[start_pos + len(keyword):start_pos + len(keyword) + 300]
            description = after_title.split('.')[0] + '.' if after_title else "Service description"
            
            services.append({
                'title': keyword,
                'description': description.strip()
            })
    
    parsed['services'] = services[:6]  # Limit to 6 services
    return parsed

def parse_services_accordion(content):
    """Parse SERVICES_ACCORDION section"""
    parsed = {}
    
    lines = content.split('.')
    parsed['main_heading'] = lines[0].strip() if lines else "Our Services"
    parsed['description'] = lines[1].strip() if len(lines) > 1 else "Service description"
    
    # Extract services
    services = []
    service_keywords = [
        'Security & Compliance Advisory',
        'Cloud & Infrastructure Planning'
    ]
    
    for keyword in service_keywords:
        if keyword in content:
            start_pos = content.find(keyword)
            after_title = content[start_pos + len(keyword):start_pos + len(keyword) + 200]
            description = after_title.split('.')[0] + '.' if after_title else "Service description"
            
            services.append({
                'title': keyword,
                'description': description.strip()
            })
    
    parsed['services'] = services
    return parsed

def parse_portfolio(content):
    """Parse PORTFOLIO section"""
    return {'main_heading': 'Portfolio', 'description': 'Our recent projects'}

def parse_testimonial(content):
    """Parse TESTIMONIAL section"""
    return {'main_heading': 'Testimonials', 'testimonial_text': content[:200]}

def parse_benefits(content):
    """Parse BENEFITS section"""
    return {'main_heading': 'Benefits', 'description': content[:100]}

def parse_content_form(content):
    """Parse CONTENT_FORM section"""
    return {'main_heading': 'Contact Us', 'content': content[:200]}

def parse_cta_simple(content):
    """Parse CTA_SIMPLE section"""
    parsed = {}
    
    # Split by question mark to separate heading and description
    parts = content.split('?')
    if len(parts) >= 2:
        parsed['main_heading'] = (parts[0] + '?').strip()
        parsed['description'] = parts[1].strip().split('.')[0] + '.' if parts[1].strip() else "Let us help you"
    else:
        lines = content.split('.')
        parsed['main_heading'] = lines[0].strip() if lines else "Ready to Get Started?"
        parsed['description'] = lines[1].strip() if len(lines) > 1 else "Let us help you"
    
    # Look for button text (usually at the end)
    words = content.split()
    if len(words) > 3:
        # Button text is often the last few words
        parsed['button_text'] = ' '.join(words[-4:]) if len(words) >= 4 else "Get Started"
    else:
        parsed['button_text'] = "Get Started"
    
    return parsed

def parse_faq(content):
    """Parse FAQ section"""
    parsed = {}
    
    # Extract title
    lines = content.split('?')
    parsed['main_heading'] = lines[0] + '?' if lines else "Frequently Asked Questions"
    
    # Find Q&A patterns
    faqs = []
    
    # Look for question patterns
    questions_text = content
    
    # Split by common question words
    potential_questions = []
    for part in questions_text.split('?'):
        if len(part.strip()) > 10:
            potential_questions.append(part.strip() + '?')
    
    # Take first few as actual Q&As
    faq_pairs = []
    for i, q in enumerate(potential_questions[:6]):  # Limit to 6 FAQs
        if i + 1 < len(potential_questions):
            answer = potential_questions[i + 1].replace('?', '').strip()
            faq_pairs.append({
                'question': q,
                'answer': answer[:200] + '...' if len(answer) > 200 else answer
            })
    
    parsed['faqs'] = faq_pairs
    return parsed

def parse_process(content):
    """Parse PROCESS section"""
    parsed = {}
    
    lines = content.split('.')
    parsed['main_heading'] = lines[0].strip() if lines else "Our Process"
    parsed['description'] = lines[1].strip() if len(lines) > 1 else "How we work"
    
    # Look for step patterns
    steps = []
    
    # Common step indicators
    step_patterns = [
        'Discovery', 'Analysis', 'Planning', 'Design', 'Development', 
        'Testing', 'Deployment', 'Launch', 'Support'
    ]
    
    for i, pattern in enumerate(step_patterns[:6], 1):
        if pattern in content:
            start_pos = content.find(pattern)
            description = content[start_pos:start_pos + 150].split('.')[0]
            steps.append({
                'title': pattern,
                'description': description.strip()
            })
    
    parsed['steps'] = steps
    return parsed

def parse_technology(content):
    """Parse TECHNOLOGY section"""
    parsed = {}
    
    lines = content.split('.')
    parsed['main_heading'] = lines[0].strip() if lines else "Technology Stack"
    parsed['description'] = lines[1].strip() if len(lines) > 1 else "Technologies we use"
    
    # Default tech stack for web development
    parsed['technologies'] = [
        'React', 'Node.js', 'Python', 'Laravel', 'MySQL', 'PostgreSQL', 
        'AWS', 'Docker', 'JavaScript', 'PHP'
    ]
    
    return parsed

def parse_industries(content):
    """Parse INDUSTRIES section"""
    parsed = {}
    
    lines = content.split('.')
    parsed['main_heading'] = lines[0].strip() if lines else "Industries We Serve"
    parsed['description'] = lines[1].strip() if len(lines) > 1 else "We serve various industries"
    
    return parsed

def main():
    # Read the extracted content
    with open('/home/sotsys-252/Desktop/page-content-update/extracted_content.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Parsing real document format...")
    sections = parse_real_document_format(content)
    
    print(f"✅ Found {len(sections)} sections:")
    for section_name in sections.keys():
        print(f"   📄 {section_name}")
    
    # Convert to structured format
    structured_content = []
    
    for section_name, section_data in sections.items():
        structured_content.append(f"[{section_name}]")
        
        if section_name == 'HERO':
            structured_content.append(f"Heading: {section_data.get('main_heading', 'Title')}")
            structured_content.append(f"Description: {section_data.get('description', 'Description')}")
            for i, bullet in enumerate(section_data.get('bullet_points', []), 1):
                structured_content.append(f"Bullet {i}: {bullet}")
            structured_content.append(f"Form Heading: {section_data.get('form_heading', 'Contact Us')}")
            structured_content.append(f"Form Button: {section_data.get('form_button_text', 'Get Started')}")
            
        elif section_name == 'FAQ':
            structured_content.append(f"Heading: {section_data.get('main_heading', 'FAQ')}")
            for i, faq in enumerate(section_data.get('faqs', []), 1):
                structured_content.append(f"Question {i}: {faq.get('question', 'Question?')}")
                structured_content.append(f"Answer {i}: {faq.get('answer', 'Answer.')}")
                
        elif section_name in ['CTA_SIMPLE', 'CTA SIMPLE']:
            structured_content.append(f"Heading: {section_data.get('main_heading', 'Ready?')}")
            structured_content.append(f"Description: {section_data.get('description', 'Description')}")
            structured_content.append(f"Button Text: {section_data.get('button_text', 'Get Started')}")
            
        elif section_name == 'PROCESS':
            structured_content.append(f"Heading: {section_data.get('main_heading', 'Our Process')}")
            structured_content.append(f"Description: {section_data.get('description', 'Process description')}")
            for i, step in enumerate(section_data.get('steps', []), 1):
                structured_content.append(f"Step {i}: {step.get('title', 'Step')}")
                structured_content.append(f"Step Description {i}: {step.get('description', 'Description')}")
                
        elif section_name == 'TECHNOLOGY':
            structured_content.append(f"Heading: {section_data.get('main_heading', 'Technology')}")
            structured_content.append(f"Description: {section_data.get('description', 'Tech we use')}")
            structured_content.append(f"Technologies: {', '.join(section_data.get('technologies', []))}")
            
        elif section_name == 'INDUSTRIES':
            structured_content.append(f"Heading: {section_data.get('main_heading', 'Industries')}")
            structured_content.append(f"Description: {section_data.get('description', 'Industries we serve')}")
        
        structured_content.append("")  # Add blank line between sections
    
    # Save structured format
    output_path = '/home/sotsys-252/Desktop/page-content-update/structured_content.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(structured_content))
    
    print(f"💾 Structured content saved to: {output_path}")
    print(f"🎯 This format can now be used with the web IDE!")

if __name__ == "__main__":
    main()