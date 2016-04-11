import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        cls.server_url = 'http://innovation.seanapsys.com'

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()


    def get_shinyapps_link(self):
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        return shinyapps.find_element_by_tag_name('a')

    def wait_for_window_with_title(self, text_in_title):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: text_in_title in b.title
        )

    def user_login_assert_equal(self,text):
        user = self.browser.find_element_by_id('id_user')
        login = user.find_element_by_tag_name('a')
        self.assertEqual(login.text, text)
        return login

    def user_login(self,username,password):
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys(username)
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys(password)
        inputbox = self.browser.find_element_by_id('id_login')
        login = self.browser.find_element_by_id('id_login')
        login.send_keys(Keys.ENTER)
