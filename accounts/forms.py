from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def clean_password1(self):
        pw = self.cleaned_data['password1']
        if len(pw) < 7:
            raise forms.ValidationError('Must be more than 7 characters long!')
        return pw

    def save(self):
        new_user = super(CreateUserForm, self).save()

        pw = self.cleaned_data['password1']
        new_user.set_password(pw)
        new_user.save()
        return new_user

