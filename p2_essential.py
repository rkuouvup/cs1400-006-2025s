s = "Hello World"
for c in s:
    print(c)
for c in s:
    print(ord(c))

print([c.isalpha() for c in s])
print([c.isupper() for c in s])
print([c.islower() for c in s])