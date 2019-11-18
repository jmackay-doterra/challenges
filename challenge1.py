import unittest
from base import Base


class Challenge1(Base):

    def test_challenge1(self):

        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

if __name__ == '__main__':
    unittest.main()