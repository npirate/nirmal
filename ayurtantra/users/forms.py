from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm (UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('age',) will show only username, age and password fields
        fields = ('username', 'email', 'age',) #will show fields that are explicitely defined here.

class CustomUserChangeForm (UserChangeForm):
    class Meta (UserChangeForm.Meta):
        model = CustomUser
        #fields = UserChangeForm.Meta.fields  will show only username and password fields
        fields = ('username', 'email', 'age',)  #will show fields that are explicitely defined here.