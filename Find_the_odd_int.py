

# -----------------------------------Find the odd int----------------------------------

# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# --------------------------------------------------------------------------------------

def find_it(seq):

    counts = dict()

    if len(seq) > 2:

        for num in seq:
            if str(num) not in counts:
                counts[str(num)] = 1
            else:
                counts[str(num)] = counts[str(num)] + 1

    else:
        return seq[0]


    for value in counts.values():
        if value % 2:
            return [int(number) for (number, count) in counts.items() if count == value][0]


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
print(find_it([10]))

