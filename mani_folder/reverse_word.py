name = "attend interviews to gaain knowledge"

n = name.split()
new = reversed(n)
out = []

for word in new:
    out.append(word[::-1])

output = " ".join(out)
print(output)


