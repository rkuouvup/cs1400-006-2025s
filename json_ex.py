import json

std1 = {"Q1": 85, "Q2": 78, "Q3": 61}
print(type(std1))
s = json.dumps(std1, indent=4)
print(type(s))
print(s)

with open("json_ex_output.txt", "w") as f:
    json.dump(std1, f)

