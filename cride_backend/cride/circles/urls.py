"""Circles URls."""

# Django REST Framework
from rest_framework import routers

# Views
from cride.circles.views import circles as circle_views

router = routers.SimpleRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
urlpatterns = router.urls
