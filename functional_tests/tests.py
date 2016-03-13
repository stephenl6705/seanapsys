from selenium.webdriver.common.keys import Keys
from unittest import skip
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

waittime = 5

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


    def get_shinyapps_link(self):
        self.browser.get(self.server_url)
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        return shinyapps.find_element_by_tag_name('a')


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
        self.browser.implicitly_wait(waittime)
        self.assertIn('RStudio Sign In', self.browser.title)

    def test_can_link_to_shiny_site(self):

        # Isaac goes back to the innovation home site and selects the shiny applications site
        shinyapps_link = self.get_shinyapps_link()
        self.assertEqual(shinyapps_link.text,"Shiny Apps","The link was:\n%s" % (shinyapps_link.text,))
        shinyapps_link.click()
        self.browser.implicitly_wait(waittime)
        # He now finds himself on a page showing Shiny Applications
        self.assertIn('Shiny Apps', self.browser.title)

    def test_can_login_on_shinyapps_screen(self):

        # Isaac noticed on the ShinyApps screen that there was a login option
        # so he goes back to the ShinyApps page to check it out
        shinyapps_link = self.get_shinyapps_link()
        shinyapps_link.click()
        self.browser.implicitly_wait(waittime)
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
        self.browser.implicitly_wait(waittime)
        self.assertIn("Movie explorer", self.browser.title)

        #table = self.browser.find_element_by_id('id_shinyapps_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('Movie Explorer', [row.text for row in rows])

        #self.fail('Finish the test')

    @skip
    def test_can_link_to_shinyapp1_site(self):

        # Isaac is now also curious about the first app that he saw
        shinyapps_link = self.get_shinyapps_link()
        shinyapps_link.click()
        #self.browser.implicitly_wait(waittime)
        shinyapp1 = self.browser.find_element_by_id('id_shinyapp1')
        shinyapp1_link = shinyapp1.find_element_by_tag_name('a')
        self.assertEqual(shinyapp1_link.text,"Hello App","The link was:\n%s" % (shinyapp1_link.text,))
        shinyapp1_link.click()
        self.browser.implicitly_wait(waittime)
        self.assertIn("Alive", self.browser.title)





if __name__ == '__main__':
    unittest.main(warnings='ignore')