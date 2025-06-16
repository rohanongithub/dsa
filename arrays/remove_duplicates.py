# This code removes duplicates from an array and fills remaining positions with zeros
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
hm = {}

for num in nums:
    if num not in hm:
        hm[num] = 1
new_nums = []
for n in hm:
    new_nums.append(n)
new_nums_len = len(nums) - len(new_nums) + 2
spare_count = len(nums) - len(new_nums)
ref_count = spare_count
while ref_count > 0:
    new_nums.append(0)
    ref_count -= 1
print(hm)
print(nums)
print(new_nums)
print(spare_count)