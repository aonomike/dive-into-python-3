import roman2
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))    
def to_roman(k):
    
    '''convert integer to roman numeral'''
   
    if not isinstance(k, int):
        raise(roman2.NotIntegerError('input value must be integer'))
    if not ( 0< k <= 3999):
        raise(roman2.OutOfRangeError('number out of range(must be less than 1..3999)'))

    result = ''
    for numeral, integer in roman_numeral_map:
        while k >= integer:
#            import pdb; pdb.set_trace()
            result += numeral
            k -= integer
    return result
