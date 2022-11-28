from random import randint
def yupi(n,m,max_znach):
    znach = [[randint(0, max_znach) for i in range(n)] for i in range(m)]
    for i in znach:
        print(*sorted(i))
yupi(int(input('Введите n:')),int(input('Введите m:')),int(input('Введите максимальую цифру:')))