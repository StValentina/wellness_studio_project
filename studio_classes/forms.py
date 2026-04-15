from django import forms
from accounts.models import AccountUser
from studio_classes.models import StudioClass, Tag

class InstructorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.profile.get_full_name()

class StudioClassForm(forms.ModelForm):
    instructor = InstructorChoiceField(
        queryset=AccountUser.objects.filter(profile__role='Instructor')
    )

    class Meta:
        model = StudioClass
        fields = '__all__'
        labels = {
            'class_title': 'Studio Class Title',
            'class_description': 'Studio Class Description',
            'level': 'Level',
            'tags': 'Tags',
        }
        widgets = {
            'class_title': forms.TextInput(),
            'class_description': forms.Textarea(attrs={
                'class': 'form-field-description',
            }),
            'class_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                }
            ),
            'level': forms.Select(),
            'tags': forms.SelectMultiple(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = AccountUser.objects.filter(
            profile__role='Instructor'
        )

class StudioClassDeleteForm(forms.ModelForm):
    class Meta:
        model = StudioClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

    def clean(self):
        return self.cleaned_data

class InstructorClassEditForm(forms.ModelForm):
    disabled_fields = ['hall_number', 'price', 'capacity', 'studio_class_service', 'instructor',]

    class Meta:
        model = StudioClass
        exclude = ['created_by']
        widgets = {
            'class_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                }
            ),
            'level': forms.Select(),
            'tags': forms.SelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.disabled_fields:
            self.fields[field_name].disabled = True

    def clean(self):
        return self.cleaned_data

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        labels = {
            'name': 'Tag Name',
        }
