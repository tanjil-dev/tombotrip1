from django import forms
from django.forms import ModelForm

from home.models import Supply, Reservation


class SupplyDetailsForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    location = forms.CharField()

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('confirm',)


class MessageForm(forms.Form):
    message = forms.CharField()

class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )

class MyAdvertiseForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'