from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from shinyapps.views import shiny_page

class ShinyPageTest(TestCase):

    def test_root_url_resolves_to_shiny_page_view(self):
        found = resolve('/shinyapps')
        self.assertEqual(found.func, shiny_page)

    def test_shiny_page_returns_correct_html(self):
        request = HttpRequest()
        response = shiny_page(request)
        expected_html = render_to_string('shiny_home.html')
        self.assertEqual(response.content.decode(), expected_html)
