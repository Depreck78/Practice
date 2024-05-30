def valid_input(prompt):
    while True:
        userinp = input(prompt)
        try:
            number = int(userinp)
            return userinp
        except ValueError:
            print("Invalid Input")

inp = valid_input("Enter Number: ")
rvs = inp [::-1]

if inp == rvs:
    print("It is Palindrome")
else:
    print("Not a Palindrome")