import unittest
from selenium import webdriver

class Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()