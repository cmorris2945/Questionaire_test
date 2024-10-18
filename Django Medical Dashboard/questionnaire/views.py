from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Questionnaire, PatientResponse, Attempt
from django.http import JsonResponse
# from .service import generate_dynamic_questions
import json

@login_required
def start_questionnaire(request):
    attempt = Attempt.objects.create(patient_id=request.user.id)
    first_question = Questionnaire.objects.order_by('order').first()  # Fetch the first question based on order

    return render(request, 'questionnaire.html', {'question': first_question, 'attempt': attempt})

def get_next_question(request, attempt_id, question_id):
    attempt = get_object_or_404(Attempt, id=attempt_id)
    current_question = get_object_or_404(Questionnaire, id=question_id)
    
    if request.method == 'POST':
        response_text = request.POST.get('response')
        PatientResponse.objects.create(attempt=attempt, question=current_question, response_text=response_text)

    # Fetch the next question based on order
    next_question = Questionnaire.objects.filter(order=current_question.order + 1).order_by('order').first()
    print("next question: {}".format(next_question))

    if next_question:
        return JsonResponse({
            'question': next_question.question_text,
            'question_type': next_question.question_type,
            'choices': next_question.choices if next_question.question_type == 'multiple_choice' else None
        })
    else:
        return JsonResponse({'message': 'Thank you for completing the questionnaire!'})
    
@login_required
def questionnaire_view(request):
    print(request.user.id)
    attempt = Attempt.objects.create(patient_id=request.user.id)
    questions = Questionnaire.objects.all().values('question_text', 'question_type', 'id', 'choices', 'order')  # Fetch all questions
    questions_list = json.dumps(list(questions))  # Convert to list for easy JSON manipulation
    print(questions_list)
    # Convert choices to a list if they exist
    # for question in questions_list:
    #     if question['choices']:
    #         question['choices'] = json.loads(question['choices'])  # Assume choices is stored as a JSON string

    return render(request, 'questionnaire.html', {'questions': questions_list, 'attempt': attempt.id})

def submit_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        attempt_id = data.get('attempt_id')
        question_id = data.get('question_id')
        response_text = data.get('response_text')

        # Fetch the attempt, question, and save the answer
        attempt = get_object_or_404(Attempt, id=attempt_id)
        question = get_object_or_404(Questionnaire, id=question_id)

        # Create and save the answer
        PatientResponse.objects.create(attempt=attempt, question=question, response_text=response_text)

        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'failed'}, status=400)

def thankyou(request):
    return render(request, 'thankyou.html')

# def generate_questions(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         attempt_id = data.get('attempt_id')
#         responses = PatientResponse.objects.filter(attempt_id=attempt_id).all()
#         conversation_history = ""
#         for response in responses:
#             conversation_history += f"Question: {response.question.question_text}\n"
#             conversation_history += f"Answer: {response.response_text}\n\n"
#         dynamic_questions = generate_dynamic_questions(conversation_history)
#         print(dynamic_questions)
#         return JsonResponse({"dynamic_questions": dynamic_questions})