s = input()
s = s.split(' ')
for i in range(len(s)):
    min_idx = i
    for j in range(i+1,len(s)):
        if int(s[min_idx][-1]) > int(s[j][-1]):
            min_idx = j
    s[i], s[min_idx] = s[min_idx], s[i]

l = []
for i in s:
    l.append(i[:-1])
x = ' '.join(l)
print(x)