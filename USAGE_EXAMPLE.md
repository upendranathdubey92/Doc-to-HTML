# Quick Usage Example

## Step 1: Create your content file

Create a file called `my_service.txt`:

```
[HERO]
Heading: AI Development Services
Description: Transform your business with cutting-edge artificial intelligence solutions. Our AI development services help companies automate processes, gain insights from data, and create intelligent applications that drive growth and innovation.
Bullet 1: Custom AI models tailored to your business needs
Bullet 2: Machine learning algorithms for predictive analytics
Bullet 3: Natural language processing and computer vision
Bullet 4: End-to-end AI implementation and support
Form Heading: Get Your AI Solution
Form Button: Schedule AI Consultation

[FAQ]
Heading: AI Development FAQs
Question 1: What types of AI solutions do you develop?
Answer 1: We develop custom machine learning models, chatbots, recommendation systems, computer vision applications, and natural language processing solutions tailored to your specific business requirements.
Question 2: How long does AI development take?
Answer 2: AI development timelines vary from 8-16 weeks for standard solutions to 6+ months for complex enterprise AI systems. We provide detailed timelines after understanding your requirements.

[CTA_SIMPLE]
Heading: Ready to Implement AI in Your Business?
Description: Let our AI experts help you identify opportunities and build intelligent solutions that drive real business value.
Button Text: Start Your AI Journey

[TECHNOLOGY]
Heading: AI Technologies We Use
Description: We leverage cutting-edge AI frameworks and cloud platforms to build scalable, intelligent solutions.
Technologies: Python, TensorFlow, PyTorch, AWS, Docker, MongoDB
```

## Step 2: Run the tool

```bash
python3 simple_content_tool.py my_service.txt
```

## Step 3: Check the output

The tool will generate `my_service_output.html` with complete HTML sections ready to use!

## Result Preview

```html
<!-- HERO SECTION -->
<section class="pt70 pb40 hero-section">
<div class="container-xl">
<div class="row align-items-center">
<div class="col-lg-7 col-md-12 banner-text">
<nav aria-label="breadcrumbs" class="rank-math-breadcrumb mb-3 mt-3">
  <p><a href="/" class="local">Home</a><span class="separator"> > </span>
     <a href="/services/" class="local">Services</a><span class="separator"> > </span>
     <span class="last">AI Development Services</span></p>
</nav>
<h1 class="fonts-45 mb-3 font-weight-bold">AI Development Services</h1>
<p class="fonts-18 mb-3">Transform your business with cutting-edge artificial intelligence solutions... <strong>The result?</strong></p>
<ul class="bullet mb-5 fonts-18">
    <li><strong>Custom AI models tailored to your business needs</strong></li>
    <li><strong>Machine learning algorithms for predictive analytics</strong></li>
    <li><strong>Natural language processing and computer vision</strong></li>
    <li><strong>End-to-end AI implementation and support</strong></li>
</ul>
<!-- Complete form and rating sections included -->
```

That's it! The tool generates production-ready HTML with all the correct classes and structure.