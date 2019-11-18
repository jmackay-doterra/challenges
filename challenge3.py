import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(Base):

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")

        # Waiting until the "Popular Items" section to load (sometimes the page loads slowly and the test fails)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")))

        # Searches for all of the Makes/Models in the "Popular Items" section
        makes = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")

        # Prints all of the texts & links
        for make in makes:
            print(make.text + " - " + make.get_attribute("href"))

if __name__ == '__main__':
    unittest.main()