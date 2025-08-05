#!/usr/bin/env python3
"""
DOCX Content Update Tool
Processes extracted docx content and generates HTML sections
"""

import re
import sys
import os

class DocxContentTool:
    def __init__(self):
        """Initialize the tool"""
        pass

    def parse_docx_content(self, content_text):
        """Parse the extracted docx content into sections"""
        lines = content_text.strip().split('\n')
        sections = {}
        current_section = None
        current_content = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check for section markers
            if line.startswith('[') and line.endswith(']'):
                # Save previous section
                if current_section and current_content:
                    sections[current_section] = '\n'.join(current_content)
                
                # Start new section
                current_section = line[1:-1]  # Remove brackets
                current_content = []
                continue
            
            # Add line to current section
            if current_section:
                current_content.append(line)
        
        # Save last section
        if current_section and current_content:
            sections[current_section] = '\n'.join(current_content)
        
        return sections

    def generate_hero_html(self, content):
        """Generate hero section HTML from docx content"""
        # Split by actual line breaks to preserve spacing
        all_lines = content.split('\n')
        lines = [line.strip() for line in all_lines if line.strip()]
        
        # Parse content
        heading = lines[0] if lines else "Service Title"
        current_index = 1
        
        description = ''
        bullet_intro = ''
        bullet_lines = []
        
        # Find where explicit bullets start (WPS style with symbols)
        bullet_start_index = -1
        for i in range(current_index, len(lines)):
            line = lines[i]
            if re.match(r'^[●\-\*•‑]\s*', line) or re.match(r'^\d+[\.\)]\s+', line):
                bullet_start_index = i
                break
        
        # If explicit bullets found (WPS style)
        if bullet_start_index != -1:
            # Process lines before bullets
            description_lines = lines[current_index:bullet_start_index]
            
            if len(description_lines) > 1:
                # Check if last line before bullets looks like an intro title
                last_line = description_lines[-1]
                is_intro_title = (
                    len(last_line) < 50 and 
                    (last_line.endswith('-') or last_line.endswith(':') or last_line.endswith('?') or 
                     not last_line.endswith('.') and not last_line.endswith(',') and not last_line.endswith(';'))
                )
                
                if is_intro_title:
                    description = ' '.join(description_lines[:-1])
                    bullet_intro = last_line
                else:
                    description = ' '.join(description_lines)
            else:
                description = ' '.join(description_lines)
            
            # Extract explicit bullets
            for line in lines[bullet_start_index:]:
                if re.match(r'^[●\-\*•‑]\s*', line) or re.match(r'^\d+[\.\)]\s+', line):
                    clean_bullet = re.sub(r'^[●\-\*•‑]\s*', '', line).strip()
                    clean_bullet = re.sub(r'^\d+[\.\)]\s+', '', clean_bullet).strip()
                    # Handle bold formatting in bullet points
                    if ':' in clean_bullet:
                        parts = clean_bullet.split(':', 1)
                        if len(parts) == 2:
                            bullet_lines.append(f"<strong>{parts[0]}:</strong>{parts[1]}")
                        else:
                            bullet_lines.append(clean_bullet)
                    else:
                        bullet_lines.append(clean_bullet)
        else:
            # No explicit bullets found - check for Google Docs style lists
            description_lines = lines[current_index:]
            
            # Look for bullet intro line (like "How We Help You-")
            intro_line_index = -1
            for i in range(len(description_lines)):
                line = description_lines[i]
                # Line that ends with dash/colon or is short and followed by structured content
                if (len(line) < 50 and 
                    (line.endswith('-') or line.endswith(':') or line.endswith('?')) and
                    i < len(description_lines) - 2):  # Must have at least 2 lines after it
                    intro_line_index = i
                    break
            
            if intro_line_index != -1:
                # We found an intro line, check if lines after it look like list items
                lines_after_intro = description_lines[intro_line_index + 1:]
                
                # Check if these lines look like list items (Google Docs style)
                likely_bullets = []
                for line in lines_after_intro:
                    trimmed = line.strip()
                    if (trimmed and 
                        len(trimmed) > 10 and  # Not too short
                        len(trimmed) < 200 and  # Not too long
                        re.match(r'^[A-Z]', trimmed) and  # Starts with capital
                        (trimmed.endswith('.') or '.' not in trimmed or len(trimmed.split('.')) <= 2)):  # Complete thought
                        likely_bullets.append(trimmed)
                
                # If we have 2+ structured lines after intro, treat them as bullets
                if len(likely_bullets) >= 2:
                    description = ' '.join(description_lines[:intro_line_index])
                    bullet_intro = description_lines[intro_line_index]
                    bullet_lines = likely_bullets
                else:
                    # Not enough structured content, treat all as description
                    description = ' '.join(description_lines)
            else:
                # No intro line found, treat all as description
                description = ' '.join(description_lines)
        
        # Create bullet points HTML
        bullet_html = ""
        for bullet in bullet_lines:
            bullet_html += f"    <li>{bullet}</li>\n"
        
        # Add bullet intro HTML if it exists
        bullet_intro_html = f'<p class="fonts-18 mb-2 font-weight-bold">{bullet_intro}</p>' if bullet_intro else ''
        
        hero_html = f"""<!-- HERO -->
<section class="pt70 pb40 hero-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-7 col-md-12 banner-text">
<nav aria-label="breadcrumbs" class="rank-math-breadcrumb mb-3 mt-3"><p><a href="/" class="local" style="text-decoration: unset;">Home</a><span class="separator"> &gt; </span><a href="/services/" class="local" style="text-decoration: unset;">Services</a><span class="separator"> &gt; </span><span class="last">{heading}</span></p></nav>
<h1 class="fonts-45 mb-3 font-weight-bold">{heading}</h1>
<p class="fonts-18 mb-3">{description}</p>
{bullet_intro_html}<ul class="bullet mb-5 fonts-18">
{bullet_html.rstrip()}
</ul>

<div class="rating-section d-flex"><a href="https://goo.gl/maps/1JSqiZssNiDHAppx8" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/google-rating.svg" alt="Google" width="97" height="56" /></a>
<a href="https://clutch.co/profile/space-o-technologies#reviews" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/clutch-rating.svg" alt="Clutch" width="99" height="56" /></a>
<a href="https://www.goodfirms.co/company/space-o-technologies#reviews" target="_blank" rel="noopener"><img src="/wp-content/uploads/2023/08/goodfirm-rating.svg" alt="GoodFirms" width="135" height="56" /></a></div>
</div>
<div class="col-lg-5 col-md-12 text-form-section">
<div class="homen_form">
<p class="fonts-24 font-weight-bold mt-0 mb-2 text-center line-height-1">Dream It, We Build It</p>
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
<!-- HERO END -->

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
</section>"""
        
        return hero_html

    def generate_services_grid_html(self, content):
        """Generate services grid HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # First line is title, second is description
        title = lines[0] if lines else "Our Services"
        description = lines[1] if len(lines) > 1 else "Professional services"
        
        # Parse services - they come in groups
        services = []
        current_service = {}
        i = 2
        
        while i < len(lines):
            line = lines[i]
            
            # Check if this is a new service title
            if not line.startswith('●') and (not current_service or current_service.get('description')):
                if current_service:
                    services.append(current_service)
                # Remove numbers from beginning of titles (1. B2B Portal → B2B Portal)
                clean_title = line
                if re.match(r'^\d+\.\s+', line):
                    clean_title = re.sub(r'^\d+\.\s+', '', line)
                current_service = {'title': clean_title, 'description': '', 'points': []}
                i += 1
                # Next line should be description
                if i < len(lines) and not lines[i].startswith('●'):
                    current_service['description'] = lines[i]
                    i += 1
            elif line.startswith('●'):
                current_service['points'].append(line.replace('●', '').strip())
                i += 1
            else:
                i += 1
        
        # Add last service
        if current_service:
            services.append(current_service)
        
        # Define the service icons
        service_icons = [
            {'file': 'Architecture-and-Design-Consulting.svg', 'alt': 'Technology & Architecture Consulting'},
            {'file': 'ux-performance-optimization.svg', 'alt': 'UI/UX & Performance Optimization'},
            {'file': 'Legacy-App-Modernization.svg', 'alt': 'Modernization & Legacy System Assessment'},
            {'file': 'code-audits-quality-assurance.svg', 'alt': 'Code Audits & Quality Assurance'},
            {'file': 'MVP-Development.svg', 'alt': 'Product Strategy & MVP Scoping'},
            {'file': 'Third-party-Integrations.svg', 'alt': 'Third-Party Integration Consulting'}
        ]
        
        # Generate HTML
        services_html = ""
        for i, service in enumerate(services[:6]):  # Limit to 6 services
            points_html = ""
            for point in service.get('points', []):
                points_html += f"<li>{point}</li>\n"
            
            if points_html:
                points_html = f"<ul class=\"bullet fonts-14 mb-3\">\n{points_html}</ul>"
            
            icon_path = f"/wp-content/uploads/2023/09/{service_icons[i]['file']}" if i < 2 else f"/wp-content/uploads/2024/02/{service_icons[i]['file']}"
            if i == 1:
                icon_path = "/wp-content/uploads/2025/07/ux-performance-optimization.svg"
            elif i == 3:
                icon_path = "/wp-content/uploads/2025/07/code-audits-quality-assurance.svg"
            elif i == 5:
                icon_path = "/wp-content/uploads/2024/03/Third-party-Integrations.svg"
                
            services_html += f"""\n<div class="col-lg-4 col-md-6">
