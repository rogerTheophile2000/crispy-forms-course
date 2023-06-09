from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.



SITUATION = {
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Desapproved', 'Desapproved'),
}

PERSONALITY = {
    ('I am outgoing', 'I am outgoing'),
    ('I am sociable', 'I am sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discret', 'I am discret'),
    ('I am serious', 'I am serious'),
}

SMOKER = {
    ('1', 'yes'),
    ('2', 'no'),
}

# FRAMEWORKS = (
#     ('Laravel', 'Laravel'),
#     ('Angular', 'Angular'),
#     ('Dango', 'Dango'),
#     ('Vue', 'Vue'),
#     ('Spring', 'Spring'),
#     ('Others', 'Others'),
# )

# LANGUAGES = (
#     ('Java', 'Java'),
#     ('Python', 'Python'),
#     ('Javascript', 'Javascript'),
#     ('C++', 'C++'),
#     ('Ruby', 'Ruby'),
#     ('Others', 'Others'),
# )

# DATABASES = (
#     ('SqlLite', 'SqlLite'),
#     ('PostgreSql', 'PostgreSql'),
#     ('MySQL', 'MySQL'),
#     ('MongoDb', 'MongoDb'),
#     ('Oracle', 'Oracle'),
#     ('Others', 'Others'),
# )

# LIBRARIES = (
#     ('React.js', 'React.js'),
#     ('Ajax', 'Ajax'),
#     ('Jquery', 'Jquery'),
#     ('Chart.js', 'Chart.js'),
#     ('Gaap', 'Gaap'),
#     ('Others', 'Others'),
# )

# MOBILE = (
#     ('Koltin', 'Koltin'),
#     ('React Native', 'React Native'),
#     ('Kivy', 'Kivy'),
#     ('Ionic', 'Ionic'),
#     ('Fluter', 'Fluter'),
#     ('Others', 'Others'),
# )

# OTHERS = (
#     ('UML', 'UML'),
#     ('GIT', 'GIT'),
#     ('GraphQL', 'GraphQL'),
#     ('Docker', 'Docker'),
#     ('Kubernates', 'Kubernates'),
#     ('Others', 'Others'),
# )



class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=3, choices=SMOKER, default="No")
    email = models.EmailField(max_length=70)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices= SITUATION, default="Pending")

    # multi checkboxes
    # frameworks = MultiSelectField(choices=FRAMEWORKS, default="")
    # Languages = MultiSelectField(choices=LANGUAGES, default="")
    # databases = MultiSelectField(choices=DATABASES, default="")
    # libraries = MultiSelectField(choices=LIBRARIES, default="")
    # mobile = MultiSelectField(choices=MOBILE, default="")
    # others = MultiSelectField(choices=OTHERS, default="")
    # capitalize (firstname and lastname)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname