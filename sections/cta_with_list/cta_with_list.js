/**
 * CTA with List Section Generator
 * Generates a call-to-action section with statistics/achievements and dual buttons
 * Supports default content when no content is provided
 */
function generateCtaTwoSection(content) {
    let statsHtml = '';
    const statImages = [
        'https://www.spaceotechnologies.com/wp-content/uploads/2025/06/Frame-1.svg',
        '/wp-content/uploads/2025/07/frameworks-tools-mastered.svg',
        '/wp-content/uploads/2025/07/seo-mobile-optimized.svg',
        '/wp-content/uploads/2025/07/years-of-dev-expertise.svg'
    ];
    
    // Handle empty content with default static HTML
    if (!content || (!content.title && !content.description && (!content.stats || content.stats.length === 0))) {
        const defaultStats = [
            '350+ Web Solutions Delivered',
            '20+ Frameworks Mastered',
            '99% Client Satisfaction',
            '5+ Years Experience'
        ];
        
        defaultStats.forEach((stat, index) => {
            const imgSrc = statImages[index] || statImages[0];
            const parts = stat.split(' ');
            const number = parts[0];
            const text = parts.slice(1).join(' ');
            
            statsHtml += `    <div class="new-button-group-inner">
        <img src="${imgSrc}">
        <strong>${number}</strong> ${text}
    </div>
`;
        });
        
        return `<section class="pt50 pb80 new-cta-section section-cta-two">
<div class="container-xl">
<div class="cta-inner">
<div class="row align-items-center">
<div class="col-md-12 text-center">
<p class="fonts-40 font-weight-bold cta-title">Ready to Transform Your Business?</p>
<p class="fonts-20 mxw-900">Let's discuss your project and explore how we can help you achieve your digital goals with cutting-edge web solutions.</p>
</div>
<div class="new-button-group">
${statsHtml}</div>
<div class="col-md-12 text-center mt-4 d-flex justify-content-center two-btn-group"><button class="btn btn-pop open-qouteform" type="button" data-medium="B_2">Start Your Project</button> <a class="btn btn-pop open-qouteform white-btn" href="/project/">View Portfolio</a></div>
</div>
</div>
</div>
</section>`;
    }
    
    if (content.stats && content.stats.length > 0) {
        content.stats.slice(0, 4).forEach((stat, index) => {
            const imgSrc = statImages[index] || statImages[0];
            const parts = stat.split(' ');
            const number = parts[0];
            const text = parts.slice(1).join(' ');
            
            statsHtml += `    <div class="new-button-group-inner">
        <img src="${imgSrc}">
        <strong>${number}</strong> ${text}
    </div>
`;
        });
    }

    const template = `<section class="pt50 pb80 new-cta-section section-cta-two">
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
</section>`;

    return template
        .replace('{title}', content.title || 'Ready to Build a Web Solution That Drives Results?')
        .replace('{description}', content.description || 'Whether you\'re a startup or an enterprise, we offer fully customized web development services.')
        .replace('{stats_html}', statsHtml);
}