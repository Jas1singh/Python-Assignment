#''' Problem 31: '''

nums = list(map(int, input("Enter elements: ").split()))

left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        left = mid + 1

print("Peak element index:", left)
print("Peak element:", nums[left])
