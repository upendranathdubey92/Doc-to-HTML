/**
 * Portfolio Section Generator
 * Generates portfolio/project showcase with alternating layouts
 * Supports default content when no projects are provided
 */
function generatePortfolioSection(content) {
    let portfolioItems = '';
    if (content.projects && content.projects.length > 0) {
        content.projects.forEach((project, index) => {
            const orderClass = index % 2 === 0 ? 'order-1' : 'order-2';
            const isEven = index % 2 === 0;
            
            if (isEven) {
                // Even index: Text left, Image right
                portfolioItems += `<div class="slider_projects ${orderClass}">
<div class="row vcenter-parent">
<div class="col-lg-6 col-12">
<div class="left_text">
<div class="slider-app-name">
<div class="top-heading">
<h3 class="fonts-26 mb-2 font-weight-bold"><a href="${project.link || '#'}">${project.title}</a></h3>
</div>
</div>
<p class="mb-3">${project.description}</p>
<div class="keep-reading ml-2"><a class="btn-link-arrow btn-link-arrow-right" href="${project.link || '#'}"><span class="btn__label-wrapper">${project.buttonText || 'See Project Details'}</span></a></div>
</div>
</div>
<div class="col-lg-6 col-12">
<img loading="lazy" decoding="async" class="project-img" src="${project.image || '/wp-content/uploads/2025/07/default-project.jpg'}" alt="${project.title}" width="600" height="459" onerror="handleImageError(this)">
</div>
</div>
</div>
`;
            } else {
                // Odd index: Text left, Image right (same as even for consistency)
                portfolioItems += `<div class="slider_projects ${orderClass}">
<div class="row vcenter-parent">
<div class="col-lg-6 col-12">
<div class="left_text">
<div class="slider-app-name">
<div class="top-heading">
<h3 class="fonts-26 mb-2 font-weight-bold"><a href="${project.link || '#'}">${project.title}</a></h3>
</div>
</div>
<p class="mb-3">${project.description}</p>
<div class="keep-reading ml-2"><a class="btn-link-arrow btn-link-arrow-right" href="${project.link || '#'}"><span class="btn__label-wrapper">${project.buttonText || 'See Project Details'}</span></a></div>
</div>
</div>
<div class="col-lg-6 col-12">
<img loading="lazy" decoding="async" class="project-img" src="${project.image || '/wp-content/uploads/2025/07/default-project.jpg'}" alt="${project.title}" width="600" height="459" onerror="handleImageError(this)">
</div>
</div>
</div>
`;
            }
        });
    }
    
    return `<div class="our-work pt70 pb70 bg-color section-portfolio">
<div class="container-xl">
<div class="text-center">
<h2 class="fonts-40 text-center font-weight-bold mb-2 mxw-900">${content.main_heading || 'Proven Results: Real Projects That Drive Business Growth'}</h2>
<p class="fonts-18 text-center mb-3 mxw-900">${content.description || 'See how we\'ve transformed complex business challenges into measurable success stories.'}</p>
</div>
${portfolioItems}
</div>
</div>`;
}