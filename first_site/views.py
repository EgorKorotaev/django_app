from django.http import HttpResponse

# Create your views here.
from django.template import loader

from first_site.models import Event


def event(request, question_id):
    template = loader.get_template('any/events.html')
    event = Event.objects.get(id=question_id)
    context = {
        'event': event,
    }

    return HttpResponse(template.render(context, request))
