import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(Base):

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        # Finds search input and searches for 'exotics'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "input-search")))
        search = self.driver.find_element(By.ID , "input-search")
        search.send_keys("exotics" + Keys.RETURN)

        # Waits until the results table is visible
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))

        # Searches the results table for any and all 'PORSCHE'
        makes = self.driver.find_elements_by_xpath("//*[@id=\"serverSideDataTable\"]//span[contains(text(),\"PORSCHE\")]")

        # Asserts that at least one 'PORSCHE' was found in the results table
        self.assertTrue(len(makes)>0,"Porsche was NOT found in the search results.")

if __name__ == '__main__':
    unittest.main()