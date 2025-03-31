greetings = ("Hey", "Hello", "What's up?", "How are you?")

result1 = []
for e in greetings:
    if e.startswith('H'):
    #if e[0] == "H":
        result1.append(e)
print(result1)

result2 = [e for e in greetings if e.startswith('H')]
print(result2)

def startWithH(s):
    if s.startswith('H'):
        return True
    else:
        return False
    
result4_filter = filter(startWithH, greetings)
result4 = list(result4_filter)
print(result4)

def myFilter(fn, lst):
    r = []
    for e in lst:
        if fn(e):
            r.append(e)
        else:
            pass
    return r

result5 = myFilter(startWithH, greetings)