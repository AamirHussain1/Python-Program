list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 7, 9]
list3 = [3, 5, 11, 13, 2]

seen = set()
common_list = []
common_num = []

for all_num in zip(list1, list2, list3):
    for num in all_num:
        common_list.append(num)

for num in common_list:
    if common_list.count(num) > 1 and num not in seen:
        seen.add(num)
        common_num.append(num)

print(common_list)
print(common_num)
