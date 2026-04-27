try:
    a = int(input("Hey, Enter a number: "))
    print(a)


except Exception as e:
    print(e)


else:
    print("I am inside else") # else only excute when try block execute
