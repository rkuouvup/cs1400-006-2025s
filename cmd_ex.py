import sys

n = len(sys.argv)
print(f"Total argments passed: {n}")

print(f"Name of Python script: {sys.argv[0]}")
for i in range(1, n):
    print(sys.argv[i])