from django import forms


class ContactUs(forms.Form):
    name = forms.CharField()
    phone = forms.IntegerField
    subject = forms.CharField()
    message = forms.Textarea()