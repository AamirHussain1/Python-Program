input_list = [1, 2, 3, 2, 3, 1, 3, 5, 5, 5, 7, 7,7]

num_freq = {}
for num in input_list:
    if num in num_freq:
        num_freq[num] += 1

    else:
        num_freq[num] = 1

get_key = [k for k, v in num_freq.items() if v % 2 != 0]
print(get_key)