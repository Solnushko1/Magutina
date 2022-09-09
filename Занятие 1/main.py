a = "Курс Основы программирования начался"
b= (16823 * 12302) // 3092
print(b)
age = int(input())
name = input()
if age > 0 and age < 75:
    if age >= 16 and name != "Иван":
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")
    if age < 16:
        print(16-age, "ещё учиться")
second = int(input())
print(second//86400, "дней", second//3600, "часов", second//60, "мин", second, "сек")
n = int(input())
q = n + n**2 + n**3 + n**4 + n**5
print(q)
x, y = 1, 2
x, y = y, x
print(x, y)
s = int(input())
if s % 2 ==0:
    print("чётное")
else:
    print("нечётное")