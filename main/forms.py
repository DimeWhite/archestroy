from django import forms


class EmailConForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'special', 'id': 'name',
                                                                        'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'special', 'id': 'mail', 'placeholder': 'Почта'}))

    number = forms.RegexField(required=True, regex=r'((\b([8]?[\+7, 7]))|(^[7,\+7])?(^[8]))(\d{10}$)',
                              error_messages={'invalid': "*Неверно введен номер телефона"},
                              widget=forms.TextInput(attrs={
                                    'class': 'special',
                                    'id': 'telephone',
                                    'placeholder': 'Номер телефона'
                                }))
    consent = forms.CharField(widget=forms.TextInput(attrs={'type': 'checkbox'}))



