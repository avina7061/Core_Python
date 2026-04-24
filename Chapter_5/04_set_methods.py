s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))


s = {1, 2, 3}
s.add(4)

print(s)  # {1, 2, 3, 4}


s = {1, 2}
s.update([3, 4])

print(s)  # {1, 2, 3, 4}


s = {1, 2, 3}
s.remove(2)
print(2 in s) # it is use for check it is in set or not
print(s)  # {1, 3}


s = {1, 2, 3}
s.discard(5)  # no error  Removes element (no error if not present)

print(s)  # {1, 2, 3}


s.clear()
print(s)  # set()

a = {1, 2}
b = {3, 4}

print(a.union(b))  # {1, 2, 3, 4}


a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))  # {2, 3}


a = {1, 2, 3}
b = {2, 3}

print(a.difference(b))  # {1}


a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))  # True


a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))  # True


