from django import forms

from online_library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'profile_img': forms.URLInput(attrs={'placeholder': 'URL'}),
        }
        labels = {
            'profile_img': 'Image URL'
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description", "image_url", "type")
        labels = {
            'image_url': 'Image'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime....'}),
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields = ("title", "description", "image_url", "type")
        labels = {
            'image_url': 'Image'
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            'profile_img': 'Image URL'
        }

class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance


    class Meta:
        model=Profile
        fields = "__all__"
        labels = {
            'profile_img': 'Image URL'
        }



