matrix = [[7,22,17],[9,30,27],[13,14,12]]
def yupi(x):

    list = []
    count = 0
    for row in range(0, len(matrix)):
        for i in range(3):
            string = ''
            if matrix[row][i] % 2 != 0:
                string += "1"
                list.append(string)
            elif matrix[row][i] % 2 == 0:
                string += "0"
                list.append(string)
    with open('matrix', 'w') as file:
        #file.write(str(list))
        for k in range(3):
            for i in range(3):
                file.write(list[count] + ' ')
                count += 1
            file.write('\n')
yupi(matrix)
