import argparse
parser = argparse.ArgumentParser(description="Open a file")
parser.add_argument("file_name", metavar="name",
                    help="the file name", type=str)
args = parser.parse_args()

with open(args.file_name, "r") as f:
    lines = f.readlines()
print(lines)