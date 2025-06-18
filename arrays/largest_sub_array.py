nums = [-1,2,4,-19,9,3,5]
maxi = float('-inf')
n = len(nums)
total = 0
for num in nums:
    total = total + num
    maxi = max(maxi, total)
    if total < 0:
        total = 0
print(maxi)
