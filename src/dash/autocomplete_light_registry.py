import autocomplete_light.shortcuts as al

from dash.models import DashboardPlugin


class DashboardPluginAutocomplete(al.AutocompleteModelBase):
    """For Dash Plugins."""

    search_fields = ['^plugin_uid']
    model = DashboardPlugin
    choices = DashboardPlugin.objects.all()
    attrs = {'placeholder': 'Enter Plugin Format...'}

    def choices_for_values(self):
        # On the way out, do the normal.
        try:
            if (self.values and isinstance(self.values[0], int)) \
                    or (isinstance(self.value, int)):

                return super(DashboardPluginAutocomplete,
                             self).choices_for_values()

        # Map Plugin_Uid names to Ids, on the way in.
        except (UnboundLocalError, AttributeError):
            objs = DashboardPlugin.objects.filter(plugin_uid__in=self.values)
            ids = self.choices.filter(pk__in=[x.id for x in objs])
            values = []
            for value in self.values:
                values.append(DashboardPlugin.objects.get(plugin_uid=value).id)
            self.values = values
            return self.order_choices(ids)

    def validate_values(self):
        return True


al.register(DashboardPluginAutocomplete)
