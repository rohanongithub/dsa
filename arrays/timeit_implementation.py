import timeit

setup_code = '''
import random
nums = random.sample(range(1, 10**6), 10**5)  # generate 100,000 unique random integers
'''

test_code = '''
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
'''

# Run timeit
execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1)
print(f"Execution time: {execution_time:.4f} seconds")
