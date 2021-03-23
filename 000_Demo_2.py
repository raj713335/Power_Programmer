
for xx in range(0, 4):
    a = int(input())

    arraylist = []

    for i in range(0, a):
        arraylist.append(list(input()))

    siz = 9
    temp_list = []

    for i in range(0, 1):
        for j in range(0, a):
            temp = int(arraylist[j][i])

            if temp < siz:
                temp_list = [[j, i]]
                siz = temp
            elif temp == siz:
                temp_list.append([j, i])

    # print("hex")
    # print(temp_list)
    # print(temp_list[0])

    if len(temp_list) == 1:
        arraylist[temp_list[0][0]][temp_list[0][1]] = '9'
    elif len(temp_list) > 1:
        if arraylist[temp_list[0][0]][temp_list[0][1]] == '9':
            pine = []
            for each in temp_list:
                pine.append(each[0])

            siz = 9
            temp_list_one = []
            for i in range(1, 2):
                for j in pine:
                    temp = int(arraylist[int(j)][i])

                    if temp < siz:
                        temp_list_one = [[j, i]]
                        siz = temp
                    elif temp == siz:
                        temp_list_one.append([j, i])

            arraylist[temp_list_one[0][0]][temp_list_one[0][1]] = '9'
        else:
            pine = []
            for each in temp_list:
                pine.append(each[0])

            siz = 9
            temp_list_one = []
            for i in range(1, 2):
                for j in pine:
                    temp = int(arraylist[int(j)][i])

                    if temp < siz:
                        temp_list_one = [[j, i]]
                        siz = temp
                    elif temp == siz:
                        temp_list_one.append([j, i])

            arraylist[temp_list_one[0][0]][temp_list[0][1]] = '9'

    total = 0
    for each in arraylist:
        total += int("".join(each))

    print(total)

"""
3
10
50
30
5
94
90
92
93
93
8
70
42
75
67
64
79
67
34
2
99
99
"""
