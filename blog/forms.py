from django import forms
from .models import Blog_Post, Sponsor

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Blog_Post
        fields = ('publication', 'sponsor', 'title', 'tags', 'text',)
        labels = {
            'publication': 'Publication (Standard Select2)',
            'sponsor': 'Sponsor (Ajax Select2)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the Select2 list blank on entry to the form
        self.fields['sponsor'].queryset = Sponsor.objects.none()

        # Make sure that the queryset is populated when doing the validation of 'sponsor'
        if 'sponsor' in self.data:
            self.fields['sponsor'].queryset = Sponsor.objects.all()

        # Make sure to populate the field from the database when it is set
        elif self.instance.pk:
                self.fields['sponsor'].queryset = Sponsor.objects.filter(pk=self.instance.sponsor.pk)

