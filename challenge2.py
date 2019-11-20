import unittest
from base import Base
from _common.search import Search


class Challenge2(Base):

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        Search.searchBar(self, "exotics")

        # Searches the results table for any and all 'PORSCHE'
        makes = self.driver.find_elements_by_xpath("//*[@id=\"serverSideDataTable\"]//span[contains(text(),\"PORSCHE\")]")

        # Asserts that at least one 'PORSCHE' was found in the results table
        self.assertTrue(len(makes)>0,"Porsche was NOT found in the search results.")

if __name__ == '__main__':
    unittest.main()