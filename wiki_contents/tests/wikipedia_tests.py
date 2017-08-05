import unittest
from unittest.mock import MagicMock

from pyramid import testing
from wiki_contents.wikipedia.contents_page import ContentsPage


class WikipediaTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.contents_page = ContentsPage('https://en.wikipedia.org/wiki/Dog')

    def tearDown(self):
        testing.tearDown()

    def test_fetch(self):
        self.contents_page.fetch()
        self.assertEqual(self.contents_page.html, '<html><body></body></html>')

    def test_scrape(self):
        self.contents_page.html = '<html><div id="toc"></div></html>'
        contents = self.contents_page.scrape()
        self.assertEqual('<div id="toc"></div>', contents)

    def test_contents_page(self):
        contents = self.contents_page.contents()
        self.assertEqual('<div id="toc"></div>', contents)
