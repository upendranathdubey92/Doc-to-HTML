// Sections Loader - Includes all section generation functions
// This file loads all the individual section files and provides a unified interface

// Section Generation Functions Loader
const SectionsLoader = {
    // Load all section functions
    async loadAllSections() {
        try {
            // Note: In a browser environment, you'll need to include each script file separately
            // This is a reference for the sections that should be loaded
            
            const sectionFiles = [
                'hero_banner/hero_banner.js',
                'faq/faq.js',
                'cta_simple/cta_simple.js',
                'cta_with_list/cta_with_list.js',
                'technology_stack/technology_stack.js',
                'industries_we_serve/industries_we_serve.js',
                'services_grid/services_grid.js',
                'services_accordion/services_accordion.js',
                'portfolio/portfolio.js',
                'testimonial/testimonial.js',
                'benefits/benefits.js',
                'benefits_two/benefits_two.js',
                'content_with_form/content_with_form.js',
                'process/process.js',
                'featured_in/featured_in.js'
            ];
            
            console.log('Section files to be loaded:', sectionFiles);
            return sectionFiles;
            
        } catch (error) {
            console.error('Error loading sections:', error);
            return [];
        }
    },
    
    // Generate section HTML using the appropriate function
    generateSection(sectionType, content) {
        const baseSectionType = sectionType.replace(/_\d+$/, '');
        console.log('🎯 GENERATE SECTION CALLED:', sectionType);
        console.log('🎯 Base section type:', baseSectionType);
        
        // Route to appropriate section generator
        if (baseSectionType.includes('HERO_BANNER_SECTION')) {
            return generateHeroSection(content);
        } else if (baseSectionType.includes('FAQ_SECTION')) {
            return generateFaqSection(content);
        } else if (baseSectionType.includes('CTA_WITH_LIST_SECTION')) {
            return generateCtaTwoSection(content);
        } else if (baseSectionType.includes('CTA_SIMPLE_SECTION')) {
            return generateCtaSection(content);
        } else if (baseSectionType.includes('TECHNOLOGY_STACK_SECTION')) {
            return generateTechnologySection(content);
        } else if (baseSectionType.includes('INDUSTRIES_WE_SERVE_SECTION')) {
            return generateIndustriesSection(content);
        } else if (baseSectionType.includes('SERVICES_GRID_SECTION')) {
            return generateServicesGridSection(content);
        } else if (baseSectionType.includes('SERVICES_ACCORDION_SECTION')) {
            return generateServicesAccordionSection(content);
        } else if (baseSectionType.includes('PORTFOLIO_SECTION')) {
            return generatePortfolioSection(content);
        } else if (baseSectionType.includes('TESTIMONIAL_SECTION')) {
            return generateTestimonialSection(content);
        } else if (baseSectionType.includes('BENEFITS_TWO')) {
            return generateBenefitsTwoSection(content);
        } else if (baseSectionType.includes('BENEFITS_SECTION')) {
            return generateBenefitsSection(content);
        } else if (baseSectionType.includes('CONTENT_WITH_FORM_SECTION')) {
            return generateContentFormSection(content);
        } else if (baseSectionType.includes('PROCESS_SECTION')) {
            return generateProcessSection(content);
        } else if (baseSectionType.includes('FEATURED_IN_SECTION')) {
            return generateFeaturedInSection(content);
        } else {
            console.warn('Unknown section type:', baseSectionType);
            return `<!-- Unknown section type: ${baseSectionType} -->`;
        }
    }
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SectionsLoader;
}