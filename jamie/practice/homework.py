layer = int(input("Enter:"))  # 盡量不要hardcode

for i in range(1, layer + 1):
    for j in range(1, layer + 1):
        if i == j:
            print("*" * i)

for i in range(1, layer + 1):
    for j in range(1, layer + 1):
        if i == j:
            print(" " * (layer - i) + "*" * i)

for i in range(1, layer + 1):
    for j in range(1, layer + 1):
        if i == j:
            print("*" * (layer - i + 1))