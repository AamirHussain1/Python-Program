input_list = [4, 5, 1, 1, 2, 0, 0, 4, 5, 2]

freq_num = {}
for num in input_list:
    if num in freq_num:
        freq_num[num] += 1

    else:
        freq_num[num] = 1
print(freq_num)
non_repeating_key = next((k for k in input_list if freq_num[k] == 1), None)
print(non_repeating_key)
