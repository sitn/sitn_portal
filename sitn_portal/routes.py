def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # default.py
    config.add_route('home', '/')

    # docs.py
    config.add_route('list', 'docs/list')
    config.add_route('search', 'docs/search/{term}')
    config.add_route('get', 'docs/get/{docid}')
    config.add_route('add', 'docs/add')
    config.add_route('edit', 'docs/edit/{docid}')
    config.add_route('delete', 'docs/delete')
