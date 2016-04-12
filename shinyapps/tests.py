#from unittest import skip
from shinyapps.models import ShinyItem, ShinyGroup
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from shinyapps.views import shiny_page
from setup_db import setup_items
from django.contrib.auth import get_user_model
User = get_user_model()
#from unittest.mock import patch
from django.http import HttpRequest

class ShinyPageTest(TestCase):

    def test_root_url_resolves_to_shiny_page_view(self):
        found = resolve(reverse('shiny_home'))
        self.assertEqual(found.func, shiny_page)

    def test_shiny_page_returns_correct_html(self):
        response = self.client.get(reverse('shiny_home'))
        expected_html = render_to_string('shiny_home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_shiny_page_returns_correct_list_after_login(self):
        setup_items(ShinyGroup, ShinyItem)
        request = HttpRequest()
        user = User.objects.create(username='admin',password='admin')
        request.user = user
        response = shiny_page(request)
        self.assertNotIn('Hello App', response.content.decode())
        self.assertNotIn('Movie Explorer', response.content.decode())
        user = User.objects.create(username='ruser',password='ruser')
        request.user = user
        response = shiny_page(request)
        self.assertIn('Hello App', response.content.decode())
        self.assertNotIn('Movie Explorer', response.content.decode())
        user = User.objects.create(username='langestrst01',password='8976YHT@')
        request.user = user
        response = shiny_page(request)
        self.assertIn('Hello App', response.content.decode())
        self.assertIn('Movie Explorer', response.content.decode())


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
