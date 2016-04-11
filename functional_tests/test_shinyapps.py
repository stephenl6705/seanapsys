from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ShinyAppsTest(FunctionalTest):

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

