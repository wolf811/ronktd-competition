from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from seminar.models import SParticipant, SPromoCode


class SParticipantForm(forms.ModelForm):
    nksystem = forms.CharField(
        max_length=200,
        label="В какой системе вы аттестовываете специалистов НК и лаборатории НК?",
        required=False,
    )
    question = forms.CharField(
        widget=forms.Textarea,
        label="Обозначьте вопросы, которые, на ваш взгляд, необходимо осветить на семинаре",
        required=False,
    )
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

    def clean_email(self):
        email = self.cleaned_data["email"]
        if SParticipant.objects.filter(email=email).exists():
            raise ValidationError(
                "Участник с таким адресом эл. почты уже зарегистрирован..."
            )
        return email

    def clean_promocode(self):
        promocode = self.cleaned_data["promocode"]
        if SPromoCode.objects.filter(code=promocode, activated=True).exists():
            raise ValidationError("Такой промо-код уже ранее был использован...")
        return promocode
