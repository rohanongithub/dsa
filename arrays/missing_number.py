nums = [0,1,2,3,4,8,5,9,6] 
n = len(nums)
hm = [0]*(n+1)
for num in nums:
    hm[num] += 1
for i in range(0,len(hm)):
    if hm[i] == 0:
        print(i)