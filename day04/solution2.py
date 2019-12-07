def is_valid_password(n: int) -> bool:
    s = str(n)
    # not decreasing
    if list(s) != sorted(s):
        return False
    # adjacent doubles are not part of a larger group of matching digits
    return 2 in [s.count(i) for i in set(s)]


print(sum(1 for n in range(136760, 595731) if is_valid_password(n)))
