name = "harry"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())

name.startswith("ha")   # True
name.endswith("rry")    # True

name.upper()      # "HARRY"
name.lower()      # "harry"
name.capitalize() # "Harry"
name.title()      # "Harry" (useful for sentences)

name.replace("r", "x")   # "haxxy"


s = "  hello  "
s.strip()   # "hello"
s.lstrip()  # "hello  "
s.rstrip()  # "  hello"


name.find("r")   # 2 (first index)

name.count("r")  # 2

s = "a,b,c"
s.split(",")   # ['a', 'b', 'c']