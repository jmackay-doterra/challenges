import unittest
from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _common.search import Search


class Challenge5(Base):

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        Search.searchBar(self, "porsche")
        Search.selectNumOfItemsToShow(self, Search.numOfItems_100)

        # Finds all models returned
        models = self.driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]//span[@data-uname=\"lotsearchLotmodel\"]")

        # Finds all unique models from list and adds them as a key value to a dictionary and updates the counts for each
        uniqueModels = {}
        for i in range(len(models)):
            if (models[i].text in uniqueModels.keys()):
                uniqueModels[models[i].text] += 1
            else:
                uniqueModels[models[i].text] = 1

        print("Unique Models Found: ")
        for i in uniqueModels:
            print(i, "(", uniqueModels[i], ")")

        # Finds all of the damages returned
        damages = self.driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]//span[@data-uname=\"lotsearchLotdamagedescription\"]")

        damageTypes = {
            "REAR END": 0,
            "FRONT END": 0,
            "MINOR DENT/SCRATCHES": 0,
            "UNDERCARRIAGE": 0,
            "MISC": 0}

        # Adds counts to the categories defined in the dictionary
        for i in range(len(damages)):
            if (damages[i].text in damageTypes.keys()):
                damageTypes[damages[i].text] += 1
            else:
                damageTypes["MISC"] += 1

        print("Damages: ")
        for i in damageTypes:
            print(i, "(", damageTypes[i], ")")


if __name__ == '__main__':
    unittest.main()