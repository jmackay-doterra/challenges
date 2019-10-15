import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


class Homework2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_homework1(self):
        self.driver.get("https://www.doterra.com")

        links = self.driver.find_elements(By.XPATH, "//*[@id=\"footer\"]//li[@class=\"footer__links__list__item\"]/a")

        for link in range(len(links)):
            linkText = links[link].text
            linkURL = links[link].get_attribute("href")
            try:
                r = requests.head(linkURL)
                print(linkText, ">", linkURL, ":", r.status_code)
            except requests.ConnectionError:
                print(linkText, ">", linkURL, ":", "Failed to connect")

if __name__ == '__main__':
    unittest.main()