
def matrix_izmenineie(m):
        for row in range (0,len(m)):
            string = ''
            if row % 2 != 0:
                for t in range (0,len(m[row])):
                    string = string + "1" + '    '
                print(string)
            else:
                for t in range (0,len(m[row])):
                    string = string + "0" + '    '
                print(string)

def yupi_dly_otkrivaniy(f):
    array = []
    while True:
        x = f.readline().strip()
        if (x == ""):
            break
        array.append(str(x))
    return array

yupi_dly_chteniy = open("C:\\Users\\My\\PycharmProjects\\pythonProject\\Основы\\lesson 10\\ex2.txt", "r")
matrix = yupi_dly_otkrivaniy(yupi_dly_chteniy)
print("Начальная матрица:", matrix)


matrix = [[1,5,3],[8,2,4],[9,11,7]]
matrix_izmenineie(matrix)