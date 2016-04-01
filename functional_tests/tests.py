from selenium.webdriver.common.keys import Keys
from unittest import skip
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class NewVisitorTest(StaticLiveServerTestCase):

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


    def test_can_link_to_r_studio_site(self):

        # Isaac has heard about a cool new innovation platform. He goes and checks out the homepage
        self.browser.get(self.server_url)

        # He notices the page title and header mention innovation platform
        self.assertIn('Modelling Platform', self.browser.title)

        # He is invited to go to our RStudio site and to our Shiny Applications site
        rstudio = self.browser.find_element_by_id('id_rstudio')
        rstudio_link = rstudio.find_element_by_tag_name('a')
        self.assertEqual(rstudio_link.text,"RStudio","The link was:\n%s" % (rstudio_link.text,))

        # He selects the RStudio link and now find himself on the Rstudio site
        rstudio_link.click()
        self.wait_for_window_with_title('RStudio Sign In')

    @skip
    def test_can_link_to_r_studio_google_site(self):

        # Isaac goes back to the innovation home site and selects the RStudio cloud site
        self.browser.get(self.server_url)
        rstudio = self.browser.find_element_by_id('id_crstudio')
        rstudio_link = rstudio.find_element_by_tag_name('a')
        self.assertEqual(rstudio_link.text,"RStudio (cloud)","The link was:\n%s" % (rstudio_link.text,))

        # He selects the RStudio cloud link and now find himself on the Rstudio cloud site
        rstudio_link.click()
        self.wait_for_window_with_title('RStudio Sign In')


    def test_can_link_to_shiny_site(self):

        # Isaac goes back to the innovation home site and selects the shiny applications site
        shinyapps_link = self.get_shinyapps_link()
        self.assertEqual(shinyapps_link.text,"Shiny Apps","The link was:\n%s" % (shinyapps_link.text,))
        shinyapps_link.click()
        # He now finds himself on a page showing Shiny Applications
        self.wait_for_window_with_title('Shiny Apps')
        # He sees an app called Hello App
        shinyapp1 = self.browser.find_element_by_id('id_shinyapp1')
        shinyapp1_link = shinyapp1.find_element_by_tag_name('a')
        self.assertEqual(shinyapp1_link.text,"Hello App","The link was:\n%s" % (shinyapp1_link.text,))

    def test_can_login_on_shinyapps_screen(self):

        # Isaac noticed on the ShinyApps screen that there was a login option
        # so he goes back to the ShinyApps page to check it out
        shinyapps_link = self.get_shinyapps_link()
        shinyapps_link.click()
        self.wait_for_window_with_title('Shiny Apps')
        # On the login option it says to enter the username
        inputbox = self.browser.find_element_by_id('id_login')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter username')
        # He enters his papas username and hits enter
        inputbox.send_keys('langestrst01')
        inputbox.send_keys(Keys.ENTER)
        # He now notices that there are 2 apps
        # The first app is the Hello App
        shinyapp1 = self.browser.find_element_by_id('id_shinyapp1')
        shinyapp1_link = shinyapp1.find_element_by_tag_name('a')
        self.assertEqual(shinyapp1_link.text,"Hello App","The link was:\n%s" % (shinyapp1_link.text,))
        # The second app is Movie Explorer and he decides to check it out
        shinyapp2 = self.browser.find_element_by_id('id_shinyapp2')
        shinyapp2_link = shinyapp2.find_element_by_tag_name('a')
        self.assertEqual(shinyapp2_link.text,"Movie Explorer","The link was:\n%s" % (shinyapp2_link.text,))
        shinyapp2_link.click()
        self.wait_for_window_with_title('Movie explorer')

        #table = self.browser.find_element_by_id('id_shinyapps_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('Movie Explorer', [row.text for row in rows])

    def test_can_login_on_home_screen(self):
        
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
        login = user.find_element_by_tag_name('a')
        self.assertEqual(login.text, "Hello admin, logout")
        
        # He clicks on Hello admin, logout and now enters Papas credentials and hits enter

        user = self.browser.find_element_by_id('id_user')
        login = user.find_element_by_tag_name('a')
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
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')