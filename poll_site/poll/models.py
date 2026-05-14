from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Voter(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Non-binary"),
        ("P", "Prefer not to say")
    ]

    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name