#''' Problem 32: '''

nums = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

nums.sort(reverse=True)

print("Kth largest element:", nums[k - 1])
