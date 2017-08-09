from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from wiki_contents.schemas import schemas

import deform.widget


class HomeViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        """
        The primary view for the Wiki-Contents application. The view uses
        Deform to display a URL input form. If the form is submitted, the input
        is validated and a redirect occurs.
        """
        schema = schemas.WikipediaSchema()
        form = deform.Form(schema, buttons=('submit',), action='/')

        # If the user submits the form.
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()

            try:  # Attempt to validate and redirect to results page
                appstruct = form.validate(controls)
                url = appstruct['url']
                return HTTPFound(location=self.request.route_url(
                    'results', _query={'url': url}))
            except deform.ValidationFailure as e:  # Handle validation error.
                return {'form': e.render()}  # Render form with error messages.

        return {'project': 'wiki-contents', 'form': form.render()}
