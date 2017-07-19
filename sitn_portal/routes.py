def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # default.py
    config.add_route('home', '/')

    # docs.py
    config.add_route('docs_fake', 'docs/fake')
    config.add_route('docs', '/docs')
