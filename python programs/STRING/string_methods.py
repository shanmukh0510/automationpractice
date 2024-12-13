#string methods

s = "hello world"
print(s.capitalize()) # capitalize

print(s.title())    #title

print(s.istitle())

print(s.upper())

print(s.isupper())

print(s.lower())

print(s.islower())

# swapcase - to convert lower to upper and upper to lower

str = "AbCdEf"

# index - find index of a string

p = "potato"
print(p.index('p',0,6))
print(p.index('o',2,6))

# find - find index of a string

a = "vivekananda"
print(a.find('i',0))
print(a.find('i',2))

# split
sentence = "a man walking on the road"
print(sentence.split())
name = 'development'
print(name.split())

print(name.split('e'))
print(name.split('e',2))
n = 'eating sleeping morning walking'
print(n.split('ing'))
print(n.split('ing',2))

#join

a = 'hi '
print(a.join('abcd'))





