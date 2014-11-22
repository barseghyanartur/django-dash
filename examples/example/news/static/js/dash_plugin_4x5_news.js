/*
    Document   : dash_plugin_4x5_news.js
    Created on : Aug 29, 2013, 21:26:23 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        News plugin specific scripts for django-dash.
*/
;

var HN_widgetID;
var HN_URL;
var HN_csrfToken;
var HN_pageURLParam;
var HN_pageNumber;
var HN_maxItemsURLParam;
var HN_maxItems;

var HN_getNews = function(widgetID, url, csrfToken, pageURLParam, pageNumber, maxItemsURLParam, maxItems) {
    HN_widgetID = widgetID;
    HN_URL = url;
    HN_csrfToken = csrfToken;
    HN_pageURLParam = pageURLParam;
    HN_pageNumber = pageNumber;
    HN_maxItemsURLParam = maxItemsURLParam;
    HN_maxItems = maxItems;
};

$(document).ready(function() {
    var postData = {
        'csrfmiddlewaretoken': HN_csrfToken,
        'page': HN_pageNumber,
        'max_items': HN_maxItems
    };

    $.post(HN_URL + '?' + HN_pageURLParam + '=' + HN_pageNumber + '&' + HN_maxItemsURLParam + '=' + HN_maxItems, postData, function(data) {
        $('#' + HN_widgetID + ' .plugin-content-wrapper').html(data);
    });

    $(document).on('click', '.pagination-prev-next .previous, .pagination-prev-next .next', function() {
        var el = $(this);
        $.get(el.attr('href'), {}, function(data) {
            $('#' + HN_widgetID + ' .plugin-content-wrapper').html(data);
        });
        return false;
    })
});
