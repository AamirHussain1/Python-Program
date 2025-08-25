nums = [3, 1, 1, 2, 3, 3]

seen = set()

for items in range(len(nums)):
    for elements in range(items + 1, len(nums)):
        if nums[items] > nums[elements]:
            if items or elements not in seen:
                seen.add(items)
                nums[items], nums[elements] = nums[elements], nums[items]
print(nums)



