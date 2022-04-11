
#-----------------------------Bit Counting-----------------------

# Write a function that takes an integer as input, and returns the number of bits
# that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010,
# so the function should return 5 in this case

#--------------------------------------------------------------------


def count_bits(n):

    number = n
    bin_num = f'{int(number):08b}'

    answer = []

    for each_number in bin_num:
        if int(each_number) != 0:
            answer.append(int(each_number))
        else:
            continue

    return sum(answer)


print(count_bits(1234))
#%