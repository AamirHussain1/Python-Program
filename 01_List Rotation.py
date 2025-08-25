nums = [1, 2, 3, 4, 5]
k = 2

for items in nums:
    if len(nums) < k:
        break

    else:
        rotated_list = nums[k:] + nums[0:k]

print(rotated_list)