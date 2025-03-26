toys = ("bicycle", "train", "doll", "teddy bear",
        "kite", "ball", "video game set")

sorted_toys = sorted(toys, key=len)

for toy in sorted_toys:
    print(toy)

for i in range(0, len(sorted_toys), 2):
    print(f"{(i//2)+1:2}. {sorted_toys[i]}")

print(list(enumerate(sorted_toys, start=1)))

for (c, t) in enumerate(sorted_toys[::2], start=1):
    print(f"{c:2}. {t}")