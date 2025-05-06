s = ' one two three four five six'

words = s.split()
print(words)

len(words)

for i in range(1,len(words),2):
    words[i] = words[i][::-1]

output = ' '.join(words)
print(output)

s = 'a5b4c3'
ss = print(s.split())


