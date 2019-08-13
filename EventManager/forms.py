from django import forms

from EventManager.models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'category', 'place', 'address', 'startDate', 'finishDate', 'eventType')