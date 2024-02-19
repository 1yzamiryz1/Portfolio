from captcha.fields import CaptchaField
from django import forms

from main.models import Contact, Certificate


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = "__all__"


class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = "__all__"

