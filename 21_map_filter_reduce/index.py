# map example
nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))
print(result)


# filter example
nums2 = [1, 2, 3, 4, 5]

result2 = list(filter(lambda x: x % 2 == 0, nums2))
print(result2)


# reduce example
from functools import reduce #reduce import

nums3 = [1, 2, 3, 4]

result3 = reduce(lambda x, y: x + y, nums3)
print(result3)


# chaining
nums4 = [1, 2, 3, 4, 5]

data = reduce(
    lambda x, y: x + y,
    filter(lambda x: x % 2 == 0,
        map(lambda x: x * 2, nums4)
    )
)

print(data)
