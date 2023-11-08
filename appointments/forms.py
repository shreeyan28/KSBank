from django.forms import ModelForm

from appointments.models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'reason']