<div class="mad_service_box">
<img src="{icon_path}" alt="{service_icons[i]['alt'] if i < len(service_icons) else service['title']}" width="74" height="74" />
<h3 class="fonts-18 font-weight-semibold">{service['title']}</h3>
<p>{service.get('description', '')}</p>
{points_html}
</div>
</div>"""
        
        return f"""<!-- SERVICES_GRID -->
<section class="pt80 pb50 services-section bg-color">
<div class="container-xl">
<h2 class="fonts-40 text-center font-weight-bold mb-3 mxw-1000">{title}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
{services_html}
</div>
</div>
</section>
<!-- SERVICES_GRID END -->"""

    def generate_services_accordion_html(self, content):
        """Generate services accordion HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        services = []
        current_service = {}
        
        for line in lines:
            # Service titles - check if line doesn't start with bullet point
            if not line.startswith(('●', '•', 'Audit', 'Recommend', 'Secure', 'Apply', 'Design', 'Support', 'Plan')):
                if current_service:
                    services.append(current_service)
                current_service = {'title': line, 'description': '', 'points': []}
            elif line.startswith(('●', '•')):
                # Bullet points
                current_service['points'].append(line.replace('●', '').replace('•', '').strip())
            else:
                # First line after title is description
                if not current_service.get('description'):
                    current_service['description'] = line
                else:
                    current_service['points'].append(line)
        
        if current_service:
            services.append(current_service)
        
        # Service icons
        service_icons = [
            'security-compliance-advisory.svg',
            'cloud-infrastructure-planning.svg'
        ]
        
        accordion_html = ""
        for i, service in enumerate(services[:2]):  # Limit to 2 services as shown in example
            points_html = ""
            for point in service.get('points', []):
                points_html += f"<li>{point}</li>\n"
            
            if points_html:
                points_html = f"<ul class=\"bullet fonts-14 mb-3\">\n{points_html}</ul>"
            
            expanded = "show" if i == 0 else ""
            collapsed = "" if i == 0 else "collapsed"
            
            icon_file = service_icons[i] if i < len(service_icons) else f"service-{i+1}.svg"
            
            accordion_html += f"""<div class="card">
<div class="card-header">
<h3 class="card-link" data-toggle="collapse" href="#{['three', 'four'][i]}"><img src="/wp-content/uploads/2025/07/{icon_file}" width="34" height="34" alt="{service['title']}" class="left-icons">{service['title']}</h3>
<div id="{['three', 'four'][i]}" class="collapse" data-parent="#accordion">
<div class="card card-body">
<p>{service.get('description', '')}</p>
{points_html}
</div>
</div>
</div>
</div>
"""
        
        return f"""<!-- SERVICES_ACCORDION -->
<section class="techno-stack pb80 bg-color services-tab-new">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
{accordion_html}</div>
</div>
</div>
</div>
</section>
<!-- SERVICES_ACCORDION END -->"""

    def generate_cta_simple_html(self, content):
        """Generate CTA simple HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Get Started Today"
        description = lines[1] if len(lines) > 1 else "Contact us for more information"
        button_text = lines[2] if len(lines) > 2 else "Contact Us"
        
        return f"""<!-- CTA_SIMPLE -->
