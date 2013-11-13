from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import csrf
from oabutton.common import SigninForm, HomeData


def homepage(req):
    # Need to lazy import the Event model so that tests work with
    # mocks
    c = {}
    c.update(csrf(req))

    from oabutton.apps.bookmarklet.models import Event

    evt_count = Event.objects.count()
    json_data = Event.objects.all().to_json()

    c.update({'count': evt_count,
              'events': json_data,
              'hostname': settings.HOSTNAME,
              'signin_form': SigninForm(),
              'home_data': HomeData()})

    return render_to_response('web/start.jade', c)
