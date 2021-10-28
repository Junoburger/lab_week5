input_num = abs(int(input("Please enter a positive integer greater than 1: ")))

num1, num2 = 1, 1
i = 0

if input_num == 1:
    print(num1)
else:
    while i < input_num:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        i += 1
