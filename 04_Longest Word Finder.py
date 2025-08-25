words = ["apple", "banana", "grapefruit", "kiwi", "pineapple", "pear"]

seen = set()
longest_word = {}
max_length = []
result = []

for items in words:
    char_count = 0
    if items not in seen:
        seen.add(items)
        longest_word[items] = len(items)

highest = max(longest_word.values())

for item, freq in longest_word.items():
    if freq == highest:
        result.append(item)

print(result)
