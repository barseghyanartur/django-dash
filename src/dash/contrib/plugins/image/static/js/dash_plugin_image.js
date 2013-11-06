/*
    Document   : dash_plugin_url_form.js
    Created on : Nov 6, 2013, 01:56:09 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Image plugin for django-dash.

        The following piece of code insures that images are opened using the lightbox.
*/
;
$(document).ready(function() {
    // Add dashboard plugin.
    $('.lightboxonic').colorbox({
        'opacity': '0.5'
    });
    
});
