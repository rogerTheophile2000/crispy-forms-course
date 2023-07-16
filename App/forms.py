from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# every letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
    
# every letters to uppercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):

    #  VALIDATIONS
    # firstname
    firstname = forms.CharField(
        label = 'Nom', min_length=3, max_length=50, 
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = True, 
        widget=forms.TextInput(attrs={
            'placeholder':'Votre nom',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )

    # lastname
    lastname = forms.CharField(
        label = 'Post-nom', min_length=3, max_length=50, 
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        widget = forms.TextInput(attrs={
            'placeholder':'Votre post-nom',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    # job
    job = Uppercase(
        label = 'Job Code', min_length=5, max_length=5,
        widget = forms.TextInput(attrs={
            'placeholder':'Example: FR-22',
            'style':'text-transform: uppercase; font-size:1rem',
        })
    )
    
    # email
    email = Lowercase(
        label = 'Adresse mail', min_length=10, max_length=50, 
        validators = [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message = "Put a valid email address !")],
        widget = forms.TextInput(attrs={
            'placeholder':'Votre Adresse mail',
            'style':'text-transform: lowercase; font-size:1rem',
        })
    )

    # meth 1
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    
    # meth 1
    
    # age
    age = forms.CharField(
        label = 'Age', min_length=2, max_length=3,
        validators = [RegexValidator(r'^[0-9]*$', 
        message = "Only Numbers is allowd !")],
        widget = forms.TextInput(attrs={'placeholder':'Votre Age'})
    )
    
    # message
    message = forms.CharField(
        label = 'Talk little about you', 
        min_length=50, max_length=1000,
        widget = forms.Textarea(attrs={
            'placeholder':'Parlez brievement de vous',
            'rows':7
        }),
    )

    # file upload
    file = forms.FileField(
        widget= forms.ClearableFileInput(
            attrs={
                'style': 'font-size : 1rem',
            }
        ),
    )

    experience = forms.BooleanField(
        label = "I have exprerience",
        required = False
    )
    
    # Method 1 (gender)
    # GENDER = [('M', 'Masculin'), ('F', 'Feminin')]
    # gender = forms.CharField(
    #     label='Genre', 
    #     widget=forms.RadioSelect(choices=GENDER)
    # )

    class Meta:
        model = Candidate
        # fields = "__all__"
        exclude =['created_at']
        
        # labels control
        labels = {
            'phone':'Enter Phone',
            'salary':'Choose your Salary',
            'personality':'Choose your Personality',
            'gender':'Choose your gender',
            'smoker':'Do you smoke',
        }

        SALARY = (
            ('','Salary expectation (month)'),
            ('Between $3000 and $4000', 'Between $3000 and $4000'),
            ('Between $4000 and $5000', 'Between $4000 and $5000'),
            ('Between $5000 and $7000', 'Between $5000 and $7000'),
            ('Between $7000 and $10000', 'Between $7000 and $10000'),
        )

        # Method 2 (gender)
        GENDER = [('M', 'Masculin'), ('F', 'Feminin')]
        # outside widget
        widgets = {
            'phone':forms.TextInput(attrs={
                # 'style':'font-size: 1rem',
                # 'placeholder':'Phone number',
                # 'data-mask':'(000) 000-000-000'
                }
            ),
            'salary':forms.Select(
                choices = SALARY,
                attrs = {
                    'class':'form-control',
                }
            ),
            'gender':forms.RadioSelect(
                choices = GENDER,
                attrs = {
                    'class':'btn-check',
                }
            ),
            'smoker':forms.RadioSelect(
                choices = SMOKER,
                attrs = {
                    'class':'btn-check',
                }
            ),
            'personality':forms.Select(attrs = {
                    'style':'font-size: 1rem;',
                }
            ),
            
        }

    # Super function
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)


        #  *********** CONTROL PANEL (individual input) *********|
        # 1. input required
        # self.fields['message'].required = True

        # 2. Input disabled
        # self.fields['experience'].disabled = False

        # 3. Input Readonly
        # self.fields['email'].widget.attrs.update({'readonly' : 'readonly'})

        #  4. SELECT OPTION *********|
        self.fields["personality"].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[1:]
        
        #  5. WIDGET CONTROL *********|
        self.fields['phone'].widget.attrs.update({'style':'font-size: 1rem', 'placeholder':'No Phone','data-mask':'(000) 000-000-000'})

        
        #  *********** READONLY / DISABLED 'LOOP FOR' IN [ARRAY] *********|
        # readonly
        # readonly = ['firstname', 'lastname', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'False'

        # disabled
        # disabled = ['firstname', 'lastname', 'job']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'

        # prenvent duplication
        # method 1
        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #     for obj in Candidate.objects.all():
        #         if obj.email == email:
        #             raise forms.ValidationError("Denied ! " + email + " is already registered>")
        #     return email

        # method 2
        def clean_email(self):
            email = self.cleaned_data.get('email')
            for obj in Candidate.objects.filter(email = email).exists():
                raise forms.ValidationError("Denied ! {} is already registered.".format(email))
            return email