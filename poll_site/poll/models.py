from django.db import models

# Create your models here.
class PollInfo(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name