<section class="pt80 pb80 new-cta-section">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title mxw-1000">{heading}</p>
<p class="fonts-20 mxw-900">{description}</p>
</div>
<div class="col-md-12 text-center mt-4"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">{button_text}</button></div>
</div>
</div>
</div>
</section>
<!-- CTA_SIMPLE END -->"""

    def generate_portfolio_html(self, content):
        """Generate portfolio HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Our Portfolio"
        description = lines[1] if len(lines) > 1 else "Recent projects showcase"
        
        # Parse projects
        projects = []
        current_project = {}
        i = 2
        
        while i < len(lines):
            line = lines[i]
            # Project title comes first
            if not line.startswith(('We developed', 'We engineered', 'Check the')):
                if current_project and 'description' in current_project:
                    projects.append(current_project)
                    current_project = {}
                current_project['title'] = line
            # Description comes after title
            elif line.startswith(('We developed', 'We engineered')):
                current_project['description'] = line
            # Link text
            elif line.startswith('Check the'):
                current_project['link_text'] = line
            i += 1
        
        if current_project and 'description' in current_project:
            projects.append(current_project)
        
        # Project images
        project_images = [
            {'file': 'CCTV-Data-Management-Platform-for-Public-Safety.png', 'width': '600', 'height': '459'},
            {'file': 'Feature-Image-Web-Based-Field-Service-Management-Solution.jpg', 'width': '600', 'height': '459'},
            {'file': 'eCommerce-Marketplace-Development-for-Waste-Management-Equipment.jpg', 'width': '600', 'height': '459'}
        ]
        
        projects_html = ""
        for i, project in enumerate(projects[:3]):  # Limit to 3 projects
            order_class = "order-1" if i % 2 == 0 else "order-2"
            img_info = project_images[i] if i < len(project_images) else {'file': 'placeholder.jpg', 'width': '600', 'height': '459'}
            
            projects_html += f"""<div class="slider_projects {order_class}">
<div class="row vcenter-parent">
<div class="col-lg-6 col-12">
<div class="left_text">
<div class="slider-app-name">
<div class="top-heading">
<h3 class="fonts-26 mb-2 font-weight-bold">{project.get('title', 'Project Title')}</h3>
</div>
</div>
<p class="mb-3">{project.get('description', '')}</p>
<div class="keep-reading ml-2"><a class="btn-link-arrow btn-link-arrow-right" href="https://www.spaceotechnologies.com/project/"><span class="btn__label-wrapper">{project.get('link_text', 'Check the Project Details')}</span></a></div>
</div>
</div>
<div class="col-lg-6 col-12">
<img class="project-img" src="/wp-content/uploads/2025/{'06' if i == 0 else '01'}/{img_info['file']}" alt="{project.get('title', 'Project')}" width="{img_info['width']}" height="{img_info['height']}" class="alignnone size-full wp-image-192738" />
</div>
</div>
</div>\n"""
        
        # Add featured-in section
        featured_html = """<section class="featured-in pt80 pb80">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">Our Solutions Recognized & Featured In</h2>
<div class="brand-listing">
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/Tech-Crunch.svg" alt="Tech Crunch" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/The-Guardian.svg" alt="The Guardian" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/Bloomberg.svg" alt="Bloomberg" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/BBC.svg" alt="BBC" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/Business-insider.svg" alt="Business insider" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="/wp-content/uploads/2023/08/The-Telegraph.svg" alt="The Telegraph" width="200" height="44"/>
</div>
</div>
</div>
</section>"""
        
        return f"""<!-- PORTFOLIO -->
<div class="our-work pt70 pb70 bg-color">
<div class="container-xl">
<div class="text-center">
<h2 class="fonts-40 text-center font-weight-bold mb-2 mxw-900">{heading}</h2>
<p class="fonts-18 text-center mb-3 mxw-900">{description}</p>
</div>
{projects_html}</div>
</div>
<!-- PORTFOLIO END -->\n\n{featured_html}"""

    def generate_benefits_html(self, content):
        """Generate benefits section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Key Benefits of Web Development Consulting Services"
        description = lines[1] if len(lines) > 1 else "Partnering with a web development consulting company offers more than just technical guidance."
        
        # Parse benefits - robust detection including numbered format
        benefits = []
        current_benefit = None
        
        all_lines = content.split('\n')
        
        for i, line in enumerate(lines[2:], start=2):
            # CRITICAL: Check if line starts with a number (1., 2., etc.)
            numbered_match = re.match(r'^(\d+)\.\s+(.+)', line)
            is_numbered_title = bool(numbered_match)
            
            # Find original line index to check for empty lines
            original_line_idx = None
            for j, orig_line in enumerate(all_lines):
                if orig_line.strip() == line:
                    original_line_idx = j
                    break
            
            # Check if separated by empty lines
            is_after_empty = original_line_idx > 0 and all_lines[original_line_idx - 1].strip() == ''
            
            # Better title detection - now includes numbered format
            is_short = len(line) < 80  # Increased to handle numbered titles
            is_title_case = re.match(r'^[A-Z][a-zA-Z\s&-]*[a-zA-Z]$', line) or re.match(r'^[A-Z][a-zA-Z]*$', line)
            no_end_punct = not line.endswith(('.', '!', '?'))
            is_first_benefit = i == 2
            
            # Smart title detection based on structure
            next_line_index = i + 1 if i < len(lines) - 3 else None
            has_long_text_after = False
            if next_line_index and next_line_index < len(lines):
                next_line = lines[next_line_index].strip()
                has_long_text_after = len(next_line) > 100
            
            # A line is a benefit title if:
            # 1. It starts with a number (1., 2., etc.)
            # 2. It's the first content after description
            # 3. It's short AND followed by longer text
            # 4. It's after empty line(s) and is relatively short
            is_benefit_title = is_numbered_title or is_first_benefit or (is_short and has_long_text_after) or (is_short and is_after_empty and i > 2)
            
            if is_benefit_title:
                # Save previous benefit
                if current_benefit:
                    benefits.append(current_benefit)
                # Start new benefit
                # If it's a numbered title, extract just the title part
                if is_numbered_title and numbered_match:
                    title = numbered_match.group(2)  # Get title without number
                else:
                    title = line
                current_benefit = {'title': title, 'description': ''}
            else:
                # Add to description
                if current_benefit:
                    if current_benefit['description']:
                        current_benefit['description'] += ' ' + line
                    else:
                        current_benefit['description'] = line
                else:
                    # Check if this might be a numbered title as first line
                    first_line_numbered = re.match(r'^(\d+)\.\s+(.+)', line)
                    if first_line_numbered:
                        current_benefit = {'title': first_line_numbered.group(2), 'description': ''}
                    else:
                        current_benefit = {'title': line, 'description': ''}
        
        # Add last benefit
        if current_benefit:
            benefits.append(current_benefit)
        
        # Define the 6 benefit icons and their slugs
        benefit_icons = [
            'eliminate-performance-issues',
            'boost-conversion-rates', 
            'clean-up-technical-debt',
            'accelerate-development-timelines',
            'maximize-development-roi',
            'execute-risk-free-redesigns'
        ]
        
        benefits_html = ""
        for i, benefit in enumerate(benefits[:6]):  # Limit to 6 benefits
            icon_slug = benefit_icons[i] if i < len(benefit_icons) else f'benefit-{i+1}'
            description_html = f'<p class="fonts-14">{benefit.get("description", "")}</p>' if benefit.get('description') else ''
            benefits_html += f"""    <div class="col-lg-4 col-md-6">
        <div class="mad_service_box text-center">
            <img src="/wp-content/uploads/2025/07/{icon_slug}.svg" alt="{benefit['title']}" width="74" height="74" />
            <h3 class="fonts-18 font-weight-semibold">{benefit['title']}</h3>
            {description_html}
        </div>
    </div>"""
        
        return f"""<section class="pt80 pb50 services-section">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3 mxw-1000">{heading}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
{benefits_html}
</div>
</div>
</section>"""

    def generate_testimonial_html(self, content):
        """Generate testimonial section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "What Our Clients Say About Working With Us"
        
        # Parse testimonial content
        testimonial_text = ""
        author_name = ""
        author_title = ""
        
        for i, line in enumerate(lines[1:]):
            if line.startswith('View all') or line.startswith('View All'):
                break
            elif i == len(lines[1:]) - 1:  # Last line is usually the title
                author_title = line
            elif i == len(lines[1:]) - 2:  # Second to last is usually the name
                author_name = line
            else:
                testimonial_text += line + ' '
        
        testimonial_text = testimonial_text.strip()
        
        # Extract name from testimonial if pattern found
        import re
        name_match = re.search(r'^([A-Z]\. [A-Za-z]+)', testimonial_text.split('.')[-1].strip())
        if name_match:
            author_name = name_match.group(1)
            testimonial_text = testimonial_text.replace(author_name, '').strip()
        
        return f"""<div class="blog-testimonial pb80 pt80 bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">{heading}</h2>
<div class="row align-items-center customer-feedback">
<div class="col-lg-7 blog-testimonial-left">
<p class="description mb-0">{testimonial_text}</p>
<div class="users-feed-ibox d-flex flex-row">
<div class="userfedd-detbox justify-content-between">
<div class="d-flex align-items-center mb-2">
<p class="user-name">{author_name}</p>
<img src="/wp-content/uploads/2023/06/Rating.svg" alt="review-star" width="82" height="13" />
</div>
<p>{author_title}</p>
</div>
</div>
<div class="read_more">
<a class="btn-link-arrow btn-link-arrow-right" href="/company/client-testimonials/"><span class="btn__label-wrapper">View all Testimonials</span></a>
</div>
</div>
<div class="col-lg-5 right-img text-right"><img src="/wp-content/uploads/2025/07/{author_name.replace(' ', '-').replace('.', '')}.png" alt="{author_name}" width="434" height="402" /></div>
</div>
</div>
</div>"""

    def generate_benefits_two_html(self, content):
        """Generate benefits2 (Why Space-O) section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Why Choose Space-O Technologies"
        description = lines[1] if len(lines) > 1 else "Partner with us for expert web development consulting."
        
        # Parse benefits - they follow title/description pairs
        benefits = []
        i = 2  # Start after heading and description
        
        while i < len(lines):
            if i + 1 < len(lines):
                title = lines[i]
                benefit_desc = lines[i + 1]
                benefits.append({'title': title, 'description': benefit_desc})
                i += 2
            else:
                # Last item without description
                benefits.append({'title': lines[i], 'description': ''})
                i += 1
        
        benefits_html = ""
        for benefit in benefits[:6]:  # Limit to 6 benefits
            benefits_html += f"""    <div class="col-lg-4 col-md-6">
        <div class="mad_service_box">
            <h3 class="fonts-18 font-weight-semibold">{benefit['title']}</h3>
            {benefit.get('description', '')}
        </div>
    </div>
