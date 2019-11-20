import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _common.search import Search


class Challenge6(Base):

    def test_challenge6(self):
        self.driver.get("https://www.copart.com")
        Search.searchBar(self, "nissan")

        # Waits until the model filter is visible
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"filters-collapse-1\"]//a[@data-uname=\"ModelFilter\"]")))

        modelFilter = self.driver.find_element(By.XPATH, "//*[@id=\"filters-collapse-1\"]//a[@data-uname=\"ModelFilter\"]")
        modelFilter.click()

        modelFilterSearch = self.driver.find_element(By.XPATH, "//*[@id=\"collapseinside4\"]//input[@ng-model=\"filter.searchText\"]")
        modelFilterSearch.send_keys("skyline")
        # modelFilterSearch.send_keys("invalid_model")

        vehicles = 0

        try:
            skylineCheckBox = self.driver.find_element(By.ID, "lot_model_descSKYLINE")
            skylineCheckBox.click()

            # Waits until the results table has reloaded
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located((By.ID, "serverSideDataTable_processing")))

            # Finds all vehicles returned of that model
            models = self.driver.find_elements(By.XPATH,
                                                 "//*[@id=\"serverSideDataTable\"]//span[@data-uname=\"lotsearchLotmodel\"]")

            vehicles = len(models)
            print("Found", vehicles, "vehicle(s) of that model.")

        except:
            self.driver.save_screenshot("../challenges/screenshots/screenshot.png")
            print("A screenshot has been saved as screenshot.png")


        self.assertTrue(vehicles > 0, "No vehicles were found with that model filter.")


if __name__ == '__main__':
    unittest.main()