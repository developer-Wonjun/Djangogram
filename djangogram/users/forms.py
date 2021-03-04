from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms as djagno_forms

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):

    error_messages = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username":_("This username has already been taken.")}
    )
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class SignUpForm(djagno_forms.ModelForm):
    class Meta:
        model = User

        fields = ['email', 'name', 'username', 'password']

        labels = {
            'email' : '이메일 주소',
            'name' : '성명',
            'username' : '사용자 이름',
            'password' : '비밀번호'
        }

        widgets = {
            'password' : djagno_forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

