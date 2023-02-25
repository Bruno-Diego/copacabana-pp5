from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'rating']
        labels = {
            'title': 'Title',
            'body': 'Review',
            'rating': 'Rating',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control \
            border-black'}),
            'body': forms.Textarea(attrs={'class': 'form-control \
                border-black', 'rows': 5}),
            'rating': forms.NumberInput(attrs={'class': 'form-control \
                border-black col-1 mx-auto'}),
        }
