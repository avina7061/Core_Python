f = open("myfile.txt")

# lines = f.readlines()
# print(lines, type(lines))  # if we use readlines() it return list of lines

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()  # by this way we read line by line the file

f.close()

#    ===============================
# WRITE (overwrite)
# ===============================
f = open("demo.txt", "w")
f.write("Hello World\n")
f.write("Hello World\n")
f.close()
# when we call its multiple time this sentence written only single time not appended one by one


# ===============================
# APPEND
# ===============================
f = open("demo3.txt", "a")
f.write("This line is appended\n")
f.close()

# ===============================
# READ FULL FILE
# ===============================
f = open("demo.txt", "r")
data = f.read()
print("Full file:")
print(data)
f.close()

# ===============================
# READ LINE BY LINE
# ===============================
f = open("demo.txt", "r")
print("Line by line:")
for line in f:
    print(line.strip())
f.close()

# Or
ft=open("demo3.txt","r")
line = ft.readline()
while (line != ""):
    print(line)
    line = ft.readline()
ft.close()

# ===============================
# READ ONE LINE
# ===============================
f = open("demo.txt", "r")
print("First line:")
print(f.readline())
f.close()

# ===============================
# READ ALL LINES (LIST)
# ===============================
f = open("demo.txt", "r")
lines = f.readlines()
print("All lines:", lines, type(lines))
f.close()

# ===============================
# POINTER FUNCTIONS
# ===============================
f = open("demo.txt", "r")
print("Pointer:", f.tell())

f.read(5)
print("After reading 5 chars:", f.tell())

f.seek(0)
print("After seek:", f.tell())
f.close()

# ===============================
# WRITE MULTIPLE LINES
# ===============================
f = open("demo2.txt", "w")
f.writelines(["A\n", "B\n", "C\n"])
f.close()

# ===============================
# FILE MODES INFO
# ===============================
# "r"  → read
# "w"  → write (overwrite)
# "a"  → append
# "x"  → create new file
# "rb" → read binary
# "wb" → write binary


# ===============================
# CHECK FILE EXISTS
# ===============================
import os

print("Exists:", os.path.exists("demo.txt"))

# ===============================
# DELETE FILE
# ===============================
# os.remove("demo2.txt")


# ===============================
# RENAME FILE
# ===============================
# os.rename("demo2.txt", "newname.txt")
