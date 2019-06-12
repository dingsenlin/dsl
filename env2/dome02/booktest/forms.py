from django import forms
class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={ 'required':'必须提供正确的邮箱地址' } ,label='邮箱',widget=forms.EmailInput(attrs={'id':'email','class':'form-control','placeholder':'请输入您的邮箱'}))
    username = forms.CharField(label='用户名',max_length=15,min_length=6,widget=forms.TextInput(attrs={'id':'username','class':'form-control','placeholder':'请输入您的账号'}))
    password = forms.CharField(label='密码',max_length=15,min_length=6,widget=forms.PasswordInput(attrs={'id':'username','class':'form-control','placeholder':'请输入您的密码'}))