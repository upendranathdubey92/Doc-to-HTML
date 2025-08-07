/**
 * Technology Stack Section Generator
 * Generates technology stack section with categories and technology icons
 * Supports default content when no technologies are provided
 */
function generateTechnologySection(content) {
    // Handle empty content with default static HTML using your exact format
    if (!content || !content.categories || content.categories.length === 0) {
        return `<div class="technology-stack pt80 pb60 bg-color">
<div class="container-xl">
<div class="row">
<div class="col-md-12">
<h2 class="fonts-40 text-center font-weight-bold mb-5">Technology Stack for Web Development</h2>
</div>
</div>
<div class="technology-inner">
<div class="row">
<div class="col-md-2">
<div class="technology-name fonts-20">Frontend Technologies</div>
</div>
<div class="col-md-10">
<ul class="technology-icon-wrapper">
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/React.svg" alt="React" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> React</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Vue.svg" alt="Vue.js" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Vue.js</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Angular.svg" alt="Angular" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Angular</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Next-js.svg" alt="Next.js" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Next.js</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/TypeScript.svg" alt="TypeScript" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> TypeScript</li>
</ul>
</div>
</div>
<div class="row">
<div class="col-md-2">
<div class="technology-name fonts-20">Backend Technologies</div>
</div>
<div class="col-md-10">
<ul class="technology-icon-wrapper">
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Node-js.svg" alt="Node.js" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Node.js</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Python.svg" alt="Python" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Python</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Django.svg" alt="Django" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Django</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/PHP.svg" alt="PHP" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> PHP</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Laravel.svg" alt="Laravel" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="this.src='https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg'"/> Laravel</li>
</ul>
</div>
</div>
<div class="row">
<div class="col-md-2">
<div class="technology-name fonts-20">Database</div>
</div>
<div class="col-md-10">
<ul class="technology-icon-wrapper">
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/PostgreSQL.svg" alt="PostgreSQL" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> PostgreSQL</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/MongoDB.svg" alt="MongoDB" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> MongoDB</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/MySQL.svg" alt="MySQL" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> MySQL</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Redis.svg" alt="Redis" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> Redis</li>
</ul>
</div>
</div>
<div class="row">
<div class="col-md-2">
<div class="technology-name fonts-20">Cloud & DevOps</div>
</div>
<div class="col-md-10">
<ul class="technology-icon-wrapper">
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/AWS.svg" alt="AWS" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> AWS</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Google-Cloud.svg" alt="Google Cloud" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> Google Cloud</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Docker.svg" alt="Docker" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> Docker</li>
<li><img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Kubernetes.svg" alt="Kubernetes" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> Kubernetes</li>
</ul>
</div>
</div>
</div>
</div>
</div>`;
    }
    
    // If categories are provided, generate dynamic HTML
    if (content && content.categories && content.categories.length > 0) {
        let categoriesHTML = '';
        content.categories.forEach(category => {
            let techList = '';
            if (category.technologies && category.technologies.length > 0) {
                category.technologies.forEach(tech => {
                    // Create a more robust tech slug and provide fallback
                    const techSlug = tech.toLowerCase()
                        .replace(/\./g, '')
                        .replace(/\s+/g, '-')
                        .replace(/[^a-z0-9-]/g, '');
                    
                    // Try different possible paths for tech icons
                    const possiblePaths = [
                        `https://www.spaceotechnologies.com/wp-content/uploads/2023/08/${tech}.svg`,
                        `https://www.spaceotechnologies.com/wp-content/uploads/2024/02/${tech}.svg`,
                        `https://www.spaceotechnologies.com/wp-content/uploads/2023/08/${techSlug}.svg`,
                        `https://www.spaceotechnologies.com/wp-content/uploads/2024/02/${techSlug}.svg`,
                        // Fallback placeholder
                        `https://www.spaceotechnologies.com/wp-content/uploads/2023/08/default-tech.svg`
                    ];
                    
                    // Use the first path as primary with global error handler
                    techList += `<li><img src="${possiblePaths[0]}" alt="${tech}" class="alignnone size-full wp-image-201587" width="24" height="24" onerror="handleImageError(this)"/> ${tech}</li>
`;
                });
            }
            
            categoriesHTML += `<div class="row">
<div class="col-md-2">
<div class="technology-name fonts-20">${category.name}</div>
</div>
<div class="col-md-10">
<ul class="technology-icon-wrapper">
${techList}</ul>
</div>
</div>
`;
        });
        
        return `<div class="technology-stack pt80 pb60 bg-color">
<div class="container-xl">
<div class="row">
<div class="col-md-12">
<h2 class="fonts-40 text-center font-weight-bold mb-5">${content.main_heading || 'Technology Stack'}</h2>
</div>
</div>
<div class="technology-inner">
${categoriesHTML}</div>
</div>
</div>`;
    }

    // Legacy fallback for old format
    const template = `<section class="pt70 pb40 technology-section bg-light section-technology">
<div class="container-xl">
<div class="row">
<div class="col-lg-12 text-center">
<h2 class="fonts-45 mb-3 font-weight-bold">{main_heading}</h2>
<p class="fonts-18 mb-5">{description}</p>
</div>
</div>
<div class="row">
<div class="col-lg-12">
<div class="tech-stack">
{tech_items}
</div>
</div>
</div>
</div>
</section>`;

    let techItems = '';
    if (content && content.technologies) {
        content.technologies.forEach(tech => {
            techItems += `<span class="tech-item badge badge-primary mr-2 mb-2 fonts-16">${tech}</span>
`;
        });
    }

    return template
        .replace('{main_heading}', (content && content.main_heading) || 'Technology Stack')
        .replace('{description}', (content && content.description) || 'Technologies we use')
        .replace('{tech_items}', techItems);
}