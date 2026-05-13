from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
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

    def __str__(self) -> str:
        return super().__str__()