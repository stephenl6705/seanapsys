#from unittest import skip
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from account.views import user_login
from django.http import HttpRequest
from django.template.loader import render_to_string
from forms import LoginForm
from unittest.mock import patch
from django.contrib.auth import get_user_model, SESSION_KEY
User = get_user_model()

class UserLoginTest(TestCase):

    #def setUp(self):
    #    self.user1 = User.objects.create_user(username='admin', email='', password='admin')
    #    self.user2 = User.objects.create_user(username='langestrst01', email='', password='8976YHT@')

    def test_login_url_resolves_to_login_view(self):
        found = resolve(reverse('login'))
        self.assertEqual(found.func, user_login)

    def test_user_login_page_returns_correct_html(self):
        request = HttpRequest()
        response = user_login(request)
        form = LoginForm()
        expected_html = render_to_string('account/login.html', {'form': form})
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertIn('Account Login', response.content.decode())

    def test_user_login_page_redirects_after_post(self):
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')

    @patch('account.views.authenticate')
    def test_calls_authenticate_with_user_and_passwd_from_post(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        mock_authenticate.assert_called_once_with(username='admin', password='admin')

    @patch('account.views.authenticate')
    def test_redirects_when_user_found(self, mock_authenticate):
        user = User.objects.create(username='admin', password='admin')
        user.backend = ''
        mock_authenticate.return_value = user
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)
        #self.assertEqual(response.content.decode(), 'OK')

    @patch('account.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(self, mock_authenticate):
        user = User.objects.create(username='admin', password='admin')
        user.backend = ''
        mock_authenticate.return_value = user
        self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(self.client.session[SESSION_KEY], str(user.pk))

    @patch('account.views.authenticate')
    def test_does_not_get_logged_in_if_authenticate_returns_None(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertNotIn(SESSION_KEY, self.client.session)


