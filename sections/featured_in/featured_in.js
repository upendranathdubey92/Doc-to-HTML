/**
 * Featured In Section Generator
 * Generates media recognition section with brand logos
 * Supports default content when no brands are provided
 */
function generateFeaturedInSection(content) {
    console.log('🚀 GENERATE FEATURED_IN CALLED');
    console.log('🚀 Content received:', content);
    console.log('🚀 Brands array:', content.brands);
    console.log('🚀 Brands length:', content.brands ? content.brands.length : 'no brands property');
    
    // ALWAYS return the exact static HTML for blank/empty/image content
    if (!content.brands || content.brands.length === 0) {
        console.log('🚀 RETURNING EXACT STATIC HTML (blank content detected)');
        return `<!-- Featured In Section Start -->
<section class="featured-in pt80 pb80 bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">Our Solutions Recognized & Featured In</h2>
<div class="brand-listing">
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Tech-Crunch.svg" alt="Tech Crunch" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Guardian.svg" alt="The Guardian" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Bloomberg.svg" alt="Bloomberg" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/BBC.svg" alt="BBC" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Business-insider.svg" alt="Business insider" width="200" height="44"/>
</div>
<div class="brand-img">
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Telegraph.svg" alt="The Telegraph" width="200" height="44"/>
</div>
</div>
</div>
</section>
<!-- Featured In Section End -->`;
    }

    // If custom brands are provided, generate dynamic HTML
    const brandImages = {
        'Tech Crunch': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Tech-Crunch.svg',
        'TechCrunch': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Tech-Crunch.svg',
        'The Guardian': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Guardian.svg',
        'Guardian': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Guardian.svg',
        'Bloomberg': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Bloomberg.svg',
        'BBC': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/BBC.svg',
        'Business Insider': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Business-insider.svg',
        'Business insider': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Business-insider.svg',
        'The Telegraph': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Telegraph.svg',
        'Telegraph': 'https://www.spaceotechnologies.com/wp-content/uploads/2023/08/The-Telegraph.svg'
    };

    let brandItems = '';
    content.brands.forEach((brand, index) => {
        const imageSrc = brandImages[brand] || brandImages['Tech Crunch']; // Default fallback
        brandItems += `<div class="brand-img">
<img src="${imageSrc}" alt="${brand}" width="200" height="44"/>
</div>
`;
    });

    const template = `<section class="featured-in pt80 pb80 bg-color">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-5">{main_heading}</h2>
<div class="brand-listing">
{brand_items}
</div>
</div>
</section>`;

    return template
        .replace('{main_heading}', content.main_heading || 'Our Solutions Recognized & Featured In')
        .replace('{brand_items}', brandItems);
}