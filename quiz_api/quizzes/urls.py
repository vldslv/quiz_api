from rest_framework import routers
#from rest_framework import urlpatterns

from .api import QuizViewSet, AttemptViewSet


router = routers.DefaultRouter()
router.register('quiz', QuizViewSet, 'quiz')
router.register('attempt', AttemptViewSet, 'attempt')


urlpatterns = router.urls
