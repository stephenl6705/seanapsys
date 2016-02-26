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
        self.fail('Finish the test')

        # He is invited to go to our RStudio site and to our Shiny Applications site

        # He selects the RStudio link and now find himself on the Rstudio site

        # He goes back to the innovation home site and selects the shiny applications site
        # He now finds himself on a page showing a list of Shiny Applications



if __name__ == '__main__':
    unittest.main(warnings='ignore')