/**
 * Services Accordion Section Generator
 * Generates services in accordion format with images and expandable content
 * Supports single and multiple sections based on service count
 */
function generateServicesAccordionSection(content) {
    if (!content.services || content.services.length === 0) {
        return '<div>No services found</div>';
    }

    const services = content.services;
    const totalServices = services.length;

    // If 3 or fewer services, use single section
    if (totalServices <= 3) {
        return this.generateSingleAccordionSection(services);
    }

    // If more than 3, split into multiple sections with swapped columns
    return this.generateMultipleAccordionSections(services);
}

function generateSingleAccordionSection(services) {
    const accordionImages = [
        '/wp-content/uploads/2025/07/security-compliance-advisory.svg',
        '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg',
        '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg'
    ];

    const collapseIds = ['one', 'two', 'three'];
    let accordionItems = '';

    services.forEach((service, index) => {
        const imageSrc = accordionImages[index] || accordionImages[0];
        const collapseId = collapseIds[index] || `item_${index}`;
        const isFirst = index === 0;
        const cardHeaderClass = isFirst ? 'card-header active' : 'card-header';
        const collapseClass = isFirst ? 'collapse show' : 'collapse';
        const displayStyle = isFirst ? 'style="display:block;"' : '';
        
        // Generate bullet points if they exist
        let bulletHtml = '';
        if (service.bullets && service.bullets.length > 0) {
            bulletHtml = '<ul class="bullet fonts-14 mb-3">';
            service.bullets.forEach(bullet => {
                bulletHtml += `<li>${bullet}</li>`;
            });
            bulletHtml += '</ul>';
        }
        
        accordionItems += `<div class="card">
<div class="${cardHeaderClass}" ${displayStyle}>
<h3 class="card-link" data-toggle="collapse" href="#${collapseId}"><img src="${imageSrc}" width="34" height="34" alt="${service.title}" class="left-icons" loading="lazy" decoding="async">${service.title}</h3>
<div id="${collapseId}" class="${collapseClass}" data-parent="#accordion">
<div class="card card-body">
<p>${service.description}</p>
${bulletHtml}
</div>
</div>
</div>
</div>
`;
    });

    return `<section class="techno-stack pb80 bg-color services-tab-new section-services-accordion">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
</div>
</div>
</section>`;
}

function generateMultipleAccordionSections(services) {
    // Split services into groups of 3
    const serviceGroups = [];
    for (let i = 0; i < services.length; i += 3) {
        serviceGroups.push(services.slice(i, i + 3));
    }

    let sectionsHtml = '';
    
    serviceGroups.forEach((group, groupIndex) => {
        const accordionImages = [
            '/wp-content/uploads/2025/07/security-compliance-advisory.svg',
            '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg',
            '/wp-content/uploads/2025/07/cloud-infrastructure-planning.svg'
        ];

        const collapseIds = ['one', 'two', 'three'];
        let accordionItems = '';

        group.forEach((service, index) => {
            const imageSrc = accordionImages[index] || accordionImages[0];
            const collapseId = collapseIds[index];
            const isFirst = index === 0;
            const cardHeaderClass = isFirst ? 'card-header active' : 'card-header';
            const collapseClass = isFirst ? 'collapse show' : 'collapse';
            const displayStyle = isFirst ? 'style="display:block;"' : '';
            
            // Generate bullet points if they exist
            let bulletHtml = '';
            if (service.bullets && service.bullets.length > 0) {
                bulletHtml = '<ul class="bullet fonts-14 mb-3">';
                service.bullets.forEach(bullet => {
                    bulletHtml += `<li>${bullet}</li>`;
                });
                bulletHtml += '</ul>';
            }
            
            accordionItems += `<div class="card">
<div class="${cardHeaderClass}" ${displayStyle}>
<h3 class="card-link" data-toggle="collapse" href="#${collapseId}"><img src="${imageSrc}" width="34" height="34" alt="${service.title}" class="left-icons" loading="lazy" decoding="async">${service.title}</h3>
<div id="${collapseId}" class="${collapseClass}" data-parent="#accordion">
<div class="card card-body">
<p>${service.description}</p>
${bulletHtml}
</div>
</div>
</div>
</div>
`;
        });

        // Swap columns for alternating sections (odd sections have swapped layout)
        const isSwapped = groupIndex % 2 === 1;
        
        if (isSwapped) {
            // Swapped: Accordion left, Image right
            sectionsHtml += `<section class="techno-stack pb80 bg-color services-tab-new section-services-accordion">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
</div>
</div>
</section>

`;
        } else {
            // Normal: Image left, Accordion right
            sectionsHtml += `<section class="techno-stack pb80 bg-color services-tab-new section-services-accordion">
<div class="container-xl">
<div class="row">
<div class="col-lg-6">
<div class="left-img">
<img src="/wp-content/uploads/2025/07/security-compliance-advisory.jpg" alt="Security Compliance Advisory" width="630" height="500" loading="lazy" decoding="async">
</div>
</div>
<div class="col-lg-6">
<div id="accordion" class="text-left">
${accordionItems}
</div>
</div>
</div>
</div>
</section>

`;
        }
    });

    return sectionsHtml;
}