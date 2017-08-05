import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from wiki_contents.views.home_view import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info['project'], 'wiki-contents')
