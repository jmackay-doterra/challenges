import unittest
from fibonacci import Fibonacci as fib
from int2word import IntToWord as i2w

class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        num = int(input("Please enter a number: "))

        fibNum = fib.generate_fibonacci(num)
        numWord = i2w.int_to_word(fibNum)

        print(str(fibNum) + " - " + numWord)

if __name__ == '__main__':
    unittest.main()