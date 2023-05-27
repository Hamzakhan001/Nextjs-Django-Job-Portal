from django_filters import rest_framework as filters
from .models import Job


class JobsFilter(filters):
    class Meta:
        model=Job
        fields = ('education','jobType', 'experience')