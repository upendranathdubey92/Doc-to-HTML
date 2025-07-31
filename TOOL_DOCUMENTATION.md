# Page Content Update Tool Documentation

## Overview
The Page Content Update Tool is an automated system that processes text files with labeled sections and generates complete HTML sections following your website's exact structure and styling. The tool preserves all HTML classes, tags, and formatting while only updating the content.

## Features
- ✅ **Zero HTML Changes**: Only content is updated, all classes and structure preserved
- ✅ **Section-Based Processing**: Uses labeled sections for organized content management
- ✅ **Multiple Section Types**: Supports 6 different section patterns
- ✅ **Static Asset Management**: Reuses technology icons and industry data
- ✅ **Validation**: Built-in format validation and error checking
- ✅ **No Dependencies**: Works with standard Python 3

## Supported Section Types

### 1. HERO Section
Complete hero section with form, breadcrumbs, and bullet points
- Main heading and description
- Bullet points with benefits
- Contact form with custom heading/button
- Rating badges (static)

### 2. FAQ Section  
Bootstrap accordion-style FAQ section
- Multiple questions and answers
- First FAQ expanded by default
- Proper accordion functionality

### 3. CTA_SIMPLE Section
Call-to-action section with centered content
- Main heading and description
- Single action button
- Green border styling

### 4. PROCESS Section
Numbered process steps in grid layout
- Up to 6 process steps
- Step titles and descriptions
- Numbered boxes (01, 02, etc.)

### 5. TECHNOLOGY Section
Technology stack showcase
- Categorized technology lists
- Icons and names from predefined database
- Filters based on requested technologies

### 6. INDUSTRIES Section  
Industries served section
- Custom heading and description (left side)
- Static industry icons (right side)
- Responsive grid layout

## Document Format

Create a text file with sections labeled using square brackets:

```
[HERO]
Heading: Your Service Title
Description: Your service description here...
Bullet 1: First benefit point
Bullet 2: Second benefit point
Bullet 3: Third benefit point
Bullet 4: Fourth benefit point
Form Heading: Contact Form Title
Form Button: Button Text

[FAQ]
Heading: FAQ Section Title
Question 1: First question?
Answer 1: Answer to first question...
Question 2: Second question?
Answer 2: Answer to second question...

[CTA_SIMPLE]
Heading: Call to Action Title
Description: CTA description text
Button Text: Action Button Text

[PROCESS]
Heading: Process Section Title
Description: Process description
Step 1: First Step Title
Step Description 1: Description of first step...
Step 2: Second Step Title
Step Description 2: Description of second step...

[TECHNOLOGY]
Heading: Technology Section Title
Description: Technology description
Technologies: React Native, Flutter, Swift, Kotlin, Firebase, MongoDB

[INDUSTRIES]
Heading: Industries Section Title
Description: Industries description text
```

## Usage Instructions

### Step 1: Prepare Your Content File
Create a `.txt` file with your content using the format above. Save it in the project directory.

### Step 2: Run the Tool
```bash
python3 simple_content_tool.py your_content_file.txt
```

### Step 3: Get Results
The tool will:
1. Validate your file format
2. Process each section
3. Generate HTML output
4. Save to `your_content_file_output.html`

## Example Usage

```bash
# Test with provided sample
python3 simple_content_tool.py test_content.txt

# Process your own content
python3 simple_content_tool.py my_service_page.txt
```

## Content Guidelines

### For HERO Section:
- **Heading**: Service title (used in breadcrumb and H1)
- **Description**: Main service description paragraph
- **Bullets**: 3-4 key benefits (automatically formatted as strong text)
- **Form Heading**: Contact form title
- **Form Button**: Form submit button text

### For FAQ Section:
- **Heading**: FAQ section title
- **Questions/Answers**: Number them sequentially (Question 1, Answer 1, etc.)
- First FAQ will be expanded by default

### For CTA Section:
- **Heading**: Call-to-action title
- **Description**: Supporting text
- **Button Text**: Action button label

### For PROCESS Section:
- **Heading**: Process section title
- **Description**: Process introduction
- **Steps**: Title and description for each step (numbered automatically)

### For TECHNOLOGY Section:
- **Heading**: Technology section title
- **Description**: Technology introduction
- **Technologies**: Comma-separated list of technologies to include

### For INDUSTRIES Section:
- **Heading**: Industries section title (left side only)
- **Description**: Industries description (left side only)
- Industry icons are static and always included

## Technology Database

The tool includes predefined technologies organized by category:

### Frontend Technologies
- React, Vue.js, Angular, Next.js, TypeScript, Tailwind CSS

### Backend Technologies  
- Node.js, Python, Django, PHP, Laravel, Ruby on Rails, .NET Core, Express.js

### Database
- PostgreSQL, MongoDB, MySQL, Redis, Firebase, Supabase

### Cloud & DevOps
- AWS, Google Cloud, Microsoft Azure, Docker, Kubernetes, Vercel

### Mobile Technologies
- React Native, Flutter, Swift, Kotlin, Firebase, MongoDB

## Error Handling

The tool provides comprehensive error checking:

### File Validation
- Checks for valid section labels
- Validates required fields
- Reports missing or malformed content

### Processing Errors
- Clear error messages for each issue
- Line-by-line content parsing
- Graceful handling of missing data

## Output Quality

Generated HTML maintains:
- ✅ **Exact class names** from original templates
- ✅ **Complete structure** with all divs and containers
- ✅ **Responsive grid systems** (Bootstrap classes)
- ✅ **Form functionality** with proper IDs and attributes
- ✅ **SEO elements** like breadcrumbs and proper headings
- ✅ **Image paths** and alt attributes
- ✅ **Interactive elements** like accordions and forms

## Limitations

### Not Yet Implemented
- SERVICES_GRID (6-card services layout)
- SERVICES_ACCORDION (accordion services with images)
- CTA_ENHANCED (CTA with statistics)
- PORTFOLIO (project showcase)
- TESTIMONIAL (client testimonials)
- BENEFITS (benefits without icons)
- COMMITMENT (4-column commitment cards)
- CONTENT_FORM (content + form layout)

### Technology Filtering
- Only technologies in the predefined database are supported
- Custom technology icons require manual addition to the database

## Troubleshooting

### Common Issues

**"No sections found"**
- Ensure section labels are in square brackets: `[HERO]`
- Check for typos in section names

**"Missing required fields"**
- HERO section needs: Heading, Description
- FAQ section needs: Questions and Answers
- Refer to format examples above

**"File not found"**
- Ensure file path is correct
- Use relative or absolute paths
- Check file permissions

### Getting Help

1. Run tool with sample file first: `python3 simple_content_tool.py test_content.txt`
2. Check generated output HTML for structure reference
3. Validate your content format against working examples
4. Ensure all required fields are present for each section type

## Next Steps

To extend the tool:
1. Add remaining section types to templates
2. Expand technology database with new icons
3. Add support for custom industry selections
4. Implement Word document support (requires python-docx)
5. Add more validation rules and content checks

The tool is designed to save significant time while maintaining perfect HTML structure and styling consistency across all generated content.