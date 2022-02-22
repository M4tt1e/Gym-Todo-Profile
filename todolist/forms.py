from django.contrib.auth import get_user_model
from django import forms

from .models import Todo, Profile

class ItemCreateForm(forms.ModelForm):
    share_with = forms.CharField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'body', 'importance', 'due_date','share_with',
                'image']

    def clean_shared_with(self):
        User = get_user_model()
        share_with = self.cleaned_data.get('share_with')
        try:
            return User.objects.get(username=share_with)
        except User.DoesNotExist:
            raise forms.ValidationError("No user exists with that username")
        

class MyOwnSignUpForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Validate Password", help_text="Enter the same password as above")
    email = forms.EmailField(widget=forms.EmailInput, label="Please enter your email address")
    
    error_messages = {
            'password_mismatch': ("The two password fields didn't match."),
    }

    class Meta:
        model = get_user_model()
        fields = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


#class ItemCreateForm(forms.ModelForm):
#    class Meta:
#        model = Todo
#        fields = ['title', 'body', 'importance', 'due_date']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
