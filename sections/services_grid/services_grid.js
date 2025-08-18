/**
 * Services Grid Section Generator
 * Generates services in a grid layout with images, titles, descriptions and bullet points
 * Supports default content when no services are provided
 */
function generateServicesGridSection(content) {
    const serviceImages = [
        '/wp-content/uploads/2023/09/Architecture-and-Design-Consulting.svg',
        '/wp-content/uploads/2025/07/ux-performance-optimization.svg',
        '/wp-content/uploads/2024/02/Legacy-App-Modernization.svg',
        '/wp-content/uploads/2025/07/code-audits-quality-assurance.svg',
        '/wp-content/uploads/2023/09/MVP-Development.svg',
        '/wp-content/uploads/2024/03/Third-party-Integrations.svg'
    ];

    let servicesGrid = '';
    if (content.services) {
        content.services.forEach((service, index) => {
            const imageSrc = serviceImages[index] || serviceImages[0];
            
            // Generate bullet points if they exist
            let bulletHtml = '';
            if (service.bullets && service.bullets.length > 0) {
                bulletHtml = '<ul class="bullet fonts-14 mb-3">';
                service.bullets.forEach(bullet => {
                    bulletHtml += `<li>${bullet}</li>`;
                });
                bulletHtml += '</ul>';
            }
            
            // Parse service link if available
            let serviceLink = '';
            let readMoreButton = '';
            
            // Check if service has a link property
            if (service.link && service.link.trim()) {
                serviceLink = service.link.trim();
            } else {
                // Try to extract link from description using various patterns
                const urlPattern = /(https?:\/\/[^\s]+)/gi;
                const markdownLinkPattern = /\[([^\]]+)\]\(([^)]+)\)/gi;
                
                // Check for markdown-style links first
                const markdownMatch = markdownLinkPattern.exec(service.description);
                if (markdownMatch) {
                    serviceLink = markdownMatch[2];
                    // Remove the markdown link syntax from description
                    service.description = service.description.replace(markdownLinkPattern, markdownMatch[1]);
                } else {
                    // Check for plain URLs
                    const urlMatch = urlPattern.exec(service.description);
                    if (urlMatch) {
                        serviceLink = urlMatch[0];
                        // Optionally remove the URL from description to avoid duplication
                        service.description = service.description.replace(urlMatch[0], '').trim();
                    }
                }
            }
            
            // Create read more button if link exists
            if (serviceLink) {
                readMoreButton = `<div class="service-link mt-3">
                    <a href="${serviceLink}" class="btn-link-arrow btn-link-arrow-right" target="_blank" rel="noopener noreferrer">
                        <span class="btn__label-wrapper">${service.buttonText || 'Learn More'}</span>
                    </a>
                </div>`;
            }

            servicesGrid += `
<div class="col-lg-4 col-md-6">
<div class="mad_service_box">
<img src="${imageSrc}" alt="${service.title}" width="74" height="74" />
<h3 class="fonts-18 font-weight-semibold">${service.title}</h3>
<p>${service.description}</p>
${bulletHtml}
${readMoreButton}
</div>
</div>
`;
        });
    }

    const template = `<section class="pt80 pb50 services-section bg-color section-services-grid">
<div class="container-xl">
<h2 class="fonts-40 text-center font-weight-bold mb-3 mxw-1000">{main_heading}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
${servicesGrid}
</div>
</div>
</section>`;

    return template
        .replace('{main_heading}', content.main_heading || 'Our Services')
        .replace('{description}', content.description || 'Services we provide');
}