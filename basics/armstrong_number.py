# armstrong number

# 1634 = 1^4 + 6^4 + 3^4 + 4^4 
from math import *

def checkArmstrong(x):
    num = x
    inputLength = int(log10(num)+1)
    count = inputLength
    ld = 0
    sum = 0
    while count > 0:
            ld = num%10
            sum = sum + (ld**inputLength)
            num = num//10
            count = count - 1
    return print(sum == x) 

checkArmstrong(1634)

    