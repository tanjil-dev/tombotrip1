from django import forms

from home.models import Supply


class SupplyDetailsForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    location = forms.CharField()

class MessageForm(forms.Form):
    message = forms.CharField()

class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )