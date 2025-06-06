hashmap = {}

nums = [1,2,4,3,5,6,1,4,2,9,3]

for i in range(0,len(nums)):
    hashmap[nums[i]] = hashmap.get(nums[i],0)+1

print(hashmap)