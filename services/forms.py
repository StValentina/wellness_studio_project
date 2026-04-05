from django import forms

from services.models import Service


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_title', 'service_description', 'image']
        widgets = {
            'service_title': forms.TextInput(attrs={
                'Label': 'Service Title',
            }),
            'service_description': forms.Textarea(attrs={
                'class': 'form-field-description',
                'label': 'Service Description',
            }),
            'image': forms.FileInput(attrs={'label': 'Service Image'}),
        }
