try:
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    s = a + b
    print("The sum of the two numbers is:", s)
except ValueError:
    print("Error: Please enter valid numbers!")

