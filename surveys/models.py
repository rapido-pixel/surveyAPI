from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=200, blank=True, unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    TEXT = 'text'
    SINGLE_CHOICE = 'singe_choice'
    MULTI_CHOICE = 'multi_choice'
    CHOICES = (
        (TEXT, 'text'),
        (SINGLE_CHOICE, 'single_choice'),
        (MULTI_CHOICE, 'multi_choice')
    )
    name = models.CharField(max_length=200, unique=True)
    answer_type = models.CharField(max_length=50, choices=CHOICES)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    anon_id = models.CharField(max_length=300, null=True, blank=True)
    survey = models.ManyToManyField(Survey, related_name='completed_surveys')

    def __str__(self):
        return f'anonymous_user {self.anon_id}'


class Answer(models.Model):
    answer = models.CharField(max_length=300, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_for_question')
    user_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.answer
