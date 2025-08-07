/**
 * FAQ Section Generator
 * Generates FAQ section with accordion-style expandable questions and answers
 * Supports default content when no FAQs are provided
 */
function generateFaqSection(content) {
    // Handle empty content with default static HTML
    if (!content || !content.faqs || content.faqs.length === 0) {
        return `<!-- FAQ Section Start -->
<div class="faq pt80 pb50 section-faq" style="background: linear-gradient(var(--bg-color-9), #fff);">
  <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center">Frequently Asked Questions</h2>
    <div id="accordion" class="text-left px-4">
<div class="card py-4">
<div class="card-header active">
<h3 class="card-link" data-toggle="collapse" href="#one">What technologies do you use for web development?</h3>
<div id="one" class="collapse open" data-parent="#accordion" style="display: block;">
<div class="card card-body">
We use modern technologies like React, Node.js, Python, PHP, and various frameworks to build robust and scalable web applications tailored to your business needs.
</div>
</div>
</div>
</div>
<div class="card py-4">
<div class="card-header ">
<h3 class="card-link" data-toggle="collapse" href="#two">How long does it take to develop a website?</h3>
<div id="two" class="collapse" data-parent="#accordion" style="display: none;">
<div class="card card-body">
Development timeline varies based on project complexity. A simple website takes 2-4 weeks, while complex applications can take 3-6 months. We provide detailed timelines during project planning.
</div>
</div>
</div>
</div>
<div class="card py-4">
<div class="card-header ">
<h3 class="card-link" data-toggle="collapse" href="#three">Do you provide ongoing support and maintenance?</h3>
<div id="three" class="collapse" data-parent="#accordion" style="display: none;">
<div class="card card-body">
Yes, we offer comprehensive support and maintenance services including regular updates, security patches, performance optimization, and technical support to keep your website running smoothly.
</div>
</div>
</div>
</div>
<div class="card py-4">
<div class="card-header ">
<h3 class="card-link" data-toggle="collapse" href="#four">What is your development process?</h3>
<div id="four" class="collapse" data-parent="#accordion" style="display: none;">
<div class="card card-body">
Our process includes requirement analysis, planning & strategy, design & development, testing & QA, deployment, and ongoing support. We follow agile methodology for efficient project delivery.
</div>
</div>
</div>
</div>
<div class="card py-4">
<div class="card-header ">
<h3 class="card-link" data-toggle="collapse" href="#five">Can you help with website redesign and upgrades?</h3>
<div id="five" class="collapse" data-parent="#accordion" style="display: none;">
<div class="card card-body">
Absolutely! We specialize in website redesigns, performance improvements, technology upgrades, and modernizing existing websites to meet current standards and user expectations.
</div>
</div>
</div>
</div>
    </div>
  </div>
</div>
<!-- FAQ Section End -->`;
    }
    
    let faqItems = '';
    if (content.faqs) {
        content.faqs.forEach((faq, index) => {
            const collapseId = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'][index] || 'item' + index;
            const isActive = index === 0 ? 'active' : ''; // First item is active
            const showCollapse = index === 0 ? 'style="display: block;"' : 'style="display: none;"';
            const collapseClass = index === 0 ? 'collapse open' : 'collapse';
            
            faqItems += `<div class="card py-4">
<div class="card-header ${isActive}">
<h3 class="card-link" data-toggle="collapse" href="#${collapseId}">${faq.question}</h3>
<div id="${collapseId}" class="${collapseClass}" data-parent="#accordion" ${showCollapse}>
<div class="card card-body">
${faq.answer}
</div>
</div>
</div>
</div>
`;
        });
    }

    const template = `<!-- FAQ Section Start -->
<div class="faq pt80 pb50 section-faq" style="background: linear-gradient(var(--bg-color-9), #fff);">
  <div class="container-xl">
    <h2 class="fonts-40 font-weight-bold text-center">{main_heading}</h2>
    <div id="accordion" class="text-left px-4">
${faqItems}
    </div>
  </div>
</div>
<!-- FAQ Section End -->`;

    return template
        .replace('{main_heading}', content.main_heading || 'FAQs About Web Development Consulting');
}