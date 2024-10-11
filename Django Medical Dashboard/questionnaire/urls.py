from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start_questionnaire, name='start_questionnaire'),
    path('', views.questionnaire_view, name='start_questionnaire'),
    path('next-question/<int:attempt_id>/<int:question_id>/', views.get_next_question, name='get_next_question'),
    path('submit_answer', views.submit_answer, name="submit_answer"),
    path('thankyou', views.thankyou, name="thankyou"),
]
