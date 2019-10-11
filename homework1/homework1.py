import unittest
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homework1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.maximize_window()
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"content_body\"]//ol[1]")))

        oils = self.driver.find_elements(By.XPATH, "//*[@id=\"content_body\"]//ol[1]//a")

        allOils = {}
        for oil in oils:
            allOils[oil] = oil.get_attribute("href")

        for oil in allOils:
            self.driver.get(allOils[oil])
            # TODO: assert the correct oil page displays
            print("went to: ", self.driver.current_url)

if __name__ == '__main__':
    unittest.main()