"""
        
        return f"""<section class="pt80 pb50 services-section practices-we-follow">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3">{heading}</h2>
<p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
<div class="row">
{benefits_html}</div>
</div>
</section>"""

    def generate_content_form_html(self, content):
        """Generate content with form section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Web Development Consulting to Future-Proof Your Digital Presence"
        
        # Parse main content and bullet points
        main_content = ""
        bullet_points = []
        bullet_section_title = ""
        in_bullets = False
        
        for line in lines[1:]:
            if line.endswith(':') and ('Challenge' in line or 'Address' in line or 'Help' in line):
                bullet_section_title = line
                in_bullets = True
                continue
            elif line.startswith('●'):
                bullet_points.append(line.replace('●', '').strip())
                in_bullets = True
            elif in_bullets and line.strip() == "":
                # Empty line might end bullet section
                continue
            elif not in_bullets:
                main_content += line + ' '
        
        main_content = main_content.strip()
        
        # Generate bullet points HTML
        bullet_html = ""
        if bullet_points:
            bullet_html = f"<strong>{bullet_section_title}</strong>\n<ul class=\"bullet fonts-14 mb-3\">\n"
            for bullet in bullet_points:
                # Split by colon to get title and description
                parts = bullet.split(':', 1)
                if len(parts) == 2:
                    bullet_html += f"<li><strong>{parts[0]}:</strong>{parts[1]}</li>\n"
                else:
                    bullet_html += f"<li>{bullet}</li>\n"
            bullet_html += "</ul>"
        
        return f"""<section class="pt80 pb80 text-form-section bg-color">
<div class="container-xl">
<div class="row">
<div class="col-lg-7 col-md-12 col-sm-12">
<h2 class="fonts-40 font-weight-bold text-left mb-4">{heading}</h2>
<p>{main_content}</p>
{bullet_html}
</div>
<div class="col-lg-5 col-md-12 col-sm-12 text-center">
<div class="homen_form">
<p class="fonts-24 font-weight-bold mt-0 mb-3 text-center line-height-1 pb-0">Talk to Our Experts Now</p>
<form id="other-form2" class="footer_form append-form blur-form" action="" method="post" name="popup-form" novalidate="">
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
<input id="submit" class="btn btn-pop mb0" name="submit" type="submit" value="Book Your Consultation Now" data-medium="S_2" />
</div>
</div>
</div>
</form>
</div>
</div>
</div>
</div>
</section>"""

    def generate_cta_two_html(self, content):
        """Generate CTA_TWO section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Parse content
        title = lines[0] if lines else "Ready to Build a Web Solution That Drives Results?"
        description = lines[1] if len(lines) > 1 else "Whether you're a startup or an enterprise, we offer fully customized web development services."
        
        # Parse stats (numbers and their descriptions)
        stats = []
        button_text = "Request a Free Proposal View Portfolio"
        
        i = 2
        while i < len(lines):
            line = lines[i].strip()
            if any(char.isdigit() for char in line) and len(line) < 10:  # This is a stat number
                stat_number = line
                stat_description = ""
                if i + 1 < len(lines) and not any(char.isdigit() for char in lines[i + 1]):
                    stat_description = lines[i + 1].strip()
                    i += 2
                else:
                    i += 1
                stats.append(f"{stat_number} {stat_description}")
            elif line.startswith(('Request', 'View')) or 'Request' in line:
                button_text = line
                i += 1
            else:
                i += 1
        
        # Generate stats HTML
        stats_html = ""
        stat_images = [
            "https://www.spaceotechnologies.com/wp-content/uploads/2025/06/Frame-1.svg",
            "/wp-content/uploads/2025/07/frameworks-tools-mastered.svg", 
            "/wp-content/uploads/2025/07/seo-mobile-optimized.svg",
            "/wp-content/uploads/2025/07/years-of-dev-expertise.svg"
        ]
        
        for i, stat in enumerate(stats[:4]):
            img_src = stat_images[i] if i < len(stat_images) else stat_images[0]
            stats_html += f"""    <div class="new-button-group-inner">
        <img src="{img_src}">
        <strong>{stat.split()[0]}</strong> {' '.join(stat.split()[1:])}
    </div>
