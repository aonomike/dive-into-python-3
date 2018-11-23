import unittest, roman1, roman2

class ToRomanBadInput(unittest.TestCase):

    def test_too_large(self):
        '''to roman should fail with large input'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, 5000)

    def test_zero(self):
        '''to_roman() should fail when input is zero'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, 0)

    def test_negative(self):
        '''to_roman() should fail when input is negative numbers'''
        self.assertRaises(roman2.OutOfRangeError, roman1.to_roman, -1)

    def test_non_integer(self):
        '''to_roman() should fail when input is not integer'''
        self.assertRaises(roman2.NotIntegerError, roman1.to_roman,'mike')


class FromRomanBadInput(unittest.TestCase):

    def test_too_many_repeated_numerals(self):
        ''' from_roman should fail with too many repeated numerals'''
        for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman1.from_roman, s)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman1.from_roman, s)

    def test_malformed_anticedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman1.from_roman, s)

    def test_blank(self):
        '''from_roman should fail with empty string'''
        self.assertRaises(roman2.InvalidRomanNumeralError, roman1.from_roman, '')


if __name__ == '__main__':
    unittest.main()
