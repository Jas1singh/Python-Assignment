#''' Problem 18: '''

nums = [2, 6, 4, 8, 10, 9, 15]

left = 0

while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
    left += 1

if left == len(nums) - 1:
    print(0)
else:
    right = len(nums) - 1

    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    minimum = nums[left]
    maximum = nums[left]

    for i in range(left, right + 1):
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])

    while left > 0 and nums[left - 1] > minimum:
        left -= 1

    while right < len(nums) - 1 and nums[right + 1] < maximum:
        right += 1

    print(right - left + 1)
