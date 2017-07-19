from pyramid.view import view_config


@view_config(route_name='docs', renderer='docs.html')
def docs(request):

    return {'one': 'one', 'project': 'sitn_portal'}


@view_config(route_name='docs_fake', renderer='json')
def docs_fake(request):

    if request.host_url == 'http://localhost:6543':
        request.response.headers['Access-Control-Allow-Origin'] = '*'

    return {
        'docs': [{
            'title': 'one',
            'project': 'sitn_portal'
        }, {
            'title': 'two',
            'project': 'sitn_portal2'
        }]
    }
