# Typing
from typing import List, Union, Optional

from django.forms import ValidationError

# Django
from django.db.models.query import QuerySet

# Models
from cride.circles.models import Circle


def get_circle_by_pk(pk: int) -> Optional[Circle]:
    """
    Method to obtain circle by pk
    - Returns: Optional[Circle]
    """
    try:
        circle = Circle.objects.get(pk=pk)
        if not circle:
            raise ValidationError('Your request was not found')
        return circle
    except Circle.DoesNotExist:
        return None


def get_all_circles() -> Union[QuerySet, List[Circle]]:
    """
    Method to get a list of all circles
    """
    circles = Circle.objects.all()
    return circles
