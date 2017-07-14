from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from pyramid_mako import add_mako_renderer

import sqlahelper
import pyramid_tm
from sitn_portal.lib import dbreflection

import yaml

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    settings = config.get_settings()

    settings.update(yaml.load(file(settings.get("app.cfg"))))

    add_mako_renderer(config, ".html")
    add_mako_renderer(config, ".js")

    config.include("pyramid_mako")

    engine = engine_from_config(settings, 'sqlalchemy.')
    sqlahelper.add_engine(engine)
    
    config.include(pyramid_tm.includeme)

    dbreflection.init(engine)

    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
