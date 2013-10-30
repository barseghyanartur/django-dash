/*
    Document   : dash_plugin_url_form.js
    Created on : Sep 25, 2013, 00:18:34 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        URL plugin for django-dash.

        The following piece of code creates a div with font-awesome
        images, that come from the form.
*/
;
$(document).ready(function() {
    // All options into an array
    var options = $('select.image-picker option');
    var selectedValue = $('select.image-picker option:selected').val();
    var values = $.map(options, function(option) {
        if (!option.value) {
            return '';
        }
        var selected = (selectedValue == option.value) ? ' class="selected"' : '';
        return '<a href="javascript:;"' + selected + '><i class="' + option.value + '"></i></a>';
    });

    // Insert a div with images after the select
    $('select.image-picker').after('<div class="pick-images">' + values.join('') + '</div>');

    // Event handler click on image
    $('.pick-images').on('click', 'a', function() {
        var el = $(this);
        var imageClass = el.find('i').attr('class');
        $('select.image-picker').val(imageClass).trigger('change');
        $('.pick-images a').removeAttr('class');
        el.addClass('selected');
    });

    // Event handler select click
    $('select.image-picker').change(function() {
        // Empty choice. Remove selected and return.
        if (!this.value) {
            $('.pick-images a').removeAttr('class');
            return;
        }

        // Some image was chosen. Mark the chosen image as selected.
        var imageSelected = $('.pick-images a i.' + this.value);
        if (imageSelected.length) {
            $('.pick-images a').removeAttr('class');
            imageSelected.parents().addClass('selected');
        }
    });
});
