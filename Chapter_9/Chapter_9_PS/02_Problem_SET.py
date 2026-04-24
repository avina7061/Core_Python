word ="Donkey"


with open("file.txt","r") as f:
    content = f.read()


newContent=content.replace("Donkey", "######")

with open("file.txt","w") as f:
    f.write(newContent)


