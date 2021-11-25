# Prints Pascal triangle to a .dat file
# the .dat file is read by LaTex to make a nice looking pdf

import numpy as np
import math
outputfile = "pascal_triangle.dat"
columns = ["x", "y", "value"]

N = 6
# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result:
with open(outputfile, 'w') as f:
    f.write('x y v\n')
    for y, row in enumerate(pascals_triangle(N)):
        for x, v in enumerate(row):
            f.write(f"{x-y/2} {-y} {v}\n")







