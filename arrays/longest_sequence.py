# This program finds the length of the longest sequence of consecutive integers in an unsorted list.
# It uses a set for efficient lookups and checks for the start of each possible sequence,
# ensuring an optimal O(n) time complexity.

nums = [100, 4, 200, 1, 3, 2]

my_set = set()
for num in nums:
    my_set.add(num)

maxi = 0
for num in my_set:
    if num - 1 not in my_set:
        x = num
        count = 1
        while x + 1 in my_set:
            count += 1
            x += 1
        maxi = max(maxi, count)

print(maxi)