"""
        
        return f"""<section class="pt50 pb80 new-cta-section">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title">{title}</p>
<p class="fonts-20 mxw-900">{description}</p>
</div>
<div class="new-button-group">
{stats_html}</div>
<div class="col-md-12 text-center mt-4 d-flex justify-content-center two-btn-group"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">Request a Free Proposal</button> <a class="btn btn-pop open-qouteform white-btn" href="/project/">View Portfolio</a></div>
</div>
</div>
</div>
</section>"""


    def generate_technology_html(self, content):
        """Generate technology stack section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Technology Stack"
        description = lines[1] if len(lines) > 1 else "Modern technologies we use."
        
        # Parse technology categories from content
        tech_categories = []
        current_category = None
        current_techs = []
        
        # Skip heading and description
        start_idx = 2 if len(lines) > 1 else 0
        
        for i in range(start_idx, len(lines)):
            line = lines[i]
            
            # Check if this is a category name (ends with ':')
            if line.endswith(':'):
                # Save previous category if exists
                if current_category and current_techs:
                    tech_categories.append({
                        'name': current_category,
                        'techs': current_techs
                    })
                
                current_category = line.replace(':', '').strip()
                current_techs = []
            else:
                # This is a technology item
                # Try to parse tech name and icon from the line
                tech_name = line.strip()
                
                # Map tech names to their icons
                tech_icons = {
                    'React': 'React.svg',
                    'React.js': 'React.svg',
                    'Vue.js': 'Vue-JS.svg',
                    'Angular': 'Angular.svg',
                    'Next.js': 'Next.js.svg',
                    'Nuxt.js': 'Nuxt.js.svg',
                    'Nuxt': 'Nuxt.js.svg',
                    'Ember.js': 'Ember.js.svg',
                    'TypeScript': 'typescript.svg',
                    'Tailwind CSS': 'Tailwind.svg',
                    'HTML': 'HTML.svg',
                    'CSS': 'CSS.svg',
                    'JavaScript': 'JavaScript.svg',
                    'Node.js': 'Node.js.svg',
                    'Python': 'python.svg',
                    'Django': 'Django.svg',
                    'PHP': 'php.svg',
                    'Laravel': 'Laravel.svg',
                    'Symfony': 'Symfony.svg',
                    'CodeIgniter': 'CodeIgniter.svg',
                    'Yii': 'Yii.svg',
                    'CakePHP': 'CakePHP.svg',
                    'Zend': 'Zend.svg',
                    'Zend Framework': 'Zend.svg',
                    'Ruby on Rails': 'ROR.svg',
                    '.NET Core': 'Microsoft_.NET_.svg',
                    'Microsoft .NET': 'Microsoft_.NET_.svg',
                    'Express': 'expressjs.svg',
                    'Express.js': 'expressjs.svg',
                    'PostgreSQL': 'Postgresql_elephant.svg',
                    'MongoDB': 'MongoDB.svg',
                    'MySQL': 'MySQL.svg',
                    'Redis': 'Redis.svg',
                    'Memcached': 'Memcached.svg',
                    'SQL': 'SQL.svg',
                    'NoSQL': 'NoSQL.svg',
                    'Firebase': 'Firebase.svg',
                    'Supabase': 'supabase.svg',
                    'AWS': 'AWS.svg',
                    'Google Cloud': 'Google-Cloud-Platform.svg',
                    'Google Cloud Platform': 'Google-Cloud-Platform.svg',
                    'Microsoft Azure': 'Microsoft-Azure.svg',
                    'Azure': 'Microsoft-Azure.svg',
                    'Docker': 'Docker.svg',
                    'Kubernetes': 'Kubernetes.svg',
                    'Heroku': 'Heroku.svg',
                    'Jenkins': 'Jenkins.svg',
                    'Vercel': 'vercel.svg',
                    'Git': 'Git.svg',
                    'Visual Studio Code': 'Visual-Studio-Code.svg',
                    'GraphQL': 'GraphQL.svg',
                    'Jest': 'Jest.svg',
                    'Cypress': 'Cypress.svg',
                    'Selenium': 'Selenium.svg',
                    'Mocha': 'Mocha.svg',
                    'WordPress': 'WordPress.svg',
                    'Drupal': 'Drupal.svg',
                    'Magento': 'Magento.svg',
                    'Joomla': 'Joomla.svg',
                    'TYPO3': 'TYPO3.svg',
                    'OpenAI': 'OpenAI.svg',
                    'ChatGPT': 'ChatGPT.svg',
                    'Whisper': 'Whisper.svg',
                    'Synthesia': 'Synthesia.svg',
                    'Prism': 'Prism.svg',
                    'Swift': 'Swift.svg',
                    'Xcode': 'Xcode.svg',
                    'Webflow': 'webflow.svg',
                    'Bubble': 'bubble.svg',
                    'Airtable': 'airtable.svg',
                    'Zapier': 'Zapier.svg',
                    'Notion': 'notion.svg',
                    'Strapi': 'strapi.svg',
                    'Figma': 'Figma.svg',
                    'Adobe Creative Suite': 'adobe-creative-suite.svg',
                    'Sketch': 'Sketch.svg',
                    'Framer': 'framer.svg',
                    'InVision': 'InVision.png'
                }
                
                # Get icon file name
                icon_file = tech_icons.get(tech_name, f"{tech_name.replace(' ', '-').lower()}.svg")
                
                if tech_name in tech_icons:
                    current_techs.append({
                        'name': tech_name,
                        'icon': icon_file
                    })
        
        # Add last category
        if current_category and current_techs:
            tech_categories.append({
                'name': current_category,
                'techs': current_techs
            })
        
        # If no categories were parsed, use default structure
        if not tech_categories:
            tech_categories = [
                {
                    'name': 'Frontend Technologies',
                    'techs': [
                        {'name': 'React', 'icon': 'React.svg'},
                        {'name': 'Vue.js', 'icon': 'Vue-JS.svg'},
                        {'name': 'Angular', 'icon': 'Angular.svg'},
                        {'name': 'Next.js', 'icon': 'Next.js.svg'},
                        {'name': 'TypeScript', 'icon': 'typescript.svg'},
                        {'name': 'Tailwind CSS', 'icon': 'Tailwind.svg'}
                    ]
                },
                {
                    'name': 'Backend Technologies',
                    'techs': [
                        {'name': 'Node.js', 'icon': 'Node.js.svg'},
                        {'name': 'Python', 'icon': 'python.svg'},
                        {'name': 'Django', 'icon': 'Django.svg'},
                        {'name': 'PHP', 'icon': 'php.svg'},
                        {'name': 'Laravel', 'icon': 'Laravel.svg'},
                        {'name': 'Ruby on Rails', 'icon': 'ROR.svg'},
                        {'name': '.NET Core', 'icon': 'Microsoft_.NET_.svg'},
                        {'name': 'Express.js', 'icon': 'expressjs.svg'}
                    ]
                },
                {
                    'name': 'Database',
                    'techs': [
                        {'name': 'PostgreSQL', 'icon': 'Postgresql_elephant.svg'},
                        {'name': 'MongoDB', 'icon': 'MongoDB.svg'},
                        {'name': 'MySQL', 'icon': 'MySQL.svg'},
                        {'name': 'Redis', 'icon': 'Redis.svg'},
                        {'name': 'Firebase', 'icon': 'Firebase.svg'},
                        {'name': 'Supabase', 'icon': 'supabase.svg'}
                    ]
                },
                {
                    'name': 'Cloud & DevOps',
                    'techs': [
                        {'name': 'AWS', 'icon': 'AWS.svg'},
                        {'name': 'Google Cloud', 'icon': 'Google-Cloud-Platform.svg'},
                        {'name': 'Microsoft Azure', 'icon': 'Microsoft-Azure.svg'},
                        {'name': 'Docker', 'icon': 'Docker.svg'},
                        {'name': 'Kubernetes', 'icon': 'Kubernetes.svg'},
                        {'name': 'Vercel', 'icon': 'vercel.svg'}
                    ]
                },
                {
                    'name': 'No-Code / Low-Code',
                    'techs': [
                        {'name': 'Webflow', 'icon': 'webflow.svg'},
                        {'name': 'Bubble', 'icon': 'bubble.svg'},
                        {'name': 'Airtable', 'icon': 'airtable.svg'},
                        {'name': 'Zapier', 'icon': 'Zapier.svg'},
                        {'name': 'Notion', 'icon': 'notion.svg'},
                        {'name': 'Strapi', 'icon': 'strapi.svg'}
                    ]
                },
                {
                    'name': 'Design & Tools',
                    'techs': [
                        {'name': 'Figma', 'icon': 'Figma.svg'},
                        {'name': 'Adobe Creative Suite', 'icon': 'adobe-creative-suite.svg'},
                        {'name': 'Sketch', 'icon': 'Sketch.svg'},
                        {'name': 'Framer', 'icon': 'framer.svg'},
                        {'name': 'InVision', 'icon': 'InVision.png'}
                    ]
                }
            ]
        
        tech_html = ""
        for category in tech_categories:
            tech_items = ""
            for tech in category['techs']:
                # Determine the correct upload path based on icon name and known patterns
                icon_path = f"/wp-content/uploads/2023/08/{tech['icon']}"
                
                # Special cases for different upload years
                if tech['name'] in ['Next.js', 'Tailwind CSS', 'Zapier']:
                    icon_path = f"/wp-content/uploads/2024/02/{tech['icon']}"
                elif tech['name'] == 'TypeScript':
                    icon_path = "/wp-content/uploads/2024/03/typescript.svg"
                elif tech['name'] == 'PHP':
                    icon_path = "/wp-content/uploads/2022/01/php.svg"
                elif tech['name'] in ['Supabase', 'Vercel', 'Webflow', 'Bubble', 'Airtable', 'Notion', 'Strapi', 'Framer', 'Adobe Creative Suite', 
                                     'Nuxt.js', 'Nuxt', 'HTML', 'CSS', 'JavaScript', 'Memcached', 'SQL', 'NoSQL', 'Heroku', 'Jenkins',
                                     'Git', 'Visual Studio Code', 'GraphQL', 'Jest', 'Cypress', 'Selenium', 'Mocha', 'OpenAI', 
                                     'ChatGPT', 'Whisper', 'Synthesia', 'Prism', 'Swift', 'Xcode']:
                    icon_path = f"/wp-content/uploads/2025/07/{tech['icon']}"
                elif tech['name'] in ['Google Cloud', 'Google Cloud Platform']:
                    icon_path = "/wp-content/uploads/2025/06/Google-Cloud-Platform.svg"
                elif tech['name'] == 'InVision':
                    icon_path = "/wp-content/uploads/2021/01/InVision.png"
                elif tech['name'] == 'Sketch':
                    icon_path = "/wp-content/uploads/2023/09/Sketch.svg"
                elif tech['name'] in ['Symfony', 'CodeIgniter', 'Yii', 'CakePHP', 'Zend', 'Zend Framework']:
                    icon_path = f"/wp-content/uploads/2023/08/{tech['icon']}"
                elif tech['name'] in ['WordPress', 'Drupal', 'Magento', 'Joomla', 'TYPO3']:
                    icon_path = f"/wp-content/uploads/2023/08/{tech['icon']}"
                elif tech['name'] == 'Ember.js':
                    icon_path = f"/wp-content/uploads/2023/08/{tech['icon']}"
                    
                tech_items += f'          <li><img src="{icon_path}" alt="{tech["name"]}" width="24" height="24"> {tech["name"]}</li>\n'
            
            tech_html += f"""  <div class="row">
    <div class="col-md-2">
      <div class="technology-name fonts-20">{category['name']}</div>
    </div>
    <div class="col-md-10">
      <ul class="technology-icon-wrapper">
{tech_items}        </ul>
    </div>
  </div>\n"""
        
        return f"""<div class="technology-stack pt80 pb60">
<div class="container-xl">
<div class="row">
<div class="col-md-12">
<h2 class="fonts-40 text-center font-weight-bold mxw-900">{heading}</h2>
<p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
</div>
</div>
<div class="technology-inner mt-4">
{tech_html}</div>
</div>
</div>"""

    def generate_industries_html(self, content):
        """Generate industries section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Industries We Serve"
        description = lines[1] if len(lines) > 1 else "We serve diverse industries with custom solutions."
        
        # Define industries with their icons
        industries = [
            {'name': 'Healthcare', 'icon': 'Healthcare.svg'},
            {'name': 'Real Estate', 'icon': 'Real-estate.svg'},
            {'name': 'Investment', 'icon': 'Investment.svg'},
            {'name': 'Insurance', 'icon': 'Insurance.svg'},
            {'name': 'eCommerce', 'icon': 'Retail.svg', 'link': '/services/ecommerce-website-development/'},
            {'name': 'Manufacturing', 'icon': 'Manufacturing.svg'},
            {'name': 'Oil & Gas', 'icon': 'Oil-Gas.svg'},
            {'name': 'Telecommunication', 'icon': 'Telecommunications.svg'},
            {'name': 'Professional Services', 'icon': 'Professional-Services.svg'},
            {'name': 'Transportaion & Logistics', 'icon': 'Transportaion-Logistics.svg'},
            {'name': 'Education & Elearning', 'icon': 'Education-Elearning.svg'},
            {'name': 'Banking & Finance', 'icon': 'Banking-Finance.svg'}
        ]
        
        industries_html = ""
        for industry in industries:
            link_html = f'<a href="{industry["link"]}" class="local" style="text-decoration: unset;">{industry["name"]}</a>' if 'link' in industry else industry['name']
            industries_html += f"""\n<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="/wp-content/uploads/2025/06/{industry['icon']}" alt="{industry['name']}" width="64" height="64"><p class="fonts-16"> {link_html}</p>
