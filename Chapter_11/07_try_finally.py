def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return


    except Exception as e:
        print(e)
        return


    finally:
        print("Hey I am inside of finally")


main()

# print statement same work as finally if i use as normally but when i use inside any def function and want to return
# something the next statement after the return is not executed but the statement inside the finally executed
# after the return