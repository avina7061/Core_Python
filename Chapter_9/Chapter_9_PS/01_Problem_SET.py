# write 2 to 20 table in different files

def functions(num):
    val = 1
    f = open(f"files/text{num}.txt", "w")
    for i in range(num, num + 10):
        f.write(f"{num} X {val} = {num*val} \n")
        val=val+1

    f.close()


for i in range(2,21):
    functions(i)

# write basically does it open file and add all contents to it if yourun multiple times
# but append add same content again and again multiple times when you run it