from django import forms


class EmailConForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=25)
    email = forms.EmailField(label="Почта")
    number = forms.CharField(label="Номер телефона", required=True)
