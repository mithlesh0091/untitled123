#
#
# from .models import *
# from django import forms
#
# class reg_sign(forms.ModelsForm):
#     School_Name = forms.CharFeild(widget=forms.TextInput(),required=True,max_length=100)
#     Cant_find_your_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Contact_person_Name = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Designation_at_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Password1 = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Password2 = forms.CharFeild(widget=forms.EmailFeild(), required=True, max_length=100)
#     Email = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Mobile_No = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#
#     class Meta():
#         model = reg_sign
#         fields = ['School_Name','Cant_find_your_School','Contact_person_Name','Designation_at_Schoo','Password','Password2','Email','Mobile_No']
#
#
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError




from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)