
nums = [1,3,2,3,4,5,6,7,8,9]
def check_sort(nums):
    for i in range(len(nums)-1):
         if nums[i] > nums[i+1]:
             return False
    return True

if check_sort(nums):
    print("Array is sorted")
else:
    print("Array is unsorted")