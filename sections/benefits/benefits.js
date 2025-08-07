/**
 * Benefits Section Generator
 * Generates benefits section with icons, titles, and descriptions
 * Supports default content when no benefits are provided
 */
function generateBenefitsSection(content) {
    // Handle empty content with default static HTML using data URI images
    if (!content || !content.benefits || content.benefits.length === 0) {
        return `<section class="pt80 pb50 services-section section-benefits">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3 mxw-1000">Why Choose Our Services</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">We deliver exceptional solutions with proven expertise and dedication to your success.</p>
<div class="row">
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiMwMDc4ZmYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+" alt="Expertise" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">Expert Team</h3>
<p>Skilled professionals with years of experience in modern technologies and best practices.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiMxMGI5ODEiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTkgMTJMMTEgMTRMMTUgMTBNMjEgMTJDMjEgMTYuOTcwNiAxNi45NzA2IDIxIDEyIDIxQzcuMDI5NDQgMjEgMyAxNi45NzA2IDMgMTJDMyA3LjAyOTQ0IDcuMDI5NDQgMyAxMiAzQzE2Ljk3MDYgMyAyMSA3LjAyOTQ0IDIxIDEyWiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+Cjwvc3ZnPg==" alt="Quality" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">Quality Assurance</h3>
<p>Rigorous testing and quality control processes to ensure reliable and bug-free solutions.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiNmNTk0MmYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTUuMDkgOC4yNkwyMiA5TDE2IDEzTDE3LjE4IDIwTDEyIDE2TDYuODIgMjBMOCAxM0wyIDlMOC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+" alt="Support" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">24/7 Support</h3>
<p>Round-the-clock support and maintenance to keep your solutions running smoothly.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiM4YjVjZjYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTMgN0gxMFYxNEgzVjdaTTE0IDdIMjFWMTBIMTRWN1pNMTQgMTRIMjFWMTdIMTRWMTRaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+" alt="Scalability" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">Scalable Solutions</h3>
<p>Build for growth with scalable architecture that adapts to your business needs.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiNlZjQ0NDQiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTMuMjUgOC4yNUwyMCA5TDEzLjc1IDEzLjc1TDE0IDIxTDEyIDE5TDEwIDIxTDEwLjI1IDEzLjc1TDQgOUwxMC43NSA4LjI1TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+" alt="Innovation" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">Innovation</h3>
<p>Stay ahead with cutting-edge technologies and innovative approaches to solve challenges.</p>
</div>
</div>
<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiM2MzY2ZjEiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJWNE0xMiAyMFYyMk00LjIyIDQuMjJMNS42NCA1LjY0TTE4LjM2IDE4LjM2TDE5Ljc4IDE5Ljc4TTIgMTJINE0yMCAxMkgyMk00LjIyIDE5Ljc4TDUuNjQgMTguMzZNMTguMzYgNS42NEwxOS43OCA0LjIyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4KPC9zdmc+" alt="Delivery" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">On-time Delivery</h3>
<p>Committed to delivering projects on schedule without compromising on quality.</p>
</div>
</div>
</div>
</div>
</section>`;
    }
    
    const template = `<section class="pt80 pb50 services-section section-benefits">
<div class="container-xl">
<h2 class="fonts-40 font-weight-bold text-center mb-3 mxw-1000">{main_heading}</h2>
<p class="fonts-18 text-center mxw-1000 mb-4">{description}</p>
<div class="row">
{benefits_items}
</div>
</div>
</section>`;

    let benefitsItems = '';
    if (content.benefits) {
        content.benefits.forEach((benefit, index) => {
            // Use static data URI images that will never break
            const staticDataImages = [
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiMwMDc4ZmYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+`, // Expertise - Blue star
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiMxMGI5ODEiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTkgMTJMMTEgMTRMMTUgMTBNMjEgMTJDMjEgMTYuOTcwNiAxNi45NzA2IDIxIDEyIDIxQzcuMDI5NDQgMjEgMyAxNi45NzA2IDMgMTJDMyA3LjAyOTQ0IDcuMDI5NDQgMyAxMiAzQzE2Ljk3MDYgMyAyMSA3LjAyOTQ0IDIxIDEyWiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+Cjwvc3ZnPg==`, // Quality - Green checkmark
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiNmNTk0MmYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTUuMDkgOC4yNkwyMiA5TDE2IDEzTDE3LjE4IDIwTDEyIDE2TDYuODIgMjBMOCAxM0wyIDlMOC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+`, // Support - Orange star
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiM4YjVjZjYiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTMgN0gxMFYxNEgzVjdaTTE0IDdIMjFWMTBIMTRWN1pNMTQgMTRIMjFWMTdIMTRWMTRaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+`, // Scalability - Purple blocks
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiNlZjQ0NDQiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJMMTMuMjUgOC4yNUwyMCA5TDEzLjc1IDEzLjc1TDE0IDIxTDEyIDE5TDEwIDIxTDEwLjI1IDEzLjc1TDQgOUwxMC43NSA4LjI1TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4KPC9zdmc+`, // Innovation - Red star
                `data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQiIGhlaWdodD0iNzQiIHZpZXdCb3g9IjAgMCA3NCA3NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzciIGN5PSIzNyIgcj0iMzciIGZpbGw9IiM2MzY2ZjEiLz4KPHN2ZyB4PSIyMCIgeT0iMjAiIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KPHBhdGggZD0iTTEyIDJWNE0xMiAyMFYyMk00LjIyIDQuMjJMNS42NCA1LjY0TTE4LjM2IDE4LjM2TDE5Ljc4IDE5Ljc4TTIgMTJINE0yMCAxMkgyMk00LjIyIDE5Ljc4TDUuNjQgMTguMzZNMTguMzYgNS42NEwxOS43OCA0LjIyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4KPC9zdmc+` // Delivery - Indigo clock
            ];
            
            const imageUrl = staticDataImages[index % staticDataImages.length];
            const altText = benefit.title || `Benefit ${index + 1}`;
            
            benefitsItems += `<div class="col-lg-4 col-md-6">
<div class="mad_service_box text-center">
<img loading="lazy" decoding="async" src="${imageUrl}" alt="${altText}" width="74" height="74">
<h3 class="fonts-18 font-weight-semibold">${benefit.title}</h3>
<p>${benefit.description}</p>
</div>
</div>
`;
        });
    }

    return template
        .replace('{main_heading}', content.main_heading || 'Key Benefits')
        .replace('{description}', content.description || 'Why choose us')
        .replace('{benefits_items}', benefitsItems);
}