# Django REST Framework
from email.policy import default
from rest_framework import serializers

# Model
from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):
    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        model = Circle
        fields = (
            'id',
            'name',
            'slug_name',
            'about',
            'picture',
            'rides_offered',
            'rides_taken',
            'verified',
            'is_public',
            'is_limited',
            'members_limit',
        )

    def validate(self, data):
        """ENsure both members_limit and is_limited are present"""
