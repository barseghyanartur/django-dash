from django.db import models

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'OrderField',
)


class OrderField(models.IntegerField):
    """OrderField.

    @author http://djangosnippets.org/users/zenx/
    @source http://djangosnippets.org/snippets/1861/

    OrderField for models from
    //ianonpython.blogspot.com/2008/08/orderfield-for-django-models.html and
    updated to use a django aggregation function. This field sets a default
    value as an auto-increment of the maximum value of the field +1.

    Ignores the incoming value and instead gets the maximum plus one of the
    field.

    This works really well in combination with "sortable_list.js". There are
    several things you should know:

        * order field shall be null=True, blank=True
        * order field shall not be unique

    If above mentioned is True, you can use jQuery drag-n-drop widget in
    your Django-admin.

    See the following example:

    >>> class Media:  # This belongs to your Admin class (admin.ModelAdmin)
    >>>     js = [
    >>>         '/media/js/jquery-1.6.2.min.js',
    >>>         '/media/js/jquery-ui-1.8.16.custom.min.js',
    >>>         '/media/js/sortable_list.js'
    >>>     ]
    """

    def pre_save(self, model_instance, add):
        # if the model is new and not an update
        if model_instance.pk is None:
            records = model_instance.__class__.objects.aggregate(
                models.Max(self.name)
            )
            if records:
                # get the maximum attribute from the first record and add
                # 1 to it
                try:
                    value = records['{0}__max'.format(self.name)] + 1
                except TypeError:
                    value = 1
            else:
                value = 1
        # otherwise the model is updating, pass the attribute value through
        else:
            value = getattr(model_instance, self.attname)
        return value

    # prevent the field from being displayed in the admin interface
    def formfield_(self, **kwargs):
        return None
