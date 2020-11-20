from rest_framework import serializers
from .models import Survey, Question, Answer
from drf_writable_nested import WritableNestedModelSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'question']
        read_only_fields = ['user_id']


class QuestionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    answer_for_question = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['name', 'survey', 'answer_type', "answer_for_question"]


class SurveySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'start_date', 'end_date', 'description', 'questions']
        read_only_fields = ['id']


class SurveySerializerWithoutStartDate(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'start_date', 'end_date', 'description', 'questions']
        read_only_fields = ['start_date', 'id']
