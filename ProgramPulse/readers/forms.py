from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()

class RegisterationForm(forms.ModelForm):
    #  all the from fields are set to true by default for the required
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["last_name"].required = False
        self.fields["first_name"].required = True
        self.fields["email"].required = True
        # for field_name, field in self.fields.items():
            # print(f'{field_name}: required={field.required}')

    def clean(self):
        # There are two type of clean method, one is on the field and the one on form
        # read the difference about them
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if (password and confirm_password) and (password == confirm_password):
                print("we are validated")
        else:
            # such errors are non field errors so how they are displayed on the top of form in html read about that
            raise ValidationError("the password and the confirm password did not matched")

    def save(self, commit=True):
        user = super().save(commit=False)
        # the work of the set password here is that it will hash the password before saving to db
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user

