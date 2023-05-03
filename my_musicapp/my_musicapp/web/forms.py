from django import forms

from my_musicapp.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForms(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        labels = {
            "image_url": "Image URL",
            "album_name": "Album Name"
        }
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': "Artist"}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class AddAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = "__all__"
