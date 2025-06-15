# Initialize array of numbers
nums = [55,32,-97,99,3,67,-101,-1,100]

# Method 1: Find smallest number by tracking differences
h = 0  # Reference index
s = 0  # Track smallest difference

for i in range(0,len(nums)):
    if nums[h] - nums[i] < s:
        s = nums[h] - nums[i]
        smallest_index = i
    
print(nums[smallest_index])

# Method 2: Find largest number using max() function
# Initialize largest with first element
largest = nums[0]
# Compare each element with current largest
for i in range(0,len(nums)):
    largest = max(largest,nums[i])
print(largest)