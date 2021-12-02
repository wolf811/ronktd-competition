from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from seminar.models import SParticipant


class SParticipantForm(forms.ModelForm):
    captcha = CaptchaField()
    promocode = forms.CharField(max_length=100, required=False)

    class Meta:
        model = SParticipant
        exclude = ["json_data"]

    def clean_pdn_accepted(self):
        data = self.cleaned_data["pdn_accepted"]
        if not data:
            raise ValidationError(
                "Необходимо принять правила обработки персональных данных..."
            )
        return data
