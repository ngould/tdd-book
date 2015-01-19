import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # She is invited to enter a to-do item
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
        inputbox.get_attribute('placeholder'), 'Enter a to-do item')

    # She types "Buy peacock feathers" in the text box
    inputbox.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates and now she sees
    # "Buy peacock feathers" in her list of to-do's
    inputbox.send_keys(Keys.ENTER)
    
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

    # The text box is still there, and Edith enters another
    # to-do: "Use peacock feathers". 
    self.fail('Finish the test!')

    #She sees that on her list once th page updates.


    # Ediths leaves the website and then comes back using her
    # unique URL (check for explanatory text).


    # The to-do list is still here.

    # Edith calls it a day and closes her browser.

if __name__ == '__main__':
  unittest.main()
