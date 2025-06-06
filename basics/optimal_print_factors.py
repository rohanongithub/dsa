from math import *

def print_factors(x):
    num = x
    factors_array = []
    for i in range (1,int(sqrt(num)+1)):
        if(num%i == 0):
            factors_array.append(i)
            if(num//i != i ):
                factors_array.append(num//i)
    factors_array.sort()
    return(print(factors_array))
             

print_factors(2012)
# O(n/2) time complexity