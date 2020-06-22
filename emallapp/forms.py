from django import forms
from emallapp.models import Register,payment,addproduct


class regForm(forms.ModelForm):
    class Meta:
        model = Register

        fields = '__all__'
class payForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'

class productForm(forms.ModelForm):
    class Meta:
        model = addproduct
        fields = '__all__'
