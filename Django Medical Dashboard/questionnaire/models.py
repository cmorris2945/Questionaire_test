from django.db import models

class Questionnaire(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('multiple_choice', 'Multiple Choice'),
    ]

    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='text')
    choices = models.JSONField(blank=True, null=True)  # Only used for multiple choice questions
    order = models.IntegerField(default=0)  # New field to specify the order of the questions

    class Meta:
        ordering = ['order']  # Ensure questions are retrieved in the correct order

    def __str__(self):
        return f"({self.order}) {self.question_text}"

class Attempt(models.Model):
    patient_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attempt {self.id} for Patient {self.patient_id}"

class PatientResponse(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return f"Response to {self.question} in Attempt {self.attempt.id}"
