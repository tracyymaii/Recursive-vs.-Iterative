
#iterative and recursive implementation
# double and int for both 


def doubleIterativePower (base, exponent):
    retVal = 1.0
    if exponent < 0:
        return 1.0/doubleIterativePower(base, -exponent)
    else:
        for x in range(exponent):
            retVal = retVal * base

    return retVal

def integerIterativePower (base, exponent):
    retVal = 1.0
    if exponent < 0:
        return 1.0/integerIterativePower(base, -exponent)
    else:
        for x in range(exponent):
            retVal = retVal * base

    return retVal

def doubleRecursivePower (base, exponent):
    if exponent < 0:
        return 1.0/doubleRecursivePower(base, -exponent)
    elif (exponent == 0):
        return 1.0
    else:
        return base * doubleIterativePower(base, exponent - 1)

def integerRecursivePower (base, exponent):
    if exponent < 0:
        return 1.0/integerRecursivePower(base, -exponent)
    elif (exponent == 0):
        return 1.0
    else:
        return base * integerRecursivePower(base, exponent - 1)
        

print("yay compiled")