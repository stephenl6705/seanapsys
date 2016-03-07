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

    def test_shiny_page_returns_correct_list_after_a_username_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'langestrst01'

        response = shiny_page(request)

        self.assertIn('Movie Explorer', response.content.decode())

        expected_html = render_to_string(
            'shiny_home.html',
            {'new_shinyapp': 'Movie Explorer'}
        )
        self.assertEqual(response.content.decode(), expected_html)

        request.POST['username'] = 'ruser'

        response = shiny_page(request)

        self.assertIn('Hello App', response.content.decode())

        expected_html = render_to_string(
            'shiny_home.html',
            {'new_shinyapp': 'Hello App'}
        )
        self.assertEqual(response.content.decode(), expected_html)

