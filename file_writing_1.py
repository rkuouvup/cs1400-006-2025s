f = open("test.txt", "a") # "w"

f.writelines("We have exam next week")

f.close()

with open("test.txt", "w") as f:
    f.writelines("hello world")

print("end of the program")