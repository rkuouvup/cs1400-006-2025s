values = (False, True, False, False, False)

print(any(values))
print(all(values))

values = {False: True}
print(any(values))
values = {False}
print(any(values))


values = ["", (), {}, "hello", 100, 0, ("", )]
l = [e for e in values if e]
print(l)


