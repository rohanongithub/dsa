que = [1,3,2,5,6,9,7]
    #  j->     <-i

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

sorted_arr = bubble_sort(que)
print(sorted_arr)          


