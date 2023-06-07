from django.db import models

# Create your models here.

SITUATION = {
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Desapproved', 'Desapproved'),
}


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices= SITUATION, default="Pending")

    # capitalize (firstname and lastname)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname