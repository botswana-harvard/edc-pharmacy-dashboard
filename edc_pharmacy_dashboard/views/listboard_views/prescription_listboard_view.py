from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ...model_wrappers import PrescriptionModelWrapper
from ..listboard_filters import PrescriptionListboardViewFilters
from .base_listboard import BaseListboardView

app_config = django_apps.get_app_config('edc_pharmacy_dashboard')
edc_pharmacy_app_config = django_apps.get_app_config('edc_pharmacy')


class PrescriptionListboardView(BaseListboardView):

    navbar_item_selected = 'prescription'

    model = edc_pharmacy_app_config.prescription_model
    model_wrapper_cls = PrescriptionModelWrapper
    form_action_url_name = f'edc_pharmacy_dashboard:approve_prescription_url'
    listboard_url_name = app_config.prescription_listboard_url_name
    listboard_template_name = app_config.prescription_listboard_template_name
    appointment_listboard_url_name = app_config.appointment_listboard_url_name
    show_all = True
    listboard_view_filters = PrescriptionListboardViewFilters()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            listboard_url_name=self.listboard_url_name,
            appointment_listboard_url_name=self.appointment_listboard_url_name)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('q'):
            options.update(subject_identifier=kwargs.get('q'))
        return options