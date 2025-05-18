from django import forms
from .models import Avis

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['nom', 'commentaire', 'note']
        widgets = {
            'note': forms.RadioSelect(choices=[(i, '★' * i + '☆' * (5 - i)) for i in range(1, 6)]),
            'commentaire': forms.Textarea(attrs={'rows': 3}),
        }