</div>
</div>"""
        
        return f"""<section class="pt80 pb60 industries-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-4 col-md-12">
<div class="industries-desc">
<h2 class="fonts-40 font-weight-bold font-weight-bold mb-2">{heading}</h2>
<p>{description}</p>
</div>
</div>
<div class="col-lg-8 col-md-12 industries-category">
<div class="row text-center">
{industries_html}
\n</div>
</div>
</div>
</div>
</section>"""

    def generate_faq_html(self, content):
        """Generate FAQ section HTML from docx content"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        heading = lines[0] if lines else "Frequently Asked Questions"
        
        # Parse FAQ items
        faqs = []
        current_faq = {}
        in_answer = False
        
        for line in lines[1:]:
            # Check if line is a question (ends with ?)
            if line.endswith('?'):
                if current_faq:
                    faqs.append(current_faq)
                current_faq = {'question': line, 'answer': []}
                in_answer = True
            elif in_answer and current_faq:
                current_faq['answer'].append(line)
        
        if current_faq:
            faqs.append(current_faq)
        
        faq_html = ""
        for i, faq in enumerate(faqs):
            # Process answer paragraphs
            answer_html = ""
            in_bullet_list = False
            for j, para in enumerate(faq['answer']):
                if para.startswith('●'):
                    # Start bullet list if not already started
                    if not in_bullet_list:
                        answer_html += '<ul class="bullet">\n'
                        in_bullet_list = True
                    clean_bullet = para.replace('●', '').strip()
                    # Handle bold formatting in FAQ bullets
                    if ':' in clean_bullet:
                        parts = clean_bullet.split(':', 1)
                        if len(parts) == 2 and len(parts[0]) < 50:
                            answer_html += f"<li><strong>{parts[0]}:</strong>{parts[1]}</li>\n"
                        else:
                            answer_html += f"<li>{clean_bullet}</li>\n"
                    else:
                        answer_html += f"<li>{clean_bullet}</li>\n"
                    
                    # Close bullet list if next item is not a bullet
                    if j+1 >= len(faq['answer']) or not faq['answer'][j+1].startswith('●'):
                        answer_html += '</ul>\n'
                        in_bullet_list = False
                else:
                    # Close any open bullet list
                    if in_bullet_list:
                        answer_html += '</ul>\n'
                        in_bullet_list = False
                    
                    # Check for bold text patterns
                    if ':' in para:
                        parts = para.split(':', 1)
                        if len(parts) == 2 and len(parts[0]) < 50:  # Likely a label
                            answer_html += f"<p><strong>{parts[0]}:</strong>{parts[1]}</p>\n"
                        else:
                            answer_html += f"<p>{para}</p>\n"
                    else:
                        answer_html += f"<p>{para}</p>\n"
            
            show_class = "show" if i == 0 else ""
            collapsed_class = "" if i == 0 else "collapsed"
            
            faq_html += f"""      <div class="card py-4">
        <div class="card-header{' active' if i == 0 else ''}">
          <h3 class="card-link" data-toggle="collapse" href="#faq-{i+1}">{faq['question']}</h3>
          <div id="faq-{i+1}" class="collapse{' show' if i == 0 else ''}" data-parent="#accordion"{' style="display:block;"' if i == 0 else ''}>
            <div class="card card-body">
              {answer_html.strip()}
            </div>
          </div>
        </div>
      </div>\n"""
        
        return f"""<!-- FAQ -->
<div class="faq pt80 pb50" style="background: linear-gradient(var(--bg-color-9), #fff);">
  <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center">{heading}</h2>
    <div id="accordion" class="text-left px-4">
{faq_html}    </div>
  </div>
</div>
<!-- FAQ END-->"""

    def process_docx_content(self, input_file, output_file=None):
        """Process docx content and generate HTML"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sections = self.parse_docx_content(content)
            print(f"Found sections: {list(sections.keys())}")
            
            html_parts = []
            
            # Process each section
            for section_name, section_content in sections.items():
                print(f"Processing section: {section_name}")
                
                if section_name == 'HERO':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_hero_html(section_content))
                elif section_name == 'SERVICES_GRID':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_services_grid_html(section_content))
                elif section_name == 'SERVICES_ACCORDION':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_services_accordion_html(section_content))
                elif section_name == 'CTA_SIMPLE':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_cta_simple_html(section_content))
                elif section_name == 'PORTFOLIO':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_portfolio_html(section_content))
                elif section_name == 'BENEFITS':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_benefits_html(section_content))
                elif section_name == 'TESTIMONIAL':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_testimonial_html(section_content))
                elif section_name == 'BENEFITS_TWO':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_benefits_two_html(section_content))
                elif section_name == 'CONTENT_FORM':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_content_form_html(section_content))
                elif section_name == 'CTA_TWO':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_cta_two_html(section_content))
                elif section_name == 'TECHNOLOGY':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_technology_html(section_content))
                elif section_name == 'INDUSTRIES':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_industries_html(section_content))
                elif section_name == 'FAQ':
                    html_parts.append(f"<!-- {section_name} SECTION -->")
                    html_parts.append(self.generate_faq_html(section_content))
                elif section_name == 'HERO END':
                    # Skip - this is just a marker
                    pass
                elif ' END' in section_name:
                    # Skip all END markers
                    pass
                else:
                    print(f"Warning: Section '{section_name}' not implemented yet")
                
                html_parts.append("")
            
            final_html = "\n".join(html_parts)
            
            # Save output
            if not output_file:
                output_file = input_file.replace('.txt', '_docx_output.html')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_html)
            
            print(f"✅ HTML generated successfully!")
            print(f"📁 Output saved to: {output_file}")
            
            return final_html
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None

def main():
    """Main CLI function"""
    if len(sys.argv) != 2:
        print("Usage: python3 docx_content_tool.py <extracted_docx_content.txt>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    tool = DocxContentTool()
    tool.process_docx_content(input_file)

if __name__ == "__main__":
    main()