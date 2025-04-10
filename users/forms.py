from django import forms

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="اسم المستخدم")
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'phone', 'address']