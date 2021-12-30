"""
Django models utilities.
"""
from django.db import models


class CRideModel(models.Model):
    """
    CRideModel acts as an abstract base class from which every other model
    in the project will inherit. this class provides every table with the
    following attributes
        + created (Datetime): Store the datetime the object was created,
        + modified (Datetime) Store the last datetime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """
        Meta options.
        """
        abstract = True  # Referencia a que este modelo sera abstracto y no se reflejara este modelo en la db

        # Funcion para obtener de una fecha
        get_latest_by = 'created'
        # Ordenar de manera descendete, es decir, el ultimo que se agrego sera el primero
        ordering = ['-created', '-modified']


# class Person(models.Model):
#   first_name = models.CharField()


# class MyPerson(Person):
#    class Meta:
#        proxy = True
