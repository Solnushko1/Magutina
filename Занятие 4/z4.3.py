def number(a,b):
    for i in range(a - (a + 1) % 2, b - (b % 2), -2):
        print(i, end=" ")
number(int(input()),int(input()))