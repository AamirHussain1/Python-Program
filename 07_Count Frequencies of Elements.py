input_list = [4, 6, 2, 6, 4, 4, 2, 7]

num_freq = {}
for num in input_list:
    if num in num_freq:
        num_freq[num] += 1

    else:
        num_freq[num] = 1

max_num = max(num_freq, key=num_freq.get)
get_num = num_freq[max_num]
get_key = [k for k,v in num_freq.items() if v == get_num]
print(get_key)
