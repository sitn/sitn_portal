from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='myapp', renderer='myapp.html')
def myapp(request):

    return {'one': 'one', 'project': 'sitn_portal'}


@view_config(route_name='myapp_fake', renderer='json')
def myapp_fake(request):

    if request.host_url == 'http://localhost:6543':
        request.response.headers['Access-Control-Allow-Origin'] = '*'

    return {
        'myapp': [{
            'title': 'one',
            'project': 'sitn_portal'
        },{
            'title': 'two',
            'project': 'sitn_portal2'
        }]
    }
