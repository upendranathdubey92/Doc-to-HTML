/**
 * Process Section Generator
 * Generates development/business process steps with numbered cards
 * Supports default content when no processes are provided
 */
function generateProcessSection(content) {
    // If no processes provided or empty content, return default process HTML
    if (!content.processes || content.processes.length === 0) {
        console.log('🚀 RETURNING DEFAULT PROCESS HTML (blank content detected)');
        return `<section class="pt80 pb50 process-sec bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center">Our Development Process</h2>
<div class="row">
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">01</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Requirement Analysis</h3>
<p>We learn about your requirements and what you need. Our team proposes solutions to meet your business needs.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">02</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Planning & Strategy</h3>
<p>We create detailed plans and strategies for your project. Our team makes roadmap based on your requirements.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">03</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Design & Development</h3>
<p>Our designers and developers work together to create your solution with modern technologies and best practices.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">04</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Testing & QA</h3>
<p>Our QA team thoroughly tests your solution. We make sure it is 100% bug-free before delivery.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">05</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Deployment</h3>
<p>We deploy your solution and provide complete support during the launch process.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">06</p>
<h3 class="font-weight-semibold fonts-20 mb-2">Support & Maintenance</h3>
<p>We provide ongoing support and maintenance to ensure your solution runs smoothly.</p>
</div>
</div>
</div>
</div>
</section>`;
    }
    
    let processItems = '';
    if (content.processes && content.processes.length > 0) {
        content.processes.forEach((process, index) => {
            const stepNumber = String(index + 1).padStart(2, '0');
            processItems += `<div class="col-lg-4 col-md-6">
<div class="instalikeapp">
<p class="number">${stepNumber}</p>
<h3 class="font-weight-semibold fonts-20 mb-2">${process.title}</h3>
<p>${process.description}</p>
</div>
</div>
`;
        });
    }

    const template = `<section class="pt80 pb50 process-sec bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center">{main_heading}</h2>
<div class="row">
{process_items}
</div>
</div>
</section>`;

    return template
        .replace('{main_heading}', content.main_heading || 'Our Development Process')
        .replace('{process_items}', processItems);
}