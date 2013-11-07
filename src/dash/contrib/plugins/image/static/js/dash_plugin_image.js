/*
    Document   : dash_plugin_image.js
    Created on : Nov 6, 2013, 01:56:09 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Image plugin for django-dash.

        The following piece of code insures that images are opened using the lightbox.
*/
;
$(document).ready(function() {
    // Add dashboard plugin.
    $('.pictonic .plugin-content-wrapper a').colorbox({
        'opacity': '0.5'
    });
});
