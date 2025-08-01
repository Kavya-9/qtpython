t = (1, 2, 3, 2, 4, 2)
repeats = [x for x in t if t.count(x) > 1]
print(set(repeats))

