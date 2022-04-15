
#-----------------------------------------------Roman Numerals Encoder-------------------------------------------------

# Create a function taking a positive integer as its parameter
# and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

#----------------------------------------------------------------------------------------------------------------------

def solution(n):

    number = str(n)

    norm_roman_max = {
                      100: "C", 200: "CC", 300: "CCC",
                      400: "CD", 500: "D", 600: "DC",
                      700: "DCC", 800: "DCCC", 900: "CM",
                      1000: "M", 2000: "MM", 3000: "MMM"
                      }

    norm_roman_mid = {
                      10: "X", 20: "XX", 30: "XXX",
                      40: "XL", 50: "L", 60: "LX",
                      70: "LXX", 80: "LXXX", 90: "XC",
                      }

    norm_roman_min = {
                      1: "I", 2: "II", 3: "III",
                      4: "IV", 5: "V", 6: "VI",
                      7: "VII", 8: "VIII", 9: "IX",
                      10: "X"
                      }

    data_max = list(norm_roman_max.keys())
    data_mid = list(norm_roman_mid.keys())
    #print(data)
    #print(int(number))

    if int(number) in data_max:
        return norm_roman_max[int(number)]

    elif int(number) in data_mid:
        return norm_roman_mid[int(number)]

    elif len(number) == 4:

        first_number = number[0] + "000"
        first_rom_num = norm_roman_max[int(first_number)]

        second_number = number[1]
        if int(second_number) == 0:
            second_rom_num = ''
        else:
            second_number = number[1] + "00"
            second_rom_num = norm_roman_max[int(second_number)]

        third_number = number[2]
        if int(third_number) == 0:
            third_rom_num = ''
        else:
            third_number = number[2] + "0"
            third_rom_num = norm_roman_mid[int(third_number)]

        fourth_number = number[3]
        if int(fourth_number) == 0:
            fourth_rom_num = ''
        else:
            fourth_rom_num = norm_roman_min[int(fourth_number)]

        return first_rom_num + second_rom_num + third_rom_num + fourth_rom_num

    elif len(number) == 3:

        first_number = number[0] + "00"
        first_rom_num = norm_roman_max[int(first_number)]

        second_number = number[1]
        if int(second_number) == 0:
            second_rom_num = ''
        else:
            second_number = number[1] + "0"
            second_rom_num = norm_roman_mid[int(second_number)]

        third_number = number[2]
        if int(third_number) == 0:
            third_rom_num = ''
        else:
            third_rom_num = norm_roman_min[int(third_number)]

        return first_rom_num + second_rom_num + third_rom_num

    elif len(number) == 2:

        first_number = number[0] + "0"
        first_rom_num = norm_roman_mid[int(first_number)]

        second_number = number[1]
        second_rom_num = norm_roman_min[int(second_number)]

        return first_rom_num + second_rom_num

    else:
        return norm_roman_min[int(number)]


#------------------------------------------------------TEST-------------------------------------------------------------


print(solution(1889))
print(solution(1300))
print(solution(900))
print(solution(1509))
print(solution(9))
print(solution(100))
print(solution(70))
print(solution(330))
print(solution(1042))


#-------------------------------------------------------RESULT----------------------------------------------------------


# MDCCCLXXXIX
# MCCC
# CM
# MDIX
# IX
# C
# LXX
# CCCXXX
# MXLII