try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank You") #thank you always print if it execute try or catch block