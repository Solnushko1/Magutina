def years(x):
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("Да")
else:
    print("Нет")
years(int(input()))