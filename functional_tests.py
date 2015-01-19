import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(2)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_list_and_retrieve_later(self):
    # Edith goes to check out the homepage
    self.browser.get('http://localhost:8000')

    # She notices that the title says to-do's
    assert 'To-Do' in self.browser.title
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the the test!')

    # She is invited to enter a to-do item


    # She types "Buy peackock feathers" in the text box


    # When she hits enter, the page updates and now she sees
    # "Buy peackock feathers" in her list of to-do's



    # The text box is still there, and Edith enters another
    # to-do: "Use peackock feathers". 


    #She sees that on her list once th page updates.


    # Ediths leaves the website and then comes back using her
    # unique URL (check for explanatory text).


    # The to-do list is still here.

    # Edith calls it a day and closes her browser.

if __name__ == '__main__':
  unittest.main()
