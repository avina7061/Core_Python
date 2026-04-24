print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):
    print(i)

for i in range(5):
    print(i)

for i in range(2, 7):
    print(i)

for i in range(1, 10, 2):  #
    print(i)

# for (int i = 1; i < 10; i += 2) { it work same as this
#     System.out.println(i);
# }

for i in range(10, 0, -1):  # it run 1 steps backward until > 0
    print(i)

# direct get all value from list
arr = [1, 2, 3, 4]

for x in arr:
    print(x)

# While Lopps
i = 0
while i < 5:
    print(i)
    i += 1

# double for loop

for i in range(3):
    for j in range(2):
        print(i, j)

for ch in "avinash":
    print(ch)

# Loops in HashMap

d = {"a": 1, "b": 2}

for key, val in d.items():
    print(key, val)
