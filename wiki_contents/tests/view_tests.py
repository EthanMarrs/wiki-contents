import unittest
import responses

from pyramid import testing

from wiki_contents.views import home_views
from wiki_contents.views import wikipedia_views


class ViewTests(unittest.TestCase):
    def setUp(self):
        """
        Setup tests and mock external request to Wikipedia.
        """
        self.test_url = 'https://en.wikipedia.org/wiki/Pylons_project'

        # Mock requests to Wikipedia
        responses.add(responses.GET, self.test_url,
                      body='<html><p>Text</p><div id="toc"></div></html>',
                      status=200)
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        """
        Assert that project name is assigned.
        """
        request = testing.DummyRequest()
        view = home_views.HomeViews(request)
        home = view.home()
        self.assertEqual(home['project'], 'wiki-contents')

    def test_no_content_view(self):
        """
        Assert that the "no content" message is displayed.
        """
        request = testing.DummyRequest()
        view = wikipedia_views.WikipediaViews(request)
        no_content = view.no_content()

        self.assertEqual(
            no_content['message'],
            'The requested Wikipedia page did not have a table of contents.'
        )

    @responses.activate
    def test_results_view(self):
        """
        Assert that the HTML is scraped as expected.
        """
        request = testing.DummyRequest(params={'url': self.test_url})
        view = wikipedia_views.WikipediaViews(request)
        results = view.results()

        # Assert that only the required HTML is returned
        self.assertEqual(str(results['html']), '<div id="toc"></div>')
