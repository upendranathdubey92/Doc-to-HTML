/**
 * Testimonial Section Generator
 * Generates client testimonial section with rating, quote, and client image
 * Supports default content when no testimonial is provided
 */
function generateTestimonialSection(content) {
    const template = `<div class="blog-testimonial pb80 pt80 bg-color section-testimonial">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">{main_heading}</h2>
<div class="row align-items-center customer-feedback">
<div class="col-lg-7 blog-testimonial-left">
<p class="description mb-0">{testimonial_text}</p>
<div class="users-feed-ibox d-flex flex-row">
<div class="userfedd-detbox justify-content-between">
<div class="d-flex align-items-center mb-2">
<p class="user-name">{client_name}</p>
<p><img loading="lazy" decoding="async" src="/wp-content/uploads/2023/06/Rating.svg" alt="review-star" width="82" height="13">
</p></div>
<p>{client_title}</p>
</div>
</div>
<div class="read_more">
<a class="btn-link-arrow btn-link-arrow-right" href="/company/client-testimonials/"><span class="btn__label-wrapper">{button_text}</span></a>
</div>
</div>
<div class="col-lg-5 right-img text-right"><img loading="lazy" decoding="async" src="/wp-content/uploads/2024/01/{client_image}" alt="{client_name}" width="434" height="402" onerror="handleImageError(this)"></div>
</div>
</div>
</div>`;

    // Generate client image filename from name
    const clientImageName = (content.client_name || 'Client-Name').replace(/\s+/g, '-') + '.png';

    return template
        .replace('{main_heading}', content.main_heading || 'Client Testimonials')
        .replace('{testimonial_text}', content.testimonial_text || 'Great service!')
        .replace(/{client_name}/g, content.client_name || 'Client Name')
        .replace('{client_title}', content.client_title || 'Client Title')
        .replace('{button_text}', content.button_text || 'View all Testimonials')
        .replace('{client_image}', clientImageName);
}