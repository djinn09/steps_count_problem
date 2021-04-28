def count_steps(n):
    if not isinstance(n, int):
        return 0
    if (n == 1) or (n == 0):
        return 1
    elif (n == 2):
        return 2
    else:
        return count_steps(n - 3) + count_steps(n - 2) + count_steps(n - 1)


print(count_steps(4) == 7)

print(count_steps(10) == 274)

print(count_steps(8) == 81)

print(count_steps("") == 0)
