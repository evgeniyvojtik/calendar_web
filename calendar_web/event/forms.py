from django.db.models import TextField
from django.forms import ModelForm, TextInput, Textarea, DateField, DateInput

from event.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_text', 'date']
        widgets = {'event_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name of event'}),
                   'event_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description of event'}),
                   "date": DateInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}), }
