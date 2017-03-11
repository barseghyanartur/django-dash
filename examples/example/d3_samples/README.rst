==========
d3_samples
==========
Example app for ``django-dash``. Contains sample D3 plugins:

- Bubble Chart, which is based on the original
  `sample <http://bl.ocks.org/mbostock/4063269>`_.
- Stacked-to-Grouped Bars, which is based on the original
  `sample <http://bl.ocks.org/mbostock/3943967>`_.
- Sunburst Partition, which is based on the original
  `sample <http://bl.ocks.org/mbostock/4063423>`_.

Installation
============
Installation steps described below.

#) Add ``d3_samples`` to ``INSTALLED_APPS`` of your Django project settings
   module.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'dash',
            'dash.contrib.layouts.android',
            'dash.contrib.layouts.bootstrap2',
            'dash.contrib.layouts.windows8',
            'dash.contrib.plugins.dummy',
            'dash.contrib.plugins.image',
            'dash.contrib.plugins.memo',
            'dash.contrib.plugins.rss_feed',
            'dash.contrib.plugins.url',
            'dash.contrib.plugins.video',
            'dash.contrib.plugins.weather',
            # ...
            'd3_samples',
            # ...
        )

#) From terminal run

    .. code-block:: sh

        ./manage.py dash_sync_plugins

Usage
=====
- Add the desired sample D3 plugin to your dashboard.

Screen-shots
============
Several screen-shots of the sample D3 plugins (in Bootstrap2 layout) are
presented below.

- Bubble Chart, Stacked-to-Grouped Bars and Sunburst Partition (view dashboard
  mode):

  .. image:: docs/_static/d3_sample_charts_view_dashboard.png
        :align: center
        :width: 900px

- Bubble Chart, Stacked-to-Grouped Bars and Sunburst Partition (edit dashboard
  mode):

  .. image:: docs/_static/d3_sample_charts_edit_dashboard.png
        :align: center
        :width: 900px

License
=======
- The the `d3.js <https://github.com/mbostock/d3/>`_ (JavaScript library) is
  licensed under `BSD <https://github.com/mbostock/d3/blob/master/LICENSE>`_.
- To the rest of the code falls under the license of the `django-dash`.

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
