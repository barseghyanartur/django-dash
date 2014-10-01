/*
    Document   : dash.js
    Created on : Aug 18, 2013, 1:24:11 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Django-dash main scripts.
*/
;
$(document).ready(function() {
    var onLightboxOpen = function() {
        $('.submenu').hide();
    };

    var onLightboxAddPluginOpen = function() {
        $('.submenu').hide();
        $( "#accordion" ).accordion({heightStyle: "content"});
    };

    // By concept (we don't want to load things in an iframe), we only show shortcut views in AJAX overlays.
    // All main views are shown as stand-alone pages.

    // Add dashboard plugin.
    $('.add-plugin').colorbox({
        'width': '576px',
        'height': '550px',
        'opacity': '0.5',
        'onComplete': onLightboxAddPluginOpen
    });

    // Show all workspaces.
    $('.menu-dashboard-workspaces').colorbox({
        'width': '576px',
        'height': '400px',
        'opacity': '0.5',
        'onComplete': onLightboxOpen
    });

    // Handling AJAX delete plugin widget requests.
    $('.remove-plugin').bind('click', function() {
        var el = $(this);
        $.getJSON($(this).attr('href'), function(data) {
            if (data.success) {
                el.parent('.plugin').remove();
            }
        });
        return false;
    });

    // Submenu.
    $('.menu-dashboard-settings').bind('click', function() {
        $('.submenu').toggle();
    });

    // Create dashboard workspace.
    $('a.menu-dashboard-create-workspace').colorbox({
        'width': '576px',
        'height': '420px',
        'opacity': '0.5',
        'onComplete': onLightboxOpen
    });

    // Edit dashboard workspace.
    $('a.menu-dashboard-edit-workspace').colorbox({
        'width': '576px',
        'height': '420px',
        'opacity': '0.5',
        'onComplete': onLightboxOpen
    });

    // Edit dashboard settings
    $('a.menu-dashboard-edit-settings').colorbox({
        'width': '576px',
        'height': '570px',
        'opacity': '0.5',
        'onComplete': onLightboxOpen
    });

    // Delete dashboard workspace.
    $('a.menu-dashboard-delete-workspace').colorbox({
        'width': '576px',
        'height': '300px',
        'opacity': '0.5',
        'onComplete': onLightboxOpen
    });
});
