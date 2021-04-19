from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import TextInput, EmailInput, Select, FileInput
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=30,label= 'User Name :')
    # email = forms.EmailField(max_length=200,label= 'Email :')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter User Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email',
            }
        ) 
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


    

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = ('phone', 'address', 'age','image')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address'   : TextInput(attrs={'class': 'input','placeholder':'address'}),
            'age'      : TextInput(attrs={'class': 'input','placeholder':'age'}),
            'image'     : FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }        