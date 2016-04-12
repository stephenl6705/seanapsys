from .base import FunctionalTest

class UserLoginTest(FunctionalTest):

    def test_can_login_and_logout_on_home_screen(self):

        # Isaac noticed that he can login on the home screen
        # so he goes to the home screen and clicks on Log-in

        self.browser.get(self.server_url)

        self.user_login_assert_equal('Log-in').click()
        self.wait_for_window_with_title('Log-in')

        # A login form opens and he used the admin credentials

        self.user_login('admin','admin')
        self.wait_for_window_with_title('Modelling Platform')

        # He now notices a welcome message on the home page saying: Hello admin, logout
        self.user_login_assert_equal('Hello admin, logout')

        # When refreshing he notices it still says: Hello admin, logout
        self.browser.refresh()
        self.wait_for_window_with_title('Modelling Platform')
        logout = self.user_login_assert_equal('Hello admin, logout')

        # He clicks on Hello admin, logout and now sees Log-in again

        logout.click()
        self.wait_for_window_with_title('Modelling Platform')
        login = self.user_login_assert_equal('Log-in')

        # He now wants to use Papas credentials

        login.click()
        self.wait_for_window_with_title('Log-in')

        self.user_login('langestrst01','8976YHT@')
        self.wait_for_window_with_title('Modelling Platform')

        # He now notices a welcome message on the home page saying: Hello Stephen, logout
        self.user_login_assert_equal('Hello Stephen, logout')

    def test_can_logout_on_shinyapps_screen(self):

        # Isaac logs in

        self.browser.get(self.server_url)

        self.user_login_assert_equal('Log-in').click()
        self.wait_for_window_with_title('Log-in')
        self.user_login('ruser','ruser')

        self.wait_for_window_with_title('Modelling Platform')

        # He then goes to the Shiny apps page to see if he can logout from there

        self.get_shinyapps_link().click()
        self.wait_for_window_with_title('Shiny Apps')
        self.user_login_assert_equal('Hello ruser, logout').click()
        self.wait_for_window_with_title('Modelling Platform')

        # He is now returned to the home page with the option to Log-in

        self.user_login_assert_equal('Log-in')


        #self.fail('Finish the test')
