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


N = [[37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]]
A = 15
B = 165


def get_not_devided_lines(not_devided_lines, line):
    left = line[0]
    right = line[1]
    new_free_lines = list()
    for free_line in not_devided_lines:
        if left > free_line[1] or right < free_line[0]:
            new_free_lines.append([free_line[0], free_line[1]])
        elif left > free_line[0] and right < free_line[1]:
            new_free_lines.append([free_line[0], left])
            new_free_lines.append([right, free_line[1]])
        elif left < free_line[0] and right < free_line[1]:
            new_free_lines.append([right, free_line[1]])
        elif left > free_line[0] and right > free_line[1]:
            new_free_lines.append([free_line[0], left])
    print(new_free_lines)
    return new_free_lines


def count(lines):
    res = 0
    for line in lines:
        res += line[1] - line[0]
    return res


if __name__ == '__main__':
    not_devided_lines = [[A, B]]
    for line in N:
        not_devided_lines = get_not_devided_lines(not_devided_lines, line)
    print(count(not_devided_lines))
