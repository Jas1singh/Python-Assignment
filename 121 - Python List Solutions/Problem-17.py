#''' Problem 17: '''

nums = [-4, -1, 0, 3, 10]

result = [0] * len(nums)

left = 0
right = len(nums) - 1
index = len(nums) - 1

while left <= right:

    left_square = nums[left] ** 2
    right_square = nums[right] ** 2

    if left_square > right_square:
        result[index] = left_square
        left += 1
    else:
        result[index] = right_square
        right -= 1

    index -= 1

print(result)
