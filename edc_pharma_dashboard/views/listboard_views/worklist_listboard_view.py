from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_pharma_dashboard.model_wrappers import WorklistModelWrapper
from edc_pharma_dashboard.views.listboard_filters import WorklistListboardViewFilters
from .base_listboard import BaseListboardView


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class WorklistListboardView(BaseListboardView):

    navbar_item_selected = 'worklist'

    model = edc_pharma_app_config.worklist_model
    model_wrapper_cls = WorklistModelWrapper
    listboard_url_name = app_config.worklist_listboard_url_name
    listboard_template_name = app_config.worklist_listboard_template_name
    prescription_listboard_url_name = app_config.appointment_listboard_url_name
    show_all = True
    listboard_view_filters = WorklistListboardViewFilters()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            listboard_url_name=self.listboard_url_name,
            prescription_listboard_url_name=self.prescription_listboard_url_name)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        return options
