import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search():
    numOfItems_20 = "option[1]"
    numOfItems_50 = "option[2]"
    numOfItems_100 = "option[3]"

    def searchBar(self, searchTerm):
        # Finds search input and searches for the searchTerm provided
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "input-search")))
        search = self.driver.find_element(By.ID, "input-search")
        search.send_keys(searchTerm + Keys.RETURN)

        # Waits until the results table is visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))

    def selectNumOfItemsToShow(self, numberOfItems):
        # Selects to show 100 items in the results
        itemsToShow = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable_length\"]//select")
        itemsToShow.click()
        option = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable_length\"]//" + numberOfItems)
        option.click()

        # Waits until the results table has reloaded
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located((By.ID, "serverSideDataTable_processing")))