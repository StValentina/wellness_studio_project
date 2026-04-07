from django import forms

from studio_classes.models import StudioClass, Tag


class StudioClassForm(forms.ModelForm):
    class Meta:
        model = StudioClass
        fields = '__all__'
        widgets = {
            'class_title': forms.TextInput(attrs={
                'label': 'Studio Class Title',
            }),
            'class_description': forms.Textarea(attrs={
                'class': 'form-field-description',
                'label': 'Studio Class Description',
            }),
            'level': forms.Select(),
            'tags': forms.Select(),
            'instructor': forms.Select(),
        }

class StudioClassDeleteForm(forms.ModelForm):
    class Meta:
        model = StudioClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

    def clean(self):
        return self.cleaned_data


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
