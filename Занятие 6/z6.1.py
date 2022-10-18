def stroka(s):
    f = s.replace("а", '*')
    colvo = f.count('*')
    f2 = f.replace('*', '')
    print(f2,',', 'количество удалений:', colvo)
stroka(input('Введите строку:'))