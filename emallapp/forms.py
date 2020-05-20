from django import forms
from emallapp.models import Register


class regForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
