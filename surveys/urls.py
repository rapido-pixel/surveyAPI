from django.urls import path
from . import views

urlpatterns = [
    path('surveys/', views.SurveyList.as_view()),
    path('surveys/<int:pk>/', views.SurveyDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('answer/<name>/', views.SurveyForUser.as_view()),
    path('answer-for-question/', views.AnswerQuestion.as_view()),
    path('finished/', views.FinishedSurveys.as_view())

]


