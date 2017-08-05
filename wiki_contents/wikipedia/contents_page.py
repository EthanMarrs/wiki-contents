from bs4 import BeautifulSoup
import requests


class ContentsPage:
    """
    A simple class that provides functionality for scraping the HTML table of
    contents from a Wikipedia page.
    """

    url = ''
    html = ''

    def __init__(self, url):
        self.url = url

    def contents(self):
        """
        Returns the Wikipedia contents page as HTML for a given URL.
        """
        return

    def fetch(self):
        """
        Fetches the HTML contents of a webpage at the provided URL.
        """
        return

    def scrape(self):
        """
        Scrapes the HTML page and returns the table of contents, or raises an
        exception if the table doesn't exist.
        """
        return
