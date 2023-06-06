from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

class CandidateForm(forms.ModelForm):

    #  VALIDATIONS
    firstname = forms.CharField(
        label='Nom', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowd !")],
        required=True, 
        widget=forms.TextInput(attrs={'placeholder':'Votre nom'})
    )

    lastname = forms.CharField(
        label='Post-nom', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowd !")],
        widget=forms.TextInput(attrs={'placeholder':'Votre post-nom'})
    )
    
    email = forms.EmailField(
        label='Adresse mail', min_length=10, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message="Put a valid email address !")],
        widget=forms.TextInput(attrs={'placeholder':'Votre Adresse mail'})
    )

    # meth 1
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    
    # meth 1
    
    age = forms.CharField(
        label='Age', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', 
        message="Only Numbers is allowd !")],
        widget=forms.TextInput(attrs={'placeholder':'Votre Age'})
    )
    
    
    message = forms.CharField(
        label='Talk little about you', 
        min_length=50, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder':'Parlez brievement de vous', 'rows':7})
    )
    

#     Name: ^[a-zA-ZÀ-ÿ\s]*$
#     Email: ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$
#     Age: ^[0-9]*$
    class Meta:
        model = Candidate
        fields = "__all__"
        # fields = ['firstname', 'lastname', 'email', 'age', 'message']
        # exclude = ['firstname', 'lastname', 'email', 'age', 'message']