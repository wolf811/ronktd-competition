from django import forms


class ParticipantForm(forms.Form):
    fio = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    commentary = forms.Textarea(required=False)
    pdn_accept = forms.BooleanField()
