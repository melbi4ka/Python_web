from django import forms

from examtask.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password", "first_name", "last_name", "profile_picture")
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Profile Picture",
        }
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Car.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")
        labels = {
            "image_url": "Image URL",
        }


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")
        labels = {
            "image_url": "Image URL",
        }


class CarDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = "__all__"
