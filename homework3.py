import unittest
from base import Base
from selenium.webdriver.common.by import By


class Homework3(Base):

    def test_challenge2(self):
        self.driver.get("https://www.doterra.com/US/en/product-education-blends")

        oils = self.driver.find_elements(By.XPATH, "//*[@id=\"content\"]//a/span[@class=\"title\"]")

        doTerra = 0
        digestZen = 0
        misc = 0
        for i in range(len(oils)):
            oilName = oils[i].text

            if ("doterra" in oilName.lower()):
                doTerra += 1
            elif ("digestzen" in oilName.lower()):
                digestZen += 1
            else:
                misc += 1

        print("doTERRA: ", doTerra)
        print("DigestZen: ", digestZen)
        print("Misc: ", misc)

if __name__ == '__main__':
    unittest.main()