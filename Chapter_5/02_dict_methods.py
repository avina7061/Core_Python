marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error


d = {"name": "Avinash", "age": 20}

print(d.get("name"))     # Avinash
print(d.get("marks"))    # None
print(d.get("marks", 0)) # 0 (default value)


d = {"a": 1, "b": 2}
print(d.keys())  # dict_keys(['a', 'b'])


print(d.values())  # dict_values([1, 2])


print(d.items())  # dict_items([('a', 1), ('b', 2)])

for k, v in d.items():
    print(k, v)



d = {"a": 1}
d.update({"b": 2})

print(d)  # {'a': 1, 'b': 2}



d = {"a": 1, "b": 2}
print(d.pop("a"))  # 1
print(d)           # {'b': 2}



d = {"a": 1, "b": 2}
print(d.popitem())  # ('b', 2)


d.clear()
print(d)  # {}


d = {"a": 1}

print(d.setdefault("a", 100))  # 1 (already exists)
print(d.setdefault("b", 100))  # 100 (added)

d.update({"c":d.get("c",0)+1})

print(d)  # {'a': 1, 'b': 100}


d = {"a": 1, "b": 2}
print(len(d))  # 2