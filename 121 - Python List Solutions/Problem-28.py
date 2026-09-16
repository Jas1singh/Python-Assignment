#''' Problem 28: '''

target = 7
nums = [2, 3, 1, 2, 4, 3]

left = 0
current_sum = 0
answer = len(nums) + 1

for right in range(len(nums)):

    current_sum += nums[right]

    while current_sum >= target:

        length = right - left + 1

        if length < answer:
            answer = length

        current_sum -= nums[left]
        left += 1

if answer == len(nums) + 1:
    answer = 0

print(answer)
