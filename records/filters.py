import django_filters
from .models import Film


class FilmFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['year', 'length', 'title', 'subject', 'actor', 'actress', 'director', 'popularity']
