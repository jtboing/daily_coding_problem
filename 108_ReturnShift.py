def return_shift(a, b):
    if a == b:
        return True

    for _ in range(len(a)):
        a = a[1:] + a[0]

        if a == b:
            return True

    return False

result = return_shift("eee", "cdeab")
print(result)