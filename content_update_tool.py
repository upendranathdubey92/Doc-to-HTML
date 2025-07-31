#!/usr/bin/env python3
"""
Page Content Update Tool
Processes Word documents with labeled sections and generates HTML content
"""

import re
import os
import sys
from typing import Dict, List, Optional, Tuple
from docx import Document

class ContentUpdateTool:
    def __init__(self):
        """Initialize the content update tool with section templates"""
        self.section_templates = self._load_section_templates()
        self.technology_stack = self._load_technology_stack()
        self.industry_data = self._load_industry_data()
        
    def _load_section_templates(self) -> Dict[str, str]:
        """Load HTML templates for each section type"""
        return {
            'HERO': '''<section class="pt70 pb40 hero-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-7 col-md-12 banner-text">
<nav aria-label="breadcrumbs" class="rank-math-breadcrumb mb-3 mt-3"><p><a href="/" class="local" style="text-decoration: unset;">Home</a><span class="separator"> &gt; </span><a href="/services/" class="local" style="text-decoration: unset;">Services</a><span class="separator"> &gt; </span><span class="last">{breadcrumb_title}</span></p></nav>
<h1 class="fonts-45 mb-3 font-weight-bold">{main_heading}</h1>
<p class="fonts-18 mb-3">{description} <strong>The result?</strong></p>
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
<input id="submit" class="btn btn-pop mb0" name="submit" type="submit" value="{form_button_text}" data-medium="BF_1" />

</div>
</div>
</div>
</form></div>
</div>
</div>
</div>
</section>''',

            'SERVICES_GRID': '''<section class="pt80 pb50 services-section bg-color">
<div class="container-xl">
<h2 class="fonts-40 text-center font-weight-bold mb-3 mxw-1000">{main_heading}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
{service_cards}
</div>
</div>
</section>''',

            'SERVICES_ACCORDION': '''<section class="techno-stack pb80 bg-color services-tab-new">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="{image_url}" alt="{image_alt}" width="630" height="500">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
{accordion_items}
</div>
</div>
</div>
</div>
</section>''',

            'CTA_SIMPLE': '''<section class="pt80 pb80 new-cta-section">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title mxw-900">{main_heading}</p>
<p class="fonts-20 mxw-900">{description}</p>
</div>
<div class="col-md-12 text-center mt-4"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">{button_text}</button></div>
</div>
</div>
</div>
</section>''',

            'CTA_ENHANCED': '''<section class="pt50 pb80 new-cta-section">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title">{main_heading}</p>
<p class="fonts-20 mxw-900">{description}</p>
</div>
<div class="new-button-group">
{stat_boxes}
</div>
<div class="col-md-12 text-center mt-4 d-flex justify-content-center two-btn-group"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">{primary_button}</button> <a class="btn btn-pop open-qouteform white-btn" href="{secondary_button_url}">{secondary_button}</a></div>
</div>
</div>
</div>
</section>''',

            'PORTFOLIO': '''<div class="our-work pt70 pb70 bg-color">
<div class="container-xl">
<h2 class="fonts-40 text-center font-weight-bold mb-2">{main_heading}</h2>
<p class="fonts-18 text-center mb-3">{description}</p>
<div class="slider_projects order-2">
{project_items}
</div>
</div>''',

            'TESTIMONIAL': '''<div class="blog-testimonial pb80 pt80 bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">{main_heading}</h2>
<div class="row align-items-center customer-feedback">
<div class="col-lg-7 blog-testimonial-left">
<p class="description mb-0">{testimonial_text}</p>
<div class="users-feed-ibox d-flex flex-row">
<div class="userfedd-detbox justify-content-between">
<div class="d-flex align-items-center mb-2">
<p class="user-name">{client_name}</p>
<img src="/wp-content/uploads/2023/06/Rating.svg" alt="review-star" width="82" height="13" />
</div>
<p>{client_position}</p>
</div>
</div>
<div class="read_more">
<a class="btn-link-arrow btn-link-arrow-right" href="/company/client-testimonials/"><span class="btn__label-wrapper">View all Testimonials</span></a>
</div>
</div>
<div class="col-lg-5 right-img text-right"><img src="{client_image}" alt="{client_name}" width="434" height="402" /></div>
</div>
</div>
</div>''',

            'PROCESS': '''<section class="pt80 pb50 process-sec bg-color">
   <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center mb-3 mxw-1000">{main_heading}</h2>
    <p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
      <div class="row">
{process_steps}
      </div>
   </div>
</section>''',

            'TECHNOLOGY': '''<div class="technology-stack pt80 pb60">
<div class="container-xl">
<div class="row">
<div class="col-md-12">
<h2 class="fonts-40 text-center font-weight-bold mxw-900">{main_heading}</h2>
<p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
</div>
</div>
<div class="technology-inner mt-4">
{technology_sections}
</div>
</div>
</div>''',

            'INDUSTRIES': '''<section class="pt80 pb60 industries-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-4 col-md-12">
<div class="industries-desc">
<h2 class="fonts-40 font-weight-bold font-weight-bold mb-2">{main_heading}</h2>
<p>{description}</p>
</div>
</div>
<div class="col-lg-8 col-md-12 industries-category">
<div class="row text-center">
{industry_boxes}
</div>
</div>
</div>
</div>
</section>''',

            'FAQ': '''<div class="faq pt80 pb50" style="background: linear-gradient(var(--bg-color-9), #fff);">
  <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center">{main_heading}</h2>
    <div id="accordion" class="text-left px-4">
{faq_items}
    </div>
  </div>
</div>''',

            'BENEFITS': '''<section class="pt80 pb50 services-section practices-we-follow">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3 mxw-1000">{main_heading}</h2>
<p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
<div class="row">
{benefit_cards}
</div>
</div>
</section>''',

            'COMMITMENT': '''<section class="pt80 pb50 services-section bg-color">
    <div class="container-xl">
        <h2 class="fonts-40 text-center font-weight-bold mb-3 mxw-900">{main_heading}</h2>
        <p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
        <div class="row">
{commitment_cards}
        </div>
    </div>
</section>''',

            'CONTENT_FORM': '''<section class="pt80 pb80 text-form-section bg-color">
<div class="container-xl">
<div class="row">
<div class="col-lg-6 col-md-12 col-sm-12">
<h2 class="fonts-40 font-weight-bold text-left mb-4">{main_heading}</h2>
{content_text}
</div>
<div class="col-lg-6 col-md-12 col-sm-12 text-center">
<div class="homen_form">
<p class="fonts-24 font-weight-bold mt-0 mb-3 text-center line-height-1 pb-0">{form_heading}</p>
<p class="fonts-16 mb-3">{form_description}</p>
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
<input id="submit" class="btn btn-pop mb0" name="submit" type="submit" value="{form_button_text}" data-medium="S_2" />
</div>
</div>
</div>
</form>
</div>
</div>
</div>
</div>
</section>'''
        }

    def _load_technology_stack(self) -> Dict[str, List[Dict[str, str]]]:
        """Load technology stack data with icons and names"""
        return {
            'Frontend Technologies': [
                {'name': 'React', 'icon': '/wp-content/uploads/2023/08/React.svg'},
                {'name': 'Vue.js', 'icon': '/wp-content/uploads/2023/08/Vue-JS.svg'},
                {'name': 'Angular', 'icon': '/wp-content/uploads/2023/08/Angular.svg'},
                {'name': 'Next.js', 'icon': '/wp-content/uploads/2024/02/Next.js.svg'},
                {'name': 'TypeScript', 'icon': '/wp-content/uploads/2024/03/typescript.svg'},
                {'name': 'Tailwind CSS', 'icon': '/wp-content/uploads/2024/02/Tailwind.svg'}
            ],
            'Backend Technologies': [
                {'name': 'Node.js', 'icon': '/wp-content/uploads/2023/08/Node.js.svg'},
                {'name': 'Python', 'icon': '/wp-content/uploads/2023/08/python.svg'},
                {'name': 'Django', 'icon': '/wp-content/uploads/2023/08/Django.svg'},
                {'name': 'PHP', 'icon': '/wp-content/uploads/2022/01/php.svg'},
                {'name': 'Laravel', 'icon': '/wp-content/uploads/2023/08/Laravel.svg'},
                {'name': 'Ruby on Rails', 'icon': '/wp-content/uploads/2023/08/ROR.svg'},
                {'name': '.NET Core', 'icon': '/wp-content/uploads/2023/08/Microsoft_.NET_.svg'},
                {'name': 'Express.js', 'icon': '/wp-content/uploads/2023/08/expressjs.svg'}
            ],
            'Database': [
                {'name': 'PostgreSQL', 'icon': '/wp-content/uploads/2023/08/Postgresql_elephant.svg'},
                {'name': 'MongoDB', 'icon': '/wp-content/uploads/2023/08/MongoDB.svg'},
                {'name': 'MySQL', 'icon': '/wp-content/uploads/2023/08/MySQL.svg'},
                {'name': 'Redis', 'icon': '/wp-content/uploads/2023/08/Redis.svg'},
                {'name': 'Firebase', 'icon': '/wp-content/uploads/2023/08/Firebase.svg'},
                {'name': 'Supabase', 'icon': '/wp-content/uploads/2025/07/supabase.svg'}
            ],
            'Cloud & DevOps': [
                {'name': 'AWS', 'icon': '/wp-content/uploads/2023/08/AWS.svg'},
                {'name': 'Google Cloud', 'icon': '/wp-content/uploads/2025/06/Google-Cloud-Platform.svg'},
                {'name': 'Microsoft Azure', 'icon': '/wp-content/uploads/2023/08/Microsoft-Azure.svg'},
                {'name': 'Docker', 'icon': '/wp-content/uploads/2023/08/Docker.svg'},
                {'name': 'Kubernetes', 'icon': '/wp-content/uploads/2023/08/Kubernetes.svg'},
                {'name': 'Vercel', 'icon': '/wp-content/uploads/2025/07/vercel.svg'}
            ],
            'No-Code / Low-Code': [
                {'name': 'Webflow', 'icon': '/wp-content/uploads/2025/07/webflow.svg'},
                {'name': 'Bubble', 'icon': '/wp-content/uploads/2025/07/bubble.svg'},
                {'name': 'Airtable', 'icon': '/wp-content/uploads/2025/07/airtable.svg'},
                {'name': 'Zapier', 'icon': '/wp-content/uploads/2024/02/Zapier.svg'},
                {'name': 'Notion', 'icon': '/wp-content/uploads/2025/07/notion.svg'},
                {'name': 'Strapi', 'icon': '/wp-content/uploads/2025/07/strapi.svg'}
            ],
            'Design & Tools': [
                {'name': 'Figma', 'icon': '/wp-content/uploads/2023/08/Figma.svg'},
                {'name': 'Adobe Creative Suite', 'icon': '/wp-content/uploads/2025/07/adobe-creative-suite.svg'},
                {'name': 'Sketch', 'icon': '/wp-content/uploads/2023/09/Sketch.svg'},
                {'name': 'Framer', 'icon': '/wp-content/uploads/2025/07/framer.svg'},
                {'name': 'InVision', 'icon': '/wp-content/uploads/2021/01/InVision.png'}
            ]
        }

    def _load_industry_data(self) -> List[Dict[str, str]]:
        """Load industry data with icons and names"""
        return [
            {'name': 'Healthcare', 'icon': '/wp-content/uploads/2025/06/Healthcare.svg'},
            {'name': 'Real Estate', 'icon': '/wp-content/uploads/2025/06/Real-estate.svg'},
            {'name': 'Investment', 'icon': '/wp-content/uploads/2025/06/Investment.svg'},
            {'name': 'Insurance', 'icon': '/wp-content/uploads/2025/06/Insurance.svg'},
            {'name': 'eCommerce', 'icon': '/wp-content/uploads/2025/06/Retail.svg', 'link': 'https://www.spaceotechnologies.com/services/ecommerce-website-development/'},
            {'name': 'Manufacturing', 'icon': '/wp-content/uploads/2025/06/Manufacturing.svg'},
            {'name': 'Oil & Gas', 'icon': '/wp-content/uploads/2025/06/Oil-Gas.svg'},
            {'name': 'Telecommunication', 'icon': '/wp-content/uploads/2025/06/Telecommunications.svg'},
            {'name': 'Professional Services', 'icon': '/wp-content/uploads/2025/06/Professional-Services.svg'},
            {'name': 'Transportaion & Logistics', 'icon': '/wp-content/uploads/2025/06/Transportaion-Logistics.svg'},
            {'name': 'Education & Elearning', 'icon': '/wp-content/uploads/2025/06/Education-Elearning.svg'},
            {'name': 'Banking & Finance', 'icon': '/wp-content/uploads/2025/06/Banking-Finance.svg'}
        ]

    def parse_document(self, doc_path: str) -> Dict[str, Dict]:
        """Parse Word document and extract content by section labels"""
        try:
            doc = Document(doc_path)
            sections = {}
            current_section = None
            current_content = {}
            
            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if not text:
                    continue
                    
                # Check if this is a section label
                section_match = re.match(r'\[(\w+)\]', text)
                if section_match:
                    # Save previous section if exists
                    if current_section and current_content:
                        sections[current_section] = current_content
                    
                    # Start new section
                    current_section = section_match.group(1)
                    current_content = {}
                    continue
                
                # Parse content within current section
                if current_section:
                    self._parse_section_content(text, current_content, current_section)
            
            # Save last section
            if current_section and current_content:
                sections[current_section] = current_content
                
            return sections
            
        except Exception as e:
            raise Exception(f"Error parsing document: {str(e)}")

    def _parse_section_content(self, text: str, content: Dict, section_type: str):
        """Parse content line based on section type"""
        # Handle different content patterns
        if text.startswith('Heading:'):
            content['main_heading'] = text.replace('Heading:', '').strip()
        elif text.startswith('Description:'):
            content['description'] = text.replace('Description:', '').strip()
        elif text.startswith('Bullet '):
            if 'bullet_points' not in content:
                content['bullet_points'] = []
            bullet_text = re.sub(r'^Bullet \d+:', '', text).strip()
            content['bullet_points'].append(bullet_text)
        elif text.startswith('Service '):
            if 'services' not in content:
                content['services'] = []
            service_match = re.match(r'Service (\d+):(.*)', text)
            if service_match:
                service_num = int(service_match.group(1))
                service_title = service_match.group(2).strip()
                # Ensure we have enough service slots
                while len(content['services']) < service_num:
                    content['services'].append({})
                content['services'][service_num - 1]['title'] = service_title
        elif text.startswith('Service Description '):
            if 'services' not in content:
                content['services'] = []
            desc_match = re.match(r'Service Description (\d+):(.*)', text)
            if desc_match:
                service_num = int(desc_match.group(1))
                desc_text = desc_match.group(2).strip()
                while len(content['services']) < service_num:
                    content['services'].append({})
                content['services'][service_num - 1]['description'] = desc_text
        elif text.startswith('Question '):
            if 'faqs' not in content:
                content['faqs'] = []
            q_match = re.match(r'Question (\d+):(.*)', text)
            if q_match:
                faq_num = int(q_match.group(1))
                question = q_match.group(2).strip()
                while len(content['faqs']) < faq_num:
                    content['faqs'].append({})
                content['faqs'][faq_num - 1]['question'] = question
        elif text.startswith('Answer '):
            if 'faqs' not in content:
                content['faqs'] = []
            a_match = re.match(r'Answer (\d+):(.*)', text)
            if a_match:
                faq_num = int(a_match.group(1))
                answer = a_match.group(2).strip()
                while len(content['faqs']) < faq_num:
                    content['faqs'].append({})
                content['faqs'][faq_num - 1]['answer'] = answer
        elif text.startswith('Step '):
            if 'steps' not in content:
                content['steps'] = []
            step_match = re.match(r'Step (\d+):(.*)', text)
            if step_match:
                step_num = int(step_match.group(1))
                step_title = step_match.group(2).strip()
                while len(content['steps']) < step_num:
                    content['steps'].append({})
                content['steps'][step_num - 1]['title'] = step_title
        elif text.startswith('Step Description '):
            if 'steps' not in content:
                content['steps'] = []
            desc_match = re.match(r'Step Description (\d+):(.*)', text)
            if desc_match:
                step_num = int(desc_match.group(1))
                desc_text = desc_match.group(2).strip()
                while len(content['steps']) < step_num:
                    content['steps'].append({})
                content['steps'][step_num - 1]['description'] = desc_text
        elif text.startswith('Form Heading:'):
            content['form_heading'] = text.replace('Form Heading:', '').strip()
        elif text.startswith('Form Button:'):
            content['form_button_text'] = text.replace('Form Button:', '').strip()
        elif text.startswith('Button Text:'):
            content['button_text'] = text.replace('Button Text:', '').strip()
        elif text.startswith('Technologies:'):
            tech_list = text.replace('Technologies:', '').strip()
            content['technologies'] = [tech.strip() for tech in tech_list.split(',')]
        # Add more parsing patterns as needed

    def generate_hero_section(self, content: Dict) -> str:
        """Generate hero section HTML"""
        template = self.section_templates['HERO']
        
        # Format bullet points
        bullet_points = ""
        if 'bullet_points' in content:
            for bullet in content['bullet_points']:
                bullet_points += f"    <li><strong>{bullet}</strong></li>\n"
        
        # Default values
        defaults = {
            'breadcrumb_title': content.get('main_heading', 'Service'),
            'main_heading': content.get('main_heading', 'Service Title'),
            'description': content.get('description', 'Service description'),
            'bullet_points': bullet_points,
            'form_heading': content.get('form_heading', 'Dream It, We Build It'),
            'form_button_text': content.get('form_button_text', 'Book Your Free Consultation')
        }
        
        return template.format(**defaults)

    def generate_services_grid(self, content: Dict) -> str:
        """Generate services grid section HTML"""
        template = self.section_templates['SERVICES_GRID']
        
        service_cards = ""
        if 'services' in content:
            for i, service in enumerate(content['services']):
                # Generate icon path (you may need to customize this based on your icon naming)
                icon_path = f"/wp-content/uploads/2025/07/service-{i+1}.svg"
                alt_text = service.get('title', f'Service {i+1}')
                
                service_card = f'''
<div class="col-lg-4 col-md-6">
<div class="mad_service_box">
<img src="{icon_path}" alt="{alt_text}" width="74" height="74" />
<h3 class="fonts-18 font-weight-semibold">{service.get('title', '')}</h3>
<p>{service.get('description', '')}</p>
<ul class="bullet fonts-14 mb-3">
{self._format_service_bullets(service.get('bullets', []))}
</ul>
</div>
</div>'''
                service_cards += service_card
        
        defaults = {
            'main_heading': content.get('main_heading', 'Our Services'),
            'description': content.get('description', 'Service description'),
            'service_cards': service_cards
        }
        
        return template.format(**defaults)

    def _format_service_bullets(self, bullets: List[str]) -> str:
        """Format bullet points for services"""
        if not bullets:
            return ""
        bullet_html = ""
        for bullet in bullets:
            bullet_html += f"<li>{bullet}</li>\n"
        return bullet_html

    def generate_faq_section(self, content: Dict) -> str:
        """Generate FAQ section HTML"""
        template = self.section_templates['FAQ']
        
        faq_items = ""
        if 'faqs' in content:
            for i, faq in enumerate(content['faqs'], 1):
                # First FAQ is active by default
                active_class = " active" if i == 1 else ""
                display_style = ' style="display:block;"' if i == 1 else ""
                
                faq_item = f'''
      <div class="card py-4">
        <div class="card-header{active_class}">
          <h3 class="card-link" data-toggle="collapse" href="#{self._number_to_word(i)}">{faq.get('question', '')}</h3>
          <div id="{self._number_to_word(i)}" class="collapse" data-parent="#accordion"{display_style}>
            <div class="card card-body">
              <p>{faq.get('answer', '')}</p>
            </div>
          </div>
        </div>
      </div>'''
                faq_items += faq_item
        
        defaults = {
            'main_heading': content.get('main_heading', 'Frequently Asked Questions'),
            'faq_items': faq_items
        }
        
        return template.format(**defaults)

    def _number_to_word(self, num: int) -> str:
        """Convert number to word for FAQ IDs"""
        words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        return words[num] if num < len(words) else f'item{num}'

    def generate_cta_simple(self, content: Dict) -> str:
        """Generate simple CTA section HTML"""
        template = self.section_templates['CTA_SIMPLE']
        
        defaults = {
            'main_heading': content.get('main_heading', 'Ready to Get Started?'),
            'description': content.get('description', 'Let us help you build something amazing.'),
            'button_text': content.get('button_text', 'Get Started Today')
        }
        
        return template.format(**defaults)

    def generate_process_section(self, content: Dict) -> str:
        """Generate process section HTML"""
        template = self.section_templates['PROCESS']
        
        process_steps = ""
        if 'steps' in content:
            for i, step in enumerate(content['steps'], 1):
                step_html = f'''         <div class="col-lg-4 col-md-6">
            <div class="instalikeapp">
               <p class="number">{i:02d}</p>
               <h3 class="font-weight-semibold fonts-20 mt-2 mb-3">{step.get('title', '')}</h3>
               <p>{step.get('description', '')}</p>
            </div>
         </div>'''
                process_steps += step_html
        
        defaults = {
            'main_heading': content.get('main_heading', 'Our Process'),
            'description': content.get('description', 'How we work with you'),
            'process_steps': process_steps
        }
        
        return template.format(**defaults)

    def generate_technology_section(self, content: Dict) -> str:
        """Generate technology stack section HTML"""
        template = self.section_templates['TECHNOLOGY']
        
        # Get requested technologies or use all
        requested_techs = content.get('technologies', [])
        
        technology_sections = ""
        for category, techs in self.technology_stack.items():
            if requested_techs:
                # Filter technologies based on requested list
                filtered_techs = [tech for tech in techs if tech['name'] in requested_techs]
                if not filtered_techs:
                    continue
            else:
                filtered_techs = techs
            
            tech_items = ""
            for tech in filtered_techs:
                tech_items += f'          <li><img src="{tech["icon"]}" alt="{tech["name"]}" width="24" height="24"> {tech["name"]}</li>\n'
            
            section_html = f'''  <div class="row">
    <div class="col-md-2">
      <div class="technology-name fonts-20">{category}</div>
    </div>
    <div class="col-md-10">
      <ul class="technology-icon-wrapper">
{tech_items}        </ul>
    </div>
  </div>

'''
            technology_sections += section_html
        
        defaults = {
            'main_heading': content.get('main_heading', 'Technology Stack'),
            'description': content.get('description', 'Technologies we work with'),
            'technology_sections': technology_sections
        }
        
        return template.format(**defaults)

    def generate_industries_section(self, content: Dict) -> str:
        """Generate industries section HTML"""
        template = self.section_templates['INDUSTRIES']
        
        # Generate industry boxes (static)
        industry_boxes = ""
        for industry in self.industry_data:
            if 'link' in industry:
                industry_name = f'<a href="{industry["link"]}">{industry["name"]}</a>'
            else:
                industry_name = industry['name']
                
            box_html = f'''
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="{industry['icon']}" alt="{industry['name']}" width="64" height="64"><p class="fonts-16">{industry_name}</p>
</div>
</div>'''
            industry_boxes += box_html
        
        defaults = {
            'main_heading': content.get('main_heading', 'Industries We Serve'),
            'description': content.get('description', 'We serve various industries with our expertise.'),
            'industry_boxes': industry_boxes
        }
        
        return template.format(**defaults)

    def process_document(self, doc_path: str, output_path: str = None) -> str:
        """Process Word document and generate HTML sections"""
        try:
            print(f"Parsing document: {doc_path}")
            sections = self.parse_document(doc_path)
            
            if not sections:
                raise Exception("No sections found in document")
            
            print(f"Found sections: {list(sections.keys())}")
            
            generated_html = []
            
            # Process each section
            for section_type, content in sections.items():
                print(f"Processing section: {section_type}")
                
                if section_type == 'HERO':
                    html = self.generate_hero_section(content)
                elif section_type == 'SERVICES_GRID':
                    html = self.generate_services_grid(content)
                elif section_type == 'FAQ':
                    html = self.generate_faq_section(content)
                elif section_type == 'CTA_SIMPLE':
                    html = self.generate_cta_simple(content)
                elif section_type == 'PROCESS':
                    html = self.generate_process_section(content)
                elif section_type == 'TECHNOLOGY':
                    html = self.generate_technology_section(content)
                elif section_type == 'INDUSTRIES':
                    html = self.generate_industries_section(content)
                else:
                    print(f"Warning: Section type '{section_type}' not implemented yet")
                    continue
                
                generated_html.append(f"<!-- {section_type} SECTION -->")
                generated_html.append(html)
                generated_html.append("")
            
            final_html = "\n".join(generated_html)
            
            # Save to output file if specified
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(final_html)
                print(f"HTML saved to: {output_path}")
            
            return final_html
            
        except Exception as e:
            raise Exception(f"Error processing document: {str(e)}")

    def validate_document_format(self, doc_path: str) -> Tuple[bool, List[str]]:
        """Validate document format and return issues if any"""
        issues = []
        
        try:
            sections = self.parse_document(doc_path)
            
            if not sections:
                issues.append("No valid sections found. Make sure to use section labels like [HERO], [FAQ], etc.")
                return False, issues
            
            # Check for required fields in each section
            for section_type, content in sections.items():
                if section_type == 'HERO':
                    if not content.get('main_heading'):
                        issues.append("HERO section missing 'Heading:' field")
                    if not content.get('description'):
                        issues.append("HERO section missing 'Description:' field")
                elif section_type == 'FAQ':
                    if not content.get('faqs'):
                        issues.append("FAQ section missing questions/answers")
                # Add more validations as needed
            
            return len(issues) == 0, issues
            
        except Exception as e:
            issues.append(f"Document parsing error: {str(e)}")
            return False, issues


def main():
    """Main function for CLI usage"""
    if len(sys.argv) != 2:
        print("Usage: python content_update_tool.py <path_to_word_document>")
        sys.exit(1)
    
    doc_path = sys.argv[1]
    
    if not os.path.exists(doc_path):
        print(f"Error: Document not found at {doc_path}")
        sys.exit(1)
    
    # Initialize tool
    tool = ContentUpdateTool()
    
    # Validate document format
    print("Validating document format...")
    is_valid, issues = tool.validate_document_format(doc_path)
    
    if not is_valid:
        print("Document validation failed:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    
    print("Document validation passed!")
    
    # Process document
    try:
        output_path = doc_path.replace('.docx', '_output.html')
        html_output = tool.process_document(doc_path, output_path)
        
        print(f"\n✅ Successfully generated HTML!")
        print(f"📁 Output saved to: {output_path}")
        print(f"📊 Generated {len(html_output.split('<!-- '))} sections")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()