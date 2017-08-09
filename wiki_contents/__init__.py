from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('results', '/results')
    config.add_route('no_contents', '/no_contents')
    config.add_static_view('static', 'deform:static')
    config.scan()
    return config.make_wsgi_app()
