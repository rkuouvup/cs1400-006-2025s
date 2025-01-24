direction = "none"

while True:
    if direction == "west":
        print("go west")
    elif direction == "east":
        print("go east")
    elif direction == "exit":
        break
    else:
        pass
    direction = input("Please enter the direction (type exit to terminate the program): ")