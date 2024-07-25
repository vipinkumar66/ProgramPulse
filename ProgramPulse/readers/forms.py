from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()

class RegisterationForm(forms.ModelForm):
    #  all the from fields are set to true by default for the required
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":" w-[90%] px-2 py-2 rounded-lg bg-gray-200 text-gray-800 border border-gray-700 active:border-indigo-700", "placeholder":"Enter password"}),
                               label="Paasword")

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"flex w-[90%] px-2 py-2 rounded-lg bg-gray-200 text-gray-800 border border-gray-700", "placeholder":"Enter your username"}),
            "email":forms.TextInput(attrs={"class":" w-[90%] px-2 py-2 rounded-lg bg-gray-200 text-gray-800 border border-gray-700", "placeholder":"Enter your Email Id"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        # the work of the set password here is that it will hash the password before saving to db
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'w-[90%] px-2 py-2 rounded-lg bg-gray-200 text-gray-800 border border-black'
    }),label="Enter your email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"w-[90%] px-2 py-2 rounded-lg bg-gray-200 text-gray-800 border border-gray-700"
    }), label="Enter your password")