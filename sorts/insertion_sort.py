nums = [-1,2,3,4,2,7,9,1]

for i in range(1, len(nums)):
    if nums[i]<nums[i-1]:
        key = nums[i]
        for j in range(i-1,-1,-1):
            if nums[j]>key:
                nums[j+1]=nums[j]
print(nums)