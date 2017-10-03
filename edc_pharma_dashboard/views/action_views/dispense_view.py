from edc_pharma.dispense import Dispense

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .base_action_view import BaseActionView


app_config = django_apps.get_app_config('edc_pharma_dashboard')


class DispenseView(BaseActionView):

    post_url_name = app_config.dispense_listboard_url_name
    valid_form_actions = ['print_labels']
    action_name = 'pharma'

    dispense_cls = Dispense

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def process_form_action(self):
        if self.action == 'print_labels':
            self.dispense_cls(
                subject_identifier='',
                timepoint_id='',
            )

    @property
    def dispenses(self):
        return self.dispense_model.objects.filter(
            processed=True, pk__in=self.selected_items)