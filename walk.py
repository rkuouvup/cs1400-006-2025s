direction = input("Please enter the direction (type exit to terminate the program): ")

while direction != "exit":
    if direction == "west":
        print("go west")
    elif direction == "east":
        print("go east")
    else:
        pass
    direction = input("Please enter the direction (type exit to terminate the program): ")