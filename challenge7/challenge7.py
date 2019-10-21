import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")

        # Waiting until the "Popular Items" section to load (sometimes the page loads slowly and the test fails)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")))

        # Searches for all of the Makes/Models in the "Popular Items" section
        links = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")

        # Stores link text and links in a 2D array
        linksArray = []
        for x in range(len(links)):
            linksArray.append([])
            for y in range(1):
                linksArray[x].append(links[x].text)
                linksArray[x].append(links[x].get_attribute("href"))

            # Checks that the URL returns a valid status code
            try:
                r = requests.head(linksArray[x][1])
                print(linksArray[x][0], linksArray[x][1], ": Status Code", r.status_code, "(PASSED)")
            except:
                print(linksArray[x][0], linksArray[x][1], "FAILED to connect")

        # # OLD CODE USED BEFORE SEEING THAT A 2D ARRAY WAS IN THE REQUIREMENTS
        # for link in range(len(links)):
        #     linkText = links[link].text
        #     linkURL = links[link].get_attribute("href")
        #     try:
        #         r = requests.head(linkURL)
        #         print(linkText, ":", linkURL, ": Status Code", r.status_code, "(PASSED)")
        #     except requests.ConnectionError:
        #         print(linkText, ":", linkURL, ": FAILED to connect")

if __name__ == '__main__':
    unittest.main()