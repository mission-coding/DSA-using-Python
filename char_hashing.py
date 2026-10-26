# store frequency of q[i] in s
# a < s[i] < z
# asciicode of a to z = 97 to 122

s = "azyxyyzaaaa"
q = ["d", "a", "y", "x", "z"]


# Method 1
# freq = {}
# for i in q:
#     if i not in freq:
#         freq[i] = s.count(i)
# print(freq)

# Method 2
l = [0]*27
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    l[index] += 1

freq = {}

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    freq[ch] = l[index]

print(freq)
