from django import forms
from emallapp.models import Register,payment


class regForm(forms.ModelForm):
    class Meta:
        model = Register

        fields = '__all__'
class payForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
