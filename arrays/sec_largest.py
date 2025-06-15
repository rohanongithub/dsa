#normal way
# Method 1: Two-pass approach - First find largest, then find second largest

nums = [55,32,-97,99,3,67,-101,-1,100,101]
largest = nums[0]
for i in range(len(nums)):
    largest = max(largest,nums[i])
sec_largest = nums[0]
for j in range(len(nums)):
    if nums[j] < largest:
        sec_largest = max(sec_largest,nums[j])
    
print(sec_largest)

#optimal solution
# Method 2: Single-pass approach - Track both largest and second largest in one iteration

l = float('-inf')
sl = float('-inf')
for k in range(0,len(nums)):
    if nums[k] > l :
        sl = l
        l = nums[k]
    elif nums[k] > sl and nums[k] != l:
        sl = nums[k]
print(sl)