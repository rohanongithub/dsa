# This code removes duplicates from an array and fills remaining positions with zeros
# Only works for positive numbers in the array, fails if there are negative integers
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
hm = [0]*20
print(nums)
for i in range(0,len(nums)):
    temp = nums[i]
    if hm[temp] != 1:
        hm[temp] += 1
new_nums = []
for j in range(0,len(hm)):
    if hm[j] == 1:
        new_nums.append(j)

spare_count = len(nums) - len(new_nums)
rem_count = spare_count+2
while spare_count > 0 :
    new_nums.append(0)
    spare_count -= 1

for k in range(0,len(nums)):
    nums[k] = new_nums[k]
print(nums)
print(rem_count)