from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Survey, Question, CustomUser
from .serializers import SurveySerializer, SurveySerializerWithoutStartDate, QuestionSerializer, AnswerSerializer
from .permissions import IsAdminOrReadOnly


class SurveyList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        if request.user.is_superuser:
            surveys = Survey.objects.all()
        else:
            surveys = Survey.objects.filter(active=True)
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetail(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return Survey.objects.get(pk=pk)

    def get(self, request, pk):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk):
        survey = self.get_object(pk)
        serializer = SurveySerializerWithoutStartDate(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    permission_classes(IsAdminOrReadOnly)

    def get_permissions(self):
        if self.request.method != 'PUT':
            return [permission() for permission in (IsAdminOrReadOnly,)]
        return super(QuestionDetail, self).get_permissions()

    def get_object(self, pk):
        return Question.objects.get(pk=pk)

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SurveyForUser(APIView):

    def create_user_id(self, request):
        if not CustomUser.objects.filter(anon_id=request.session.session_key):
            request.session.set_expiry(3000000)
            request.session.save()
            CustomUser(anon_id=request.session.session_key).save()

    def users_finish_survey(self, request, name):
        select_survey = get_object_or_404(Survey, name=name, active=True)
        user = CustomUser.objects.get(anon_id=request.session.session_key)
        user.survey.add(select_survey)

    def get(self, request, name):
        self.create_user_id(request)
        self.users_finish_survey(request, name)
        user = CustomUser.objects.get(anon_id=request.session.session_key)
        survey = user.survey.get(name=name)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)


class AnswerQuestion(APIView):

    def get_user_id(self, anon_id):
        return CustomUser.objects.get(anon_id=anon_id)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=self.get_user_id(request.session.session_key))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinishedSurveys(APIView):

    def get(self, request):
        user_id = CustomUser.objects.get(anon_id=request.session.session_key)
        surveys = user_id.survey.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)
