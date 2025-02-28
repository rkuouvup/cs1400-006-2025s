def printMonth(monthNumber):
    monthList = ["January", "February", "March", "April", 
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"]
    try:
        monthInt = int(monthNumber)
        if monthInt > 0 and monthInt <= 12:
            return monthList[monthInt - 1]
        else:
            raise ValueError
    except ValueError:
        return "Error"
    except:
        return "unknown error"
    

answer = input("Enter the nth of month in a year: ")
result = printMonth(answer)
if (result == "Error"):
    print("Error")
else:
    print(f"The month is {result}")