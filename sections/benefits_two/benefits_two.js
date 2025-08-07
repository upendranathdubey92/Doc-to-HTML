/**
 * Benefits Two Section Generator
 * Generates benefits section with simple title/description format
 * No icons, just text-based benefits
 */
function generateBenefitsTwoSection(content) {
    const template = `<section class="pt80 pb50 services-section practices-we-follow section-benefits-two">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3">{main_heading}</h2>
<p class="fonts-18 text-center mxw-900 mb-4">{description}</p>
<div class="row">
{benefits_items}
</div>
</div>
</section>`;

    let benefitsItems = '';
    if (content.benefits) {
        content.benefits.slice(0, 6).forEach(benefit => {
            benefitsItems += `    <div class="col-lg-4 col-md-6">
        <div class="mad_service_box">
            <h3 class="fonts-18 font-weight-semibold">${benefit.title}</h3>
            ${benefit.description}
        </div>
    </div>
`;
        });
    }

    return template
        .replace('{main_heading}', content.main_heading || 'Why Choose Space-O Technologies')
        .replace('{description}', content.description || 'Partner with us for expert web development consulting.')
        .replace('{benefits_items}', benefitsItems);
}