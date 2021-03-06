from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ShinyAppsTest(FunctionalTest):

    def test_shinyapps_screen_displays_apps_from_logged_in_user_only(self):

        # Isaac goes to the shiny apps page and sees no apps

        self.browser.get(self.server_url)

        foundapp=False
        try:
            shinyapp1 = self.browser.find_element_by_id('id_shinyapp1')
            foundapp=True
        except:
            pass
        self.assertEqual(foundapp,False)

        # He then logs in, redirecting him to the homepage so he clicks back into Shiny Apps

        self.user_login_assert_equal('Log-in').click()
        self.wait_for_window_with_title('Log-in')
        self.user_login('langestrst01','8976YHT@')
        self.wait_for_window_with_title('Modelling Platform')

        self.get_shinyapps_link().click()
        self.wait_for_window_with_title('Shiny Apps')

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

