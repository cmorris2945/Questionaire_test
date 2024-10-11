from django.core.management.base import BaseCommand
from questionnaire.models import Questionnaire

class Command(BaseCommand):
    help = 'Load predefined questions into the database if none exist'

    def handle(self, *args, **kwargs):
        if Questionnaire.objects.exists():
            self.stdout.write(self.style.WARNING('Questions already exist. Skipping...'))
        else:
            questions = [
                {'question_text': 'What is your age?', 'question_type': 'text', 'order': 1},
                {'question_text': 'What symptoms are you experiencing?', 'question_type': 'text', 'order': 2},
                {'question_text': 'Have you been diagnosed with any of the following conditions?', 
                 'question_type': 'multiple_choice', 'choices': ['Diabetes', 'Hypertension', 'None'], 'order': 3},
            ]
            
            for question in questions:
                Questionnaire.objects.create(**question)

            self.stdout.write(self.style.SUCCESS('Successfully loaded questions'))
