from django.db import models

class Question(models.Model):
    TYPE_CHOICES = (
        ("MC", "Multiple Choice"),
        ("TXT", "Text Answer"),
        ("NC", "Number Choice"),
    )

    text = models.CharField(max_length=300)
    question_type = models.CharField(max_length=3, choices=TYPE_CHOICES, null=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text}"

class Respondent(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Non-binary"),
        ("P", "Prefer not to say")
    ]

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Answer(models.Model):
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)

    text_answers = models.TextField()

    def __str__(self):
        return f"{self.respondent.id} Answers"