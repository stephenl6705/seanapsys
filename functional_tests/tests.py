from unittest import skip
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

waittime = 3

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
        self.browser.implicitly_wait(waittime)

    def tearDown(self):
        self.browser.quit()

    @skip
    def test_can_link_to_r_studio_site(self):

        # Isaac has heard about a cool new innovation platform. He goes and checks out the homepage
        self.browser.get(self.server_url)

        # He notices the page title and header mention innovation platform
        self.assertIn('Innovation Platform', self.browser.title)

        # He is invited to go to our RStudio site and to our Shiny Applications site
        rstudio = self.browser.find_element_by_id('id_rstudio')
        rstudio_link = rstudio.find_element_by_tag_name('a')
        self.assertEqual(rstudio_link.text,"RStudio","The link was:\n%s" % (rstudio_link.text,))

        # He selects the RStudio link and now find himself on the Rstudio site
        rstudio_link.click()
        self.browser.implicitly_wait(waittime)
        self.assertIn('RStudio Sign In', self.browser.title)

    @skip
    def test_can_link_to_shiny_site(self):

        # Isaac goes back to the innovation home site and selects the shiny applications site
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        shinyapps_link = shinyapps.find_element_by_tag_name('a')
        self.assertEqual(shinyapps_link.text,"Shiny Apps","The link was:\n%s" % (shinyapps_link.text,))
        shinyapps_link.click()
        self.browser.implicitly_wait(waittime)
        # He now finds himself on a page showing a list of Shiny Applications
        self.assertIn('Shiny Apps', self.browser.title)

    @skip
    def test_can_link_to_shinyapp1_site(self):

        # Isaac is now also curious about the first app that he saw
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        shinyapps_link = shinyapps.find_element_by_tag_name('a')
        shinyapps_link.click()
        #self.browser.implicitly_wait(waittime)
        shinyapp1 = self.browser.find_element_by_id('id_shinyapp1')
        shinyapp1_link = shinyapp1.find_element_by_tag_name('a')
        self.assertEqual(shinyapp1_link.text,"Hello App","The link was:\n%s" % (shinyapp1_link.text,))
        shinyapp1_link.click()
        self.browser.implicitly_wait(waittime)
        self.assertIn("Alive", self.browser.title)

    @skip
    def test_can_link_to_shinyapp2_site(self):

        # Isaac is now also curious about the second app that he saw
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        shinyapps_link = shinyapps.find_element_by_tag_name('a')
        shinyapps_link.click()
        self.browser.implicitly_wait(waittime)
        shinyapp2 = self.browser.find_element_by_id('id_shinyapp2')
        shinyapp2_link = shinyapp2.find_element_by_tag_name('a')
        self.assertEqual(shinyapp2_link.text,"Movie Explorer","The link was:\n%s" % (shinyapp2_link.text,))
        shinyapp2_link.click()
        self.browser.implicitly_wait(waittime)
        self.assertIn("Movie explorer", self.browser.title)

    def test_can_login_on_shinyapps_screen(self):

        # Isaac noticed on the ShinyApps screen that there was a login option with a text saying
        # To access your private apps please login here
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        shinyapps_link = shinyapps.find_element_by_tag_name('a')
        shinyapps_link.click()
        self.browser.implicitly_wait(waittime)
        login = self.browser.find_element_by_id('id_login')
        login_link = login.find_element_by_tag_name('a')
        self.assertEqual(login_link.text,"Login here","The link was:\n%s" % (login_link.text,))

        # He clicks on login and is asked for a username and password
        login_link.click()
        self.browser.implicitly_wait(waittime)
        self.assertIn('Shiny Apps', self.browser.title)
        self.fail('Finish the test')
        # He now finds a list of additional Shiny Applications






if __name__ == '__main__':
    unittest.main(warnings='ignore')