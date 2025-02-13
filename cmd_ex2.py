import argparse

parser = argparse.ArgumentParser(description="Process integers")
# t = turtle.Turtle()
# t.forward(100)
# print("hello", end="")
parser.add_argument("nums", type = int, nargs="?", help="put integers")
args = parser.parse_args()
print(args.nums)