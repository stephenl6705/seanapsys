from .base import FunctionalTest
from unittest import skip

class HomepageLinksTest(FunctionalTest):

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


    def test_can_link_to_shiny_site_when_logged_in_only(self):

        self.browser.get(self.server_url)

        # Isaac goes to the innovation home site and sees the Rstudio links only

        FoundShinyApps=False
        try:
            shinyapps_link = self.get_shinyapps_link()
            FoundShinyApps = True
        except:
            pass
        self.assertEqual(FoundShinyApps, False)

        # He then logs in

        self.user_login_assert_equal('Log-in').click()
        self.wait_for_window_with_title('Log-in')
        self.user_login('ruser','ruser')

        self.wait_for_window_with_title('Modelling Platform')

        # He now notices the Shiny Apps link so he checks that out

        shinyapps_link = self.get_shinyapps_link()
        self.assertEqual(shinyapps_link.text,"Shiny Apps","The link was:\n%s" % (shinyapps_link.text,))
        shinyapps_link.click()

        # He now finds himself on a page showing Shiny Applications
        self.wait_for_window_with_title('Shiny Apps')

