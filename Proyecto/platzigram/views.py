"""platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time is {}'.format(now))

def sort_integers(request):
    """Return a JSON"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_inits = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_inits,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeing."""
    if age <= 12:
        message = 'Sorry {}, you are not allow here!'.format(name)
    else:
        message = 'Hello {}, welcome to platzigram'.format(name)
    return HttpResponse(message)