"""
Есть произвольно задаваемый основной отрезок [А, В], и есть N — количество произвольно задаваемых доп. отрезков.
Необходимо вычислить длину основного отрезка, на которой не происходит наложения дополнительных отрезков.

Пример:

А = 15, В = 165
N1 [37, 68]
N2 [52, 74]
N3 [118, 146]
N4 [35, 44]
N5 [37, 65]
N6 [46, 74]

Ответ: 83

"""


def devide_lines(not_devided_lines, line):
    """
    :param not_devided_lines: список основных отрезков
    :param line: список из двух точек, характеризирующих отрезок
    :return:
    """
    a = line[0]
    b = line[1]
    new_devided_lines = []
    for i in not_devided_lines:
        if i[0] < a and i[1] > b:
            new_devided_lines.append([i[0], a])
            new_devided_lines.append([b, i[1]])  # *--i[0]--a-----------------b--i[1]--*
        elif i[0] < a and i[1] < b:
            if i[1] > a:
                new_devided_lines.append([i[1], b])
            else:
                new_devided_lines.append(i)  # *-i[0]---a----------------------i[1]---b--*
                new_devided_lines.append([i[1], a])
                not_devided_lines.remove(i)
        elif i[0] > a and i[1] < b:
            continue  # *-a--i[0]----------------------i[1]----b--------*
        elif i[0] > a and b < i[1]:
            new_devided_lines.append([b, i[1]])  # # *-a--i[0]-----------------------b---i[1]-----*
    return new_devided_lines


if __name__ == '__main__':
    A = 15
    B = 165
    not_devided_lines = [[A, B]]
    N = [[37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]]
    for line in N:
        not_devided_lines = devide_lines(not_devided_lines, line)
    print(not_devided_lines)
