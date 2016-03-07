from shinyapps.models import Item
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
            {'shinyapp_id': 'id_shinyapp2',
                'username': 'langestrst01',
                'shinyapp_dirname': 'movie_explorer',
                'shinyapp_name': 'Movie Explorer',
            }
        )
        self.assertEqual(response.content.decode(), expected_html)

        request.POST['username'] = 'ruser'

        response = shiny_page(request)

        self.assertIn('Hello App', response.content.decode())

        expected_html = render_to_string(
            'shiny_home.html',
            {
                'shinyapp_id': 'id_shinyapp1',
                'username': 'ruser',
                'shinyapp_dirname': 'hello',
                'shinyapp_name': 'Hello App',
            }
        )
        self.assertEqual(response.content.decode(), expected_html)

class ShinyModelTest(TestCase):

    def test_saving_and_retrieving_shinyapps(self):

        first_item = Item()
        first_item.name = 'Hello App'
        first_item.save()

        second_item = Item()
        second_item.name = 'Movie Explorer'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Hello App')
        self.assertEqual(second_saved_item.name, 'Movie Explorer')
