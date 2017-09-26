from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper

app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.dispense_model
    next_url_name = app_config.dispense_listboard_url_name
    querystring_attrs = ['subject_visit']

    @property
    def subject_visit(self):
        return self.object.subject_visit.id
