# Typing
from typing import List, Union, Optional

from django.forms import ValidationError

# Django
from django.db.models.query import QuerySet

# Models
from cride.users.models import User


def get_user_by_pk(pk: int) -> Optional[User]:
    """
    Method to obtain user by pk
    - Returns: Optional[User]
    """
    try:
        circle = User.objects.get(pk=pk)
        if not circle:
            raise ValidationError('Your request was not found')
        return circle
    except User.DoesNotExist:
        return None
