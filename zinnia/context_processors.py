"""Context Processors for Zinnia"""
from zinnia import __version__
import django


def version(request):
    """
    Add version of Zinnia and Django to the context.
    """
    return {
        'ZINNIA_VERSION': __version__,
        'DJANGO_VERSION': django.get_version(),
    }
