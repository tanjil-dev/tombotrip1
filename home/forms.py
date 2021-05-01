from django import forms
from django.forms import ModelForm

from home.models import Supply, Reservation,ProductAttribute


class SupplyDetailsForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": 'date'})
    )
    location = forms.CharField()

    traveller = forms.IntegerField()

    phone = forms.CharField(max_length=11)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('confirm',)


class MessageForm(forms.Form):
    message = forms.CharField()
    email = forms.EmailField()

class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )

class MyProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        exclude=('supply',)

class MyAdvertiseForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'
        exclude = ('user','price', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', 'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17')
        # widgets = {
        #     'description': Textarea(attrs={'cols': 25, 'rows': 6}),
        #     'visit_date': DateInput(attrs={"type": 'date'}),
        # }