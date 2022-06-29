# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
#
#
# class loginform(forms.Form):
#     username = forms.CharField(max_length=50)
#     password= forms.CharField(widget=forms.PasswordInput)
#     # class Meta:
#     #     model = User
#     #     fields = ['username', 'password1', 'password2']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        # excludes private information from User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), )
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''