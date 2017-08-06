from pyramid.view import view_config
from wiki_contents.wikipedia.contents_page import ContentsPage


class WikipediaViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='results', request_method='POST',
                 renderer='templates/results.jinja2')
    def results(self):
        url = self.request.params['url']
        contents_page = ContentsPage(url)
        html = contents_page.contents()

        return {'html': html}
