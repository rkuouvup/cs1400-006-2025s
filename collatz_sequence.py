import argparse

def collatz_next(n):
    if n % 2 == 0:
            n = n // 2
    else:
        n = 3 * n + 1
    return n

def collatz_seq_generation(n):
    seq = [n]
    while n != 1:
        n = collatz_next(n)
        seq.append(n)
    return seq

def print_collatz(lst):
    for i in range(len(lst)):
         print(f"{i}: {lst[i]}")


def main():
    parser = argparse.ArgumentParser(description="Generate Collatz sequence")
    parser.add_argument("init", metavar = "n",
                        type=int, help="the initial number")
    args = parser.parse_args()
    #print(args.init)

    # call a function to generate the sequence
    col_seq = collatz_seq_generation(args.init)
    print(col_seq)

    # print the sequence
    print_collatz(col_seq)


if __name__ == "__main__":
    main()