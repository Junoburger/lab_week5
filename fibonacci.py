input_num = abs(int(input("Please enter a positive integer greater than 1: ")))

num1, num2 = 1, 1
count = 0

if input_num == 1:
    print(num1)
else:
    print("Fibonacci sequence:")
    while count < input_num:
        print(num1)
        nth = num1 + num2
        # update values
        num1 = num2
        num2 = nth
        count += 1
