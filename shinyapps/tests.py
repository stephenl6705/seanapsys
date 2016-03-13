from unittest import skip
from shinyapps.models import ShinyItem, ShinyGroup
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from shinyapps.views import shiny_page
from setup_db import setup_items, save_selected_group

class ShinyPageTest(TestCase):

    def test_root_url_resolves_to_shiny_page_view(self):
        found = resolve('/shinyapps')
        self.assertEqual(found.func, shiny_page)

    def test_shiny_page_returns_correct_html(self):
        request = HttpRequest()
        setup_items(ShinyGroup, ShinyItem)
        response = shiny_page(request)
        expected_html = render_to_string('shiny_home.html')
        #self.assertEqual(response.content.decode(), expected_html)
        self.assertIn('Hello App', response.content.decode())

    def test_shiny_page_returns_correct_list_after_a_username_POST_request(self):
        request = HttpRequest()
        setup_items(ShinyGroup, ShinyItem)
        request.method = 'POST'

        request.POST['username'] = 'langestrst01'
        save_selected_group(ShinyGroup,'langestrst01',selected_status=True)
        response = shiny_page(request)
        self.assertIn('Hello App', response.content.decode())
        self.assertIn('Movie Explorer', response.content.decode())

        request.POST['username'] = 'ruser'
        save_selected_group(ShinyGroup,'ruser',selected_status=True)
        response = shiny_page(request)
        self.assertIn('Hello App', response.content.decode())


class ShinyModelTest(TestCase):

    def test_saving_and_retrieving_shinyapps(self):

        first_group = ShinyGroup()
        first_group.username = 'ruser'
        first_group.save()
        first_item = ShinyItem()
        first_item.name = 'Hello App'
        first_item.group = first_group
        first_item.save()

        second_group = ShinyGroup()
        second_group.username = 'langestrst01'
        second_group.save()
        second_item = ShinyItem()
        second_item.name = 'Movie Explorer'
        second_item.group = second_group
        second_item.save()

        saved_items = ShinyItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Hello App')
        self.assertEqual(second_saved_item.name, 'Movie Explorer')
        self.assertEqual(first_saved_item.group.username, 'ruser')
        self.assertEqual(second_saved_item.group.username, 'langestrst01')
