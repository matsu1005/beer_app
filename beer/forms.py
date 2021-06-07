from django import forms
from .models import Review


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'beer', 'score', 'taste_kire', 'taste_sannmi', 'taste_nigami', 'taste_amami', 
            'taste_koku', 'content', 'image1', 'image2', 'image3' 
            )
