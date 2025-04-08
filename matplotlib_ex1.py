"""
Select the correct Python Intepreter on VSCode:
1. Open the Command Palette by pressing
    Windows/Linux: Ctrl+Shift+P
    Mac: Cmd+Shift+P
2. Search Python Interpreter
3. Choose "Python: Select Interpreter"
4. Choose "Python 3.xx.x ('base') your_python_path  Conda
"""

import matplotlib.pyplot as plt
import random

x = [i for i in range(1, 10+1)]
y = [random.randint(1, 10) for i in range(1, 10+1)]


#plt.plot(x, y, "ro", markersize=10)
#plt.plot(x, y, "b-", linewidth=5)

#plt.scatter(x, y, c=y, s=[i*500 for i in y], alpha=0.5)


plt.scatter(x, y, marker="s", c="red")
plt.plot(x, y, "s-")

plt.show()
