from unittest import skip
from django.core.urlresolvers import resolve
from django.test import TestCase
from account.views import user_login
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from forms import LoginForm

class UserLoginTest(TestCase):

    #def setUp(self):
    #    self.user1 = User.objects.create_user(username='admin', email='', password='admin')
    #    self.user2 = User.objects.create_user(username='langestrst01', email='', password='8976YHT@')

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/account/login/')
        self.assertEqual(found.func, user_login)

    def test_user_login_page_returns_correct_html(self):
        request = HttpRequest()
        response = user_login(request)
        form = LoginForm()
        expected_html = render_to_string('account/login.html', {'form': form})
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertIn('Account Login', response.content.decode())

    def test_user_login_page_redirects_after_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'admin'
        request.POST['password'] = 'admin'
        response = user_login(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    @skip
    def test_user_login_can_save_a_POST_request(self):
        User.objects.create(username='admin', password='admin')
        User.objects.create(username='langestrst01', password='8976YHT@')
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'admin'
        request.POST['password'] = 'admin'
        user_login(request)
        self.user = User.objects.get(username='admin')
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
        request.POST['username'] = 'langestrst01'
        request.POST['password'] = '8976YHT@'
        user_login(request)
        self.user = User.objects.get(username='langestrst01')
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
        #self.assertTrue(self.user.is_authenticated)
