from django import forms

from .models import Room


class RoomForm(forms.Form):
    end_date = forms.DateField(widget=forms.SelectDateWidget)
