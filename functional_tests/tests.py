import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(2)

  def tearDown(self):
    time.sleep(0.5)
    self.browser.quit()

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [r.text for r in rows])

  def test_can_start_list_and_retrieve_later(self):
    # Edith goes to check out the homepage
    self.browser.get(self.live_server_url)

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
    
    self.check_for_row_in_list_table('1: Buy peacock feathers')

    # The text box is still there, and Edith enters another
    # to-do: "Use peacock feathers to make a fly". 
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)

    #She sees that on her list once th page updates.
    self.check_for_row_in_list_table('1: Buy peacock feathers')
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    # Ediths leaves the website and then comes back using her
    # unique URL (check for explanatory text).
    self.fail('Finish the test!')

    # The to-do list is still here.

    # Edith calls it a day and closes her browser.


