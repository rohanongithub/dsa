def print_factors(x):
    num = x
    factors_array = []
    for i in range (1,num//2):
        if(num%i == 0):
            factors_array.append(i)
    factors_array.append(num)
    return print(factors_array)

print_factors(2012)
# O(n/2) time complexity