from .models import Survey, Question
from rest_framework import viewsets, permissions
from .serializers import SurveySerializer, QuestionSerializer

class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = SurveySerializer

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = QuestionSerializer