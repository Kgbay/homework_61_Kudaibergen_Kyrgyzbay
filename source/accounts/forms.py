from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control form-control-lg'})
    password.widget.attrs.update({'class': 'form-control form-control-lg'})