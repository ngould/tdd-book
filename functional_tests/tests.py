import sys
import time
import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    for arg in sys.argv:
      if 'liveserver' in arg:
        cls.server_url = 'http://' + arg.split('=')[1]
        return
    super(NewVisitorTest, cls).setUpClass()
    cls.server_url = cls.live_server_url

  @classmethod
  def tearDownClass(cls):
    if cls.server_url == cls.live_server_url:
      super(NewVisitorTest, cls).tearDownClass()

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
    self.browser.get(self.server_url)

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
    edith_list_url = self.browser.current_url
    self.assertRegexpMatches(edith_list_url, '/lists/.+')
    self.check_for_row_in_list_table('1: Buy peacock feathers')

    # The text box is still there, and Edith enters another
    # to-do: "Use peacock feathers to make a fly". 
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)

    #She sees that on her list once the page updates.
    self.check_for_row_in_list_table('1: Buy peacock feathers')
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    # Now a new user, Francis, comes along to the site.

    ## We use a new browser session to make sure that no information
    ## of Edith's is coming through from cookies, etc.
    self.browser.quit()
    self.browser = webdriver.Firefox()

    # Francis visits the home page. There is no sign of Edith's list.
    self.browser.get(self.server_url)
    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Buy peacock feathers', page_text)
    self.assertNotIn('make a fly', page_text)

    # Francis starts a new list by entering a new item.
    # He is less interesting than Edith.
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)

    # Francis gets his own unique URL
    francis_list_url = self.browser.current_url
    self.assertRegexpMatches(francis_list_url, '/lists/.+')
    self.assertNotEqual(francis_list_url, edith_list_url)

    # Again, there is no trace of Edith's list
    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Buy peacock feathers', page_text)
    self.assertIn('Buy milk', page_text)

    # Satisfied, they both go to sleep

  def test_layout_and_styling(self):
    #Edith goes to the home page
    self.browser.get(self.server_url)
    self.browser.set_window_size(1024, 768)

    # She notices the input box is nicely centered
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=5,
    )

    # She starts a new list and sees the input is nicely
    # centered there too
    inputbox.send_keys('testing\n')
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=5,
    )








