#''' Problem 35: '''

nums = list(map(int, input("Enter elements: ").split()))

left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

print("Minimum element:", nums[left])
