def is_valid_password(n: int) -> bool:
    s = str(n)
    # not decreasing
    if list(s) != sorted(s):
        return False
    # adjacent doubles
    if len(set(s)) == len(s):
        return False
    return True


print(sum(1 for n in range(136760, 595731) if is_valid_password(n)))
