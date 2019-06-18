from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy
# class LoginForm(forms.Form):
#     # email = forms.EmailField(error_messages={ 'required':'必须提供正确的邮箱地址' } ,label='邮箱',widget=forms.EmailInput(attrs={'id':'email','class':'form-control','placeholder':'请输入您的邮箱'}))
#     # username = forms.CharField(label='用户名',max_length=15,min_length=6,widget=forms.TextInput(attrs={'id':'username','class':'form-control','placeholder':'请输入您的账号'}))
#     # password = forms.CharField(label='密码',max_length=15,min_length=6,widget=forms.PasswordInput(attrs={'id':'username','class':'form-control','placeholder':'请输入您的密码'}))
#     pass

class MyUserLoginForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ["username","password"]
        widgets = {'password':forms.PasswordInput(attrs={'class':'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'})
                   }
        help_texts = {
            'username':gettext_lazy(''),
        }

class MyUserRegistForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ["username","password","email"]
        widgets = {'password':forms.PasswordInput(attrs={'class':'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})

                   }
        help_texts = {
            'username':gettext_lazy(''),
        }