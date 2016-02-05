import autocomplete_light.shortcuts as al

from dash.models import DashboardPlugin

""" For Dash Plugins """
class DashboardPluginAutocomplete(al.AutocompleteModelBase):
    search_fields = ['^plugin_uid']
    model = DashboardPlugin
    choices = DashboardPlugin.objects.all()

    def choices_for_values(self):
        """
            Map Plugin_Uid names to Ids 
        """
        objs = DashboardPlugin.objects.filter(plugin_uid__in=self.values)
        ids = self.choices.filter(pk__in=[x.id for x in objs])
        values = []
        for value in self.values:
            values.append(DashboardPlugin.objects.get(plugin_uid=value).id)
        self.values = values
        return self.order_choices(ids)

al.register(DashboardPluginAutocomplete)
