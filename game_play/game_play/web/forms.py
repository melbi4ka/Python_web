from django import forms

from game_play.web.models import Profile, Game


class CreateProfileForms(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # one way to be hidden chars
    class Meta:
        model = Profile
        fields = ("email", "age", "password")

        widgets = {
            'password': forms.PasswordInput(),
        }


#         second way to hidden chars

class EditProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "first_name": "First name",
            "last_name": "Last Name",
            "profile_img": "Profile Picture",
        }


class DeleteProfileForms(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ("title", "category", "rating", "max_level", "game_img", "summary")

        labels = {
            "max_level": "Max Level",
            "game_img": "Image URL",
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ("title", "category", "rating", "max_level", "game_img", "summary")

        labels = {
            "max_level": "Max Level",
            "game_img": "Image URL",
        }


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = ("title", "category", "rating", "max_level", "game_img", "summary")
