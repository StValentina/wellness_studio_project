from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'review_class',]
        labels = {
            'review_text': 'Review Text',
            'rating': 'Rating',
        }
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

class ReviewDeleteForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'review_class', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = True

    def clean(self):
        return self.cleaned_data