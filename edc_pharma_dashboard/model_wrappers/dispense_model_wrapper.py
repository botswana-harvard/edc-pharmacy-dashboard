from edc_model_wrapper import ModelWrapper
from edc_pharma.models import DispenseAppointment
from edc_pharma.timepoint_descriptor import TimepointDescriptor

from django.apps import apps as django_apps

app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.dispense_model
    next_url_name = app_config.dispense_listboard_url_name
    querystring_attrs = ['subject_identifier', 'sid']

    @property
    def dispense_appointment(self):
        dispense_timepoint = DispenseAppointment.objects.filter(
            schedule__subject_identifier=self.object.subject_identifier,
            is_dispensed=False
        ).order_by('created').first()
        if not dispense_timepoint:
            dispense_timepoint = DispenseAppointment.objects.filter(
                schedule__subject_identifier=self.object.subject_identifier,
                is_dispensed=True
            ).order_by('created').last()
        return dispense_timepoint

    @property
    def dispense_appointment_id(self):
        return str(self.dispense_appointment.id)

    @property
    def dispense_appointment_descriptor(self):
        descriptor = TimepointDescriptor(
            dispense_appointment=self.dispense_appointment)
        return descriptor
