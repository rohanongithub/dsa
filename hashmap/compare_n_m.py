n = [2,3,1,4,5,2,4,3,1,4]
m = [3]
#how many times does m[i] repeat in n
#dont use brute force to compare each and every element with O(n*m)
#May encounter TLE error since over 10^8

hash_list = [0]*11

for num in n:
    hash_list[num] += 1

for num in m:
    if num == 0 or num>10:
        print(0)
    else:
        print(hash_list[num])

#time complexity is O(n+m)

  


