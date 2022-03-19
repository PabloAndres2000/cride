"""Users URls."""

# Django

# Django Rest Framework
from rest_framework import routers

# Views
from cride.users.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
