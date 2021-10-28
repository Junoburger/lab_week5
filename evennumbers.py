input_num = abs(int(input("Please enter a positive integer: ")))


i = 1
while i <= input_num:
    if (2*i) % 2 == 0:
        print(2*i)
    i = i + 1
