#''' Problem 19: '''

nums = [3, 0, 1]

n = len(nums)

expected = n * (n + 1) // 2

actual = 0

for num in nums:
    actual += num

print(expected - actual)
