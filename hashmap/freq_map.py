freq_map = {}
nums = [2,3,4,1,3,66,2,11,8,5,3,2,0]

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
#worst case is O(n)