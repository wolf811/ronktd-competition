from captcha.fields import CaptchaField
from django import forms

from seminar.models import SParticipant


class SParticipantForm(forms.ModelForm):
    captcha = CaptchaField()
    promocode = forms.CharField(max_length=100)

    class Meta:
        model = SParticipant
        exclude = ["json_data"]
