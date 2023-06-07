from django.db import models

# Create your models here.


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname