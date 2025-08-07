/**
 * Simple CTA Section Generator
 * Generates a simple call-to-action section with title, description, and button
 * Supports default content when no content is provided
 */
function generateCtaSection(content) {
    // Handle empty content with default static HTML
    if (!content || (!content.main_heading && !content.description)) {
        return `<section class="pt80 pb80 new-cta-section section-cta-simple">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title mxw-1000">Ready to Transform Your Business?</p>
<p class="fonts-20 mxw-900">Let's discuss your project and explore how we can help you achieve your digital goals with cutting-edge web solutions.</p>
</div>
<div class="col-md-12 text-center mt-4"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">Start Your Project</button></div>
</div>
</div>
</div>
</section>`;
    }
    
    const template = `<section class="pt80 pb80 new-cta-section section-cta-simple">
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