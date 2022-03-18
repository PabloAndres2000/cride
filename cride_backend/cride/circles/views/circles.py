# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializers
from cride.circles.serializers.circles import CircleModelSerializer

# Models
from cride.circles.models.circles import Circle
from cride.circles.models.memberships import Membership

# Providers
from cride.circles.providers import circles as circles_providers
from cride.circles.providers import membership as membership_providers
from cride.utils.lib.constants import DATA_NOT_FOUND, SERVER_ERROR


class CircleViewSet(viewsets.ModelViewSet):

    serializer_class = CircleModelSerializer

    def list(self, request):
        circles = circles_providers.get_all_circles()
        serializer = CircleModelSerializer(circles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perfom_create(self, serializer):
        """Assign circle admin."""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitation=10,
        )
