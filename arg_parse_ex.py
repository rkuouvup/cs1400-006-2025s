import argparse

# python arg_parse_ex.py file_name 1 2 3 4 5
# ==> create a new file called "file_name"
# in the "file_name", 1 to 5 is written in each line
parser = argparse.ArgumentParser(description="Open a file and write integers")
parser.add_argument("file_name", metavar="name",
                    help="the file name", type=str)
parser.add_argument("numbers", metavar="N", nargs="+",
                    help="integers to be written in the file")
args = parser.parse_args()
"""
print(args.file_name)
print(args.numbers)
"""
"""
f = open(args.file_name, "w")
# file writing
f.close()
"""

with open(args.file_name, "w") as f:
    for e in args.numbers:
        f.writelines(e + "\n")