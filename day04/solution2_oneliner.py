print(sum(list(s) == sorted(s) and 2 in [s.count(i) for i in s] for s in map(str, range(136760, 595731))))