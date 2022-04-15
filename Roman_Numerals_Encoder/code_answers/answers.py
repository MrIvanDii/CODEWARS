
#----------------------------------------------------------------------------------------------------------------------

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


#----------------------------------------------------------------------------------------------------------------------


vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c, v in vals if v <= n)


#----------------------------------------------------------------------------------------------------------------------


units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]


#----------------------------------------------------------------------------------------------------------------------


anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)


#----------------------------------------------------------------------------------------------------------------------


def solution(n):
    s = ''
    while n - 1000 >= 0:
        n = n - 1000
        s += 'M'
    while n - 900 >= 0:
        n = n - 900
        s += 'CM'
    while n - 500 >= 0:
        n = n - 500
        s += 'D'
    while n - 400 >= 0:
        n = n - 400
        s += 'CD'
    while n - 100 >= 0:
        n = n - 100
        s += 'C'
    while n - 90 >= 0:
        n = n - 90
        s += 'XC'
    while n - 50 >= 0:
        n = n - 50
        s += 'L'
    while n - 40 >= 0:
        n = n - 40
        s += 'XL'
    while n - 10 >= 0:
        n = n - 10
        s += 'X'
    while n - 9 >= 0:
        n = n - 9
        s += 'IX'
    while n - 5 >= 0:
        n = n - 5
        s += 'V'
    while n - 4 >= 0:
        n = n - 4
        s += 'IV'
    while n - 1 >= 0:
        n = n - 1
        s += 'I'
    return s

