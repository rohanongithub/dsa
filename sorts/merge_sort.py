#note the import is made from another py file that contains merge algorithm not divide
from merge_array import merge_sorted_arrays

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr)
    mid = n//2
    left_arr = arr[ : mid]
    right_arr = arr[mid : ]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge_sorted_arrays(left_arr,right_arr)

# testing
que = [3,1,5,7,3,2,8,0,4,2]
output = merge_sort(que)
print(output)
