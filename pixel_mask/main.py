from PIL import Image


def get_squares(x_min, x_max, y_min, y_max, h):
    squares = []
    while x_min < x_max or y_min < y_max:
        squares.append([[x_min, y_min], [x_min + h, y_min + h]])
        x_min += h
        y_min += h
    return squares


def get_average_from_squares(squares, img, obj_for_count, h):
    rgb_list = []
    rgb = [0, 0, 0]
    qty = 0
    for square in squares:
        for x in range(square[0][0], square[1][0], 1):
            for y in range(square[0][1], square[1][1], 1):
                rgb[0] += obj_for_count[x, y][0]  # r
                rgb[1] += obj_for_count[x, y][1]  # g
                rgb[2] += obj_for_count[x, y][2]  # b
                qty += 1
        rgb_list.append([round(rgb[0] / qty), round(rgb[1] / qty), round(rgb[2] / qty)])
        rgb[0] = 0
        rgb[1] = 0
        rgb[2] = 0
    return rgb_list


if __name__ == '__main__':
    y_min = int(input('y_min: '))
    y_max = int(input('y_max: '))
    x_min = int(input('x_min: '))
    x_max = int(input('x_max: '))
    h = int(input('h: '))
    # y_min = 50
    # y_max = 100
    # x_min = 50
    # x_max = 100
    # h = 5
    picture_name = str(input('Введите название фото с его расширением: '))

    img = Image.open(picture_name)  # Файл для перебора
    obj_for_count = img.load()
    f = open(picture_name, "rb")  # Файл для размера
    img_for_size = Image.open(f)

    width = img_for_size.size[0]  # Ширина
    height = img_for_size.size[1]  # Высота
    squares = get_squares(x_min, x_max, y_min, y_max, h)
    rgb_list = get_average_from_squares(squares, img, obj_for_count, h)
    count = 0
    for rgb in rgb_list:
        count += 1
        img_for_out = Image.new("RGB", (h, h),
                                (rgb[0], rgb[1], rgb[2]))
        img_for_out.save(f'out{count}.jpg')

    print(squares)
