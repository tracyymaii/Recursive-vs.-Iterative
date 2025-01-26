# Title: Recursive vs. Iterative
# Purpose: To compare the runtime of different implementations of 
#          the same algorithm with the same time complexity
# Author: Tracy Mai
# Date: January 25, 2025

import time
import csv
import sys

def main():

    baseDouble = 2.718281828459045091
    baseInt = 1000003
  
    # Manually increased the recursion limit in python to find the max n of my own computer
    sys.setrecursionlimit(30000001)

    with open("recursive_vs._iterative_time.csv", "w", newline = "") as data:
        input = csv.writer(data)

        for n in range(30000001):
            output = [n]
            output.append(f"{runTime(doubleIterativePower, baseDouble, n):.1f}")
            output.append(f"{runTime(doubleRecursivePower, baseDouble, n):.1f}")
            output.append(f"{runTime(integerIterativePower, baseInt, n):.1f}")
            output.append(f"{runTime(integerRecursivePower, baseInt, n):.1f}")
            input.writerow(output)

# Double Iterative Power
# Iteratively calulates the exponential total based on the base and exponent given
# @param the base for double functions, the exponent
# @return the exponential total
def doubleIterativePower (base1, exponent):

    retVal = 1.0
    if exponent < 0:
        return 1.0/doubleIterativePower(base1, -exponent)
    else:
        for x in range(exponent):
            retVal = retVal * base1
    return retVal

# Double Recursive Power
# Recursively calulates the exponential total based on the base and exponent given
# @param the base for double functions, the exponent
# @return the exponential total
def doubleRecursivePower (base1, exponent):
    if exponent < 0:
        return 1.0/doubleRecursivePower(base1, -exponent)
    elif exponent == 0:
        return 1.0
    else:
        return base1 * doubleIterativePower(base1, exponent - 1)

# Interger Iterative Power
# Iteratively calulates the exponential total based on the base and exponent given
# @param the base for integer functions, the exponent
# @return the exponential total
def integerIterativePower (base2, exponent):
    retVal = 1.0
    if exponent < 0:
        return 1.0/integerIterativePower(base2, -exponent)
    else:
        for x in range(exponent):
            retVal = retVal * base2

    return retVal

# Interger Recursive Power
# Iteratively calulates the exponential total based on the base and exponent given
# @param the base for integer functions, the exponent
# @return the exponential total
def integerRecursivePower (base2, exponent):
    if exponent < 0:
        return 1.0/integerRecursivePower(base2, -exponent)
    elif exponent == 0:
        return 1.0
    else:
        return base2 * integerRecursivePower(base2, exponent - 1)

# Run Time
# Calculates the runtime of each function and converts it to microseconds
# @param the implementations shown above, the base depending on the implementation, the exponent
# @return the runtime in microseconds
def runTime(implementation, base, exponent):
    startTime = time.perf_counter()
    implementation(base, exponent)
    endTime = time.perf_counter()
    microSeconds = 1000000 * (endTime-startTime)

    return microSeconds
        

main()