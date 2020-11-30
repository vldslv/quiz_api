from rest_framework import serializers

from .models import Quiz, Question, Attempt, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['text', 'answer_type', 'answer']


class QuizSerializer(serializers.ModelSerializer):
    
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'questions']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['answer',]


class AttemptSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Attempt
        fields = ['id', 'user_id', 'quiz', 'pass_date', 'answers']

