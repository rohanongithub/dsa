# this is to merge two sorted arrays 
left = [1,2,4,6]
right = [1,4,6,8,8,8,9,32]

def merge_sorted_arrays(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left) :
        while i < len(left):
          result.append(left[i])
          i += 1
    else :
        while j < len(right):
            result.append(right[j])
            j += 1
    return result
merged_arr = merge_sorted_arrays(left,right)
print(merged_arr)
