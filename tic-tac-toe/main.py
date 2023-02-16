def game():
    print()
    print(f"    0  1  2")  # Выводим координаты столбцов
    for i in range(3):     # Цикл для вывода координат строк
        row_in_game = f" {i}  {cell[i][0]}  {cell[i] [1]}  {cell[i][2]}"
        print(row_in_game)
    print()


def test():
    while True:
        num = input("Ваш ход: ").split()

        if len(num) != 2:  # Проверка, действительно ли ввели 2 значения
            print("Введите две цифры.")
            print("Пример: 0 1, 1 1, 2 0")
            continue

        x, y = num

        if not (x.isdigit()) or not (y.isdigit()):  # Проверка, действительно ли ввели цифры
            print("Введите комбинацию цифр.")
            print("Пример: 0 1, 1 1, 2 0")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:  # Проверка, входят ли числа в диапазонр [0 2]
            print("Цифры не  входят в диапазон")
            continue

        if cell[x][y] != " ":  # Проверка, свободна ли клетка
            print("Клетка занята, будте внимательней")
            continue

        return x, y


def victory():
    global player_x
    global player_o

    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))  # Победные компинации
    for comb in win:
        you_win = []
        for a in comb:
            you_win.append(cell[a[0]][a[1]])
        if you_win == ["X", "X", "X"]:
            print(f"Победитель - {player_x}")
            return True
        if you_win == ["O", "O", "O"]:
            print(f"Победитель - {player_o}")
            return True
    return False


print()
print()
print('Добро пожаловать в игру "Крестики - Нолики"')
print()
print("Игрок - X, введите ваше имя")
player_x = input()
print("Игрок - O, введите ваше имя")
player_o = input()
print()
print("ИГРА НАЧАЛАСЬ, УДАЧИ!)")

cell = [[" "]*3 for i in range(3)]
count = 0
while True:
    count += 1
    game()
    if count % 2 == 0:
        print(f"Ходит - {player_o}")
    else:
        print(f"Ходит - {player_x}")

    x, y = test()

    if count % 2 == 0:
        cell[x][y] = "O"
    else:
        cell[x][y] = "X"

    if victory():
        break

    if count == 9:
        print(" Ничья. Сыграем еще?")
        break