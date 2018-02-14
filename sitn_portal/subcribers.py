# -*- coding: utf-8 -*-
from pyramid.events import subscriber, NewRequest


@subscriber(NewRequest)
def allowLocalhost(event):

    if event.request.host_url == 'http://localhost:6543':
        event.request.response.headers['Access-Control-Allow-Origin'] = '*'
