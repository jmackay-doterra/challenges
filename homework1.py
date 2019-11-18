import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homework1(Base):

    def test_homework1(self):
        self.driver.maximize_window()
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"content_body\"]//ol[1]")))

        # Using a list to find all elements
        oils = self.driver.find_elements(By.XPATH, "//*[@id=\"content_body\"]//ol[1]//a")

        # Using a dictionary to store all keys and values
        i = 0
        allOils = {}
        while i < len(oils):
            key = oils[i].text
            value = oils[i].get_attribute("href")
            i += 1
            if len(key) > 1:
                allOils[key] = value

        # print(allOils.keys())
        # print(allOils.values())

        # Using an array to store the broken links
        hasError = False
        brokenLinks = []
        for oil in allOils:
            self.driver.get(allOils[oil])
            # print("Went to: ", self.driver.current_url)
            try:
                oilHeader = self.driver.find_element(By.XPATH,"//*[@id=\"prod-title\"]/h1")
                # print("Found: ", oilHeader.text)
            except:
                brokenLinks.append(allOils[oil])
                hasError = True
                # print("***NO HEADER WAS FOUND***")

        self.assertFalse(hasError, "There was a problem with one or more of the URL's: {}".format(brokenLinks))

if __name__ == '__main__':
    unittest.main()