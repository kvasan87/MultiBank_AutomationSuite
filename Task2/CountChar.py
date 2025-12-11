text = "hello world"

# Options
include_spaces = 'no' #give the value in lower case
ignore_case = 'yes' #give the value in lower case

# Apply case option
if ignore_case == "yes":
    text = text.lower()

counts = {}

for char in text:
    # Space option
    if include_spaces == "no" and char == " ":
        continue

    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

result = ""
for char in counts:
    temp = char + ":" + str(counts[char]) + ", "
    result = result+temp

# Remove last comma + space
if len(result) > 2:
    result = result[:-2]

print(result)