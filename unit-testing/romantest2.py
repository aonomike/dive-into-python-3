import unittest, roman1, roman2

class ToRomanBadInput(unittest.TestCase):

    def test_too_large(self):
        '''to roman should fail with large input'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, 4000)
    
    def test_zero(self):
        '''to_roman() should fail when input is zero'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, 0)

    def test_negative(self):
        '''to_roman() should fail when input is negative numbers'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, -1)
    
    def test_non_integer(self):
        '''to_roman() should fail when input is not integer'''
        self.assertRaises(roman2.NotIntegerError, roman1.to_roman,'mike')

if __name__ == '__main__':
    unittest.main()
