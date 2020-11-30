from rest_framework import viewsets, filters
import datetime as dt

from .models import Quiz, Attempt
from .serializers import QuizSerializer, AttemptSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.exclude(end_date__lte=dt.datetime.today())
    serializer_class = QuizSerializer
    http_method_names = ['get', 'head']


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    http_method_names = ['get', 'head', 'post', 'delete']
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user_id',]
