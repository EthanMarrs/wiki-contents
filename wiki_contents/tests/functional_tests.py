import unittest


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from wiki_contents import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Wiki-Contents' in res.body)
        self.assertTrue(
            b'Submit a Wikipedia URL to navigate the table of contents.'
            in res.body
        )
