"""
The views.py rendering python program.
"""

from django.http import HttpResponse
from django.template import loader

def index(request):
    """
    This is the primary function to call the index.html page.
    """
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
