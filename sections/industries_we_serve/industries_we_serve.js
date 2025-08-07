/**
 * Industries We Serve Section Generator
 * Generates industries section with icons and industry categories
 * Supports default content when no industries are provided
 */
function generateIndustriesSection(content) {
    // ALWAYS return the exact static HTML for blank/empty/image content
    if (!content.industries || content.industries.length === 0) {
        console.log('🚀 RETURNING EXACT STATIC INDUSTRIES HTML (blank content detected)');
        return `<section class="pt80 pb60 industries-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-4 col-md-12">
<div class="industries-desc">
<h2 class="fonts-40 font-weight-bold font-weight-bold mb-2">Industries We Serve</h2>
<p>Whether you operate in healthcare, finance, eCommerce, or any other domain, we develop and integrate mobile innovations that enhance workflows, address industry regulations, and deliver optimal digital experiences for your customers and stakeholders.</p>
</div>
</div>
<div class="col-lg-8 col-md-12 industries-category">
<div class="row text-center">
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/Photo-Video.svg" alt="Photo Video" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/photo-editing-app-development/">Photo &amp; Video</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/Social-Networking.svg" alt="Social Networking" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/instagram-like-app-development/">Social Networking</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/On-Demand-Delivery.svg" alt="On Demand Delivery" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/on-demand-app-development/">On-Demand Delivery</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/Entertainment.svg" alt="Entertainment" width="64" height="64">
<p class="fonts-16">Entertainment</p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/Health-Fitness.svg" alt="Health-Fitness" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/solution/healthcare-app-development/">Health &amp; Fitness</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/09/Food-Drink.svg" alt="Manufacturing" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/zomato-like-restaurant-app-development/">Food &amp; Drink</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Transportation.svg" alt="Transportation" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/solution/enterprise-fleet-management/">Transportation &amp; Logistics</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Education.svg" alt="Education" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/solution/mobile-apps-for-schools/">Education &amp; Elearning</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/11/Ecommerce-Shopping.svg" alt="Hospitality" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/ecommerce-website-development/">Ecommerce &amp; Shopping</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Finance.svg" alt="Finance" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/financial-software-development/">Banking &amp; Finance</a></p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Travel.svg" alt="Travel" width="64" height="64">
<p class="fonts-16">Travel &amp; Tourism</p>
</div>
</div>
<div class="col-lg-3 col-md-4 col-sm-6 col-6">
<div class="industries-box">
<img decoding="async" loading="lazy" src="https://www.spaceotechnologies.com/wp-content/uploads/2023/08/Real-estate.svg" alt="Real-estate" width="64" height="64">
<p class="fonts-16"><a href="https://www.spaceotechnologies.com/services/real-estate-app-development/">Real Estate</a></p>
</div>
</div>
</div>
</div>
</div>
</div>
</section>`;
    }

    // If custom industries are provided, generate dynamic HTML (this would need custom parsing logic)
    const template = `<section class="pt80 pb60 industries-section">
<div class="container-xl">
<div class="row">
<div class="col-lg-4 col-md-12">
<div class="industries-desc">
<h2 class="fonts-40 font-weight-bold font-weight-bold mb-2">{main_heading}</h2>
<p>{description}</p>
</div>
</div>
<div class="col-lg-8 col-md-12 industries-category">
<div class="row text-center">
{industry_items}
</div>
</div>
</div>
</div>
</section>`;

    return template
        .replace('{main_heading}', content.main_heading || 'Industries We Serve')
        .replace('{description}', content.description || 'We serve various industries')
        .replace('{industry_items}', '<!-- Custom industries would go here -->');
}