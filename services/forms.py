from django import forms

from services.models import Service


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_title', 'service_description', 'image']
        labels = {
            'service_title': 'Service Title',
            'service_description': 'Service Description',
            'image': 'Service Image',
        }
        widgets = {
            'service_title': forms.TextInput(),
            'service_description': forms.Textarea(attrs={
                'class': 'form-field-description',
            }),
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            filename = self.instance.image.name.split('/')[-1]
            self.fields['image'].help_text = f"Current image: {filename}"
