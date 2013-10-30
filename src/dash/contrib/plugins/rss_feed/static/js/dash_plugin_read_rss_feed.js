/*
    Document   : dash_plugin_read_rss_feed.js
    Created on : Aug 29, 2013, 01:52:07 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        RSS plugin specific scripts for django-dash.
*/
;

var RRF_widgetID;
var RRF_URL;
var RRF_csrfToken;
var RRF_feedURL;
var RRF_customFeedTitle;
var RRF_showFeedTitle;
var RRF_maxItems;
var RRF_truncateAfter;
var RRF_cacheFor;

var RRF_getFeed = function(widgetID, url, csrfToken, feedURL, customFeedTitle, showFeedTitle, maxItems, truncateAfter, cacheFor) {
    RRF_widgetID = widgetID;
    RRF_URL = url;
    RRF_csrfToken = csrfToken;
    RRF_feedURL = feedURL;
    RRF_customFeedTitle = customFeedTitle;
    RRF_showFeedTitle = showFeedTitle;
    RRF_maxItems = maxItems;
    RRF_truncateAfter = truncateAfter;
    RRF_cacheFor = cacheFor;
};

$(document).ready(function() {
    var postData = {
        'csrfmiddlewaretoken': RRF_csrfToken,
        'feed_url': RRF_feedURL,
        'custom_feed_title': RRF_customFeedTitle,
        'show_feed_title': RRF_showFeedTitle,
        'max_items': RRF_maxItems,
        'truncate_after': RRF_truncateAfter,
        'cache_for': RRF_cacheFor
    };

    $.post(RRF_URL, postData, function(data) {
        $('#' + RRF_widgetID + ' .plugin-content-wrapper').html(data);
    });
});
