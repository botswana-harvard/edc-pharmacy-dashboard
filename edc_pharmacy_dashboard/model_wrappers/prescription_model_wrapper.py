from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper
from edc_pharmacy import AppointmentDescriber


app_config = django_apps.get_app_config('edc_pharmacy_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class PrescriptionModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.prescription_model
    next_url_name = app_config.prescription_listboard_url_name
    querystring_attrs = ['subject_identifier']

    @property
    def dispense_appt_describe(self):
        appt_describe = AppointmentDescriber(
            dispense_appointment=self.object.dispense_appointment)
        return appt_describe

    @property
    def subject_identifier(self):
        return self.object.subject_identifier

    @property
    def is_pending(self):
        return (
            self.dispense_appt_describe.is_next_pending_appointment()
            and not self.object.is_approved)