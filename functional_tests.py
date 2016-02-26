from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_link_to_r_studio_site(self):

        # Isaac has heard about a cool new innovation platform. He goes and checks out the homepage
        self.browser.get('http://innovation.seanapsys.com')

        # He notices the page title and header mention innovation platform
        self.assertIn('Innovation Platform', self.browser.title)

        # He is invited to go to our RStudio site and to our Shiny Applications site
        rstudio = self.browser.find_element_by_id('id_rstudio')
        rstudio_link = rstudio.find_element_by_tag_name('a')
        self.assertEqual(rstudio_link.text,"RStudio","The link was:\n%s" % (rstudio_link.text,))
        shinyapps = self.browser.find_element_by_id('id_shinyapps')
        shinyapps_link = shinyapps.find_element_by_tag_name('a')
        self.assertEqual(shinyapps_link.text,"Shiny Apps","The link was:\n%s" % (shinyapps_link.text,))

        # He selects the RStudio link and now find himself on the Rstudio site
        rstudio_link.click()
        self.assertIn('RStudio Sign In', self.browser.title)

        # He goes back to the innovation home site and selects the shiny applications site
        self.browser.get('http://innovation.seanapsys.com')
        shinyapps_link.click()
        self.assertIn('Shiny Apps', self.browser.title)

        # He now finds himself on a page showing a list of Shiny Applications

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')