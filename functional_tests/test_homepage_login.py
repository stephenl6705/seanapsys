from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class HomepageLoginTest(FunctionalTest):

    def test_can_login_and_logout_on_home_screen(self):

        # Isaac noticed that he can login on the home screen
        # so he goes to the home screen and clicks on Log-in
        self.browser.get(self.server_url)
        user = self.browser.find_element_by_id('id_user')
        login = user.find_element_by_tag_name('a')
        self.assertEqual(login.text, 'Log-in')
        login.click()
        self.wait_for_window_with_title('Log-in')

        # A login form opens and he simply enters

        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('admin')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('admin')
        inputbox = self.browser.find_element_by_id('id_login')
        login = self.browser.find_element_by_id('id_login')
        login.send_keys(Keys.ENTER)
        self.wait_for_window_with_title('Modelling Platform')

        # He now notices a welcome message on the home page saying: Hello admin, logout
        user = self.browser.find_element_by_id('id_user')
        logout = user.find_element_by_tag_name('a')
        self.assertEqual(logout.text, "Hello admin, logout")

        # He clicks on Hello admin, logout and now sees Log-in again

        logout.click()
        self.wait_for_window_with_title('Modelling Platform')
        user = self.browser.find_element_by_id('id_user')
        login = user.find_element_by_tag_name('a')
        self.assertEqual(login.text, 'Log-in')

        # He now wants to use Papas credentials

        login.click()
        self.wait_for_window_with_title('Log-in')

        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('langestrst01')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('8976YHT@')
        login = self.browser.find_element_by_id('id_login')
        login.send_keys(Keys.ENTER)
        self.wait_for_window_with_title('Modelling Platform')

        # He now notices a welcome message on the home page saying: Hello Stephen, logout
        user = self.browser.find_element_by_id('id_user')
        login = user.find_element_by_tag_name('a')
        self.assertEqual(login.text, "Hello Stephen, logout")


        #self.fail('Finish the test')
