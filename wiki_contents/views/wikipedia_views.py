from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from wiki_contents.wikipedia.contents_page import ContentsPage


class WikipediaViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='results', request_method='GET',
                 renderer='templates/results.jinja2')
    def results(self):
        """
        A view that attempts to fetch a Wikipedia page and display just the
        contents page. The view uses the ContentsPage class to handle this.
        If no content is returned, the view redirects to a new page.
        """
        contents_page = ContentsPage(self.request.params['url'])
        html = contents_page.contents()

        if html:
            return {'html': html}
        else:  # If no HTML content
            return HTTPFound(location='/no_contents')

    @view_config(route_name='no_contents', request_method='GET',
                 renderer='templates/no_contents.jinja2')
    def no_content(self):
        """
        A simple view that displays a no content message.
        """
        return {'message': 'The requested Wikipedia page did not have a table '
                           'of contents.'}
