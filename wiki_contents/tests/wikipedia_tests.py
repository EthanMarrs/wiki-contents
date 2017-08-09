import unittest
import responses

from pyramid import testing
from wiki_contents.wikipedia.contents_page import ContentsPage


class WikipediaTests(unittest.TestCase):
    def setUp(self):
        """
        Setup tests with ContentsPage object, and mocking of HTTP requests.
        """
        test_url = 'https://en.wikipedia.org/wiki/Dog'

        # Mock requests to Wikipedia
        responses.add(
            responses.GET, test_url,
            body='<html><div id="toc"></div></html>', status=200
        )

        self.config = testing.setUp()
        self.contents_page = ContentsPage(test_url)

    def tearDown(self):
        testing.tearDown()

    @responses.activate
    def test_fetch(self):
        """
        Assert that returned HTML content from the external request is stored
        in the object.
        """
        self.contents_page.fetch()
        self.assertEqual(
            self.contents_page.html,
            '<html><div id="toc"></div></html>'
        )

    def test_scrape(self):
        """
        Assert that the HTML is scraped to only include a div with id "toc".
        """
        self.contents_page.html = '<html><div id="toc"></div></html>'
        contents = self.contents_page.scrape()
        self.assertEqual('<div id="toc"></div>', str(contents))

    @responses.activate
    def test_contents(self):
        """
        Assert that the contents method both fetches and scrapes the HTML for
        the contents page.
        """
        contents = self.contents_page.contents()
        self.assertEqual('<div id="toc"></div>', str(contents))
