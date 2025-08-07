/**
 * Content with Form Section Generator
 * Generates content section with contact form on the right side
 * Supports bullet points and descriptive content
 */
function generateContentFormSection(content) {
    let bulletHtml = '';
    if (content.bullet_points && content.bullet_points.length > 0) {
        bulletHtml = `<strong>${content.bullet_intro || 'Key Points:'}</strong>\n<ul class="bullet fonts-14 mb-3">\n`;
        for (let bullet of content.bullet_points) {
            bulletHtml += `<li>${bullet}</li>\n`;
        }
        bulletHtml += '</ul>';
    }

    const template = `<section class="pt80 pb80 text-form-section bg-color section-content-form">
<div class="container-xl">
<div class="row">
<div class="col-lg-7 col-md-12 col-sm-12">
<h2 class="fonts-40 font-weight-bold text-left mb-4">{main_heading}</h2>
<p>{description}</p>
{bullet_html}
</div>
<div class="col-lg-5 col-md-12 col-sm-12 text-center">
<div class="homen_form">
<p class="fonts-24 font-weight-bold mt-0 mb-3 text-center line-height-1 pb-0">Talk to Our Experts Now</p>
<form id="other-form2" class="footer_form append-form blur-form" action="" method="post" name="popup-form" novalidate="">
<div class="row">
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-user"></i><input id="name" class="form-control" name="name" required="" size="40" type="text" value="" placeholder="Name*" data-name="Please enter your name" /><small class="error"></small></p>
<div class="clearfix"></div>
</div>
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-envelope"></i><input id="email" class="form-control" name="email" required="" size="40" type="email" value="" placeholder="Email*" data-name="Please enter your email" /><small class="error"></small></p>
<div class="clearfix"></div>
</div>
</div>
<div class="row">
<div class="form-group col-md-12 input_cover mb-0 text-left">
<p class="mb-2"><i class="fa fa-phone"></i><input id="number" class="form-control" name="number" required="" size="15" type="tel" value="" placeholder="Phone*" data-name="Please enter your number" /><small class="error"></small><span id="error-msg" class="d-none"></span></p>
<div class="clearfix"></div>
</div>
</div>
<div class="row">
<div class="form-group col-md-12 mb-0 text-left"><textarea id="Comment" class="form-control" cols="40" name="comment" required="" rows="3" placeholder="Write your message.*" data-name="Please enter your description"></textarea><small class="error"></small></div>
</div>
<div class="row">
<div class="form-group col-md-12">
<div class="footer_txt_block mt-2">
<input id="form_type" name="form_type" type="hidden" value="footer_form" />
[spaceo_get_permalink][spaceo_get_referal]
<div id="loadingmessage" class="loader"><img src="/wp-content/uploads/2021/04/ajax-loader.gif" alt="Ajax loader" width="30" height="30" /></div>
<input id="submit" class="btn btn-pop mb0" name="submit" type="submit" value="Book Your Consultation Now" data-medium="S_2" />
</div>
</div>
</div>
</form>
</div>
</div>
</div>
</div>
</section>`;

    return template
        .replace('{main_heading}', content.main_heading || 'Contact Us')
        .replace('{description}', content.description || 'Get in touch')
        .replace('{bullet_html}', bulletHtml);
}