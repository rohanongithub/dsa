# TC: O(n^2) SC: O(1) - Two pointer approach to move zeros to end while maintaining relative order
nums = [1,2,0,4,3,0,0,3,5,1]
n = len(nums)
for i in range(0,n-1):
    if nums[i] == 0:
        j = i+1 
        while nums[j] == 0 and j<n-1:
            j += 1 
        nums[i],nums[j] = nums[j],nums[i]
print(nums)