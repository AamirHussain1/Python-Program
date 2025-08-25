list1 = [10, 20, 30]
list2 = ['a', 'b', 'c', 'd', 'e']

appended_list = []
for items in zip(list1, list2):
    for pairs in items:
        appended_list.append(pairs)

if len(list1) > len(list2) or len(list2) > len(list1):
    combined_list = list1 + list2
    for element in combined_list:
        if element not in appended_list:
            appended_list.append(element)

print(appended_list)
