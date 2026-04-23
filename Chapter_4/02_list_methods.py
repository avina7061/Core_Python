friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)



l = [1, 2]
l.append(3)   # [1, 2, 3]


l = [1, 2, 4]
l.insert(2, 3)   # [1, 2, 3, 4]


l1 = [1, 2]
l2 = [3, 4]
l1.extend(l2)   # [1,2,3,4]


l = [10, 20, 30]
l.pop(1)   # removes 20   remove by index


l = [1, 2, 3]
l.remove(2)   # removes first 2  remove by value


l.clear()   # []


l = [3,1,2]
l.sort()   # [1,2,3]

l.sort(reverse=True)


l.reverse()

l = [1,2,2,3]
l.count(2)   # 2


l.index(2)   # first occurrence


l2 = l.copy()


