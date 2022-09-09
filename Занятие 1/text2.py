
age = int(input())
name = input()
if age > 0 and age < 75:
    if age >= 16 and name != "Иван":
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")
    if age < 16:
        print(16-age, "ещё учиться")
