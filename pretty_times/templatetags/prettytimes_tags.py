from django.template import Library
from pretty_times import pretty


register = Library()


@register.filter
def relative_time(datetime_arg, accuracy=None):
    return pretty.date(datetime_arg, accuracy)
