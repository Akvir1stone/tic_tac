positions = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
win_con = False


def vis_game():
    print('\n')
    print(positions[0][0], ' | ', positions[0][1], ' | ', positions[0][2])
    print('_ ', '.', ' _ ', '.', ' _')
    print(positions[1][0], ' | ', positions[1][1], ' | ', positions[1][2])
    print('_ ', '.', ' _ ', '.', ' _')
    print(positions[2][0], ' | ', positions[2][1], ' | ', positions[2][2])


def p_turn(x, y, p):
    if positions[x][y] == ' ':
        positions[x][y] = p
        check_win_con()
    else:
        print('Позиция занята')
        p_turn(input_pos(input('Выберите строчку 1-3: ')), input_pos(input('Выберите столбик 1-3: ')), p)


def input_pos(a):
    while a == '' or int(a) > 3 or int(a) == 0:
        a = input('Введите корректное значение: ')
    return int(a) - 1


def check_win_con():
    global win_con
    if positions[0][0] == 'X' and positions[1][1] == 'X' and positions[2][2] == 'X':
        print('-----!!!!!!-----')
        print('Игрок Х победил')
        win_con = True
        return None
    elif positions[0][2] == 'X' and positions[1][1] == 'X' and positions[2][0] == 'X':
        print('-----!!!!!!-----')
        print('Игрок Х победил')
        win_con = True
        return None
    elif positions[0][0] == 'X' and positions[1][1] == 'X' and positions[2][2] == 'X':
        print('-----!!!!!!-----')
        print('Игрок Х победил')
        win_con = True
        return None
    elif positions[0][2] == 'X' and positions[1][1] == 'X' and positions[2][0] == 'X':
        print('-----!!!!!!-----')
        print('Игрок Х победил')
        win_con = True
        return None
    for i in range(3):
        if positions[i][0] == 'X' and positions[i][1] == 'X' and positions[i][2] == 'X':
            print('-----!!!!!!-----')
            print('Игрок Х победил')
            win_con = True
        elif positions[0][i] == 'X' and positions[1][i] == 'X' and positions[2][i] == 'X':
            print('-----!!!!!!-----')
            print('Игрок Х победил')
            win_con = True
        elif positions[i][0] == 'X' and positions[i][1] == 'X' and positions[i][2] == 'O':
            print('-----!!!!!!-----')
            print('Игрок O победил')
            win_con = True
        elif positions[0][i] == 'X' and positions[1][i] == 'X' and positions[2][i] == 'O':
            print('-----!!!!!!-----')
            print('Игрок O победил')
            win_con = True


def game():
    while True:
        vis_game()
        print('Ходит игрок X')
        p_turn(input_pos(input('Выберите строчку 1-3: ')), input_pos(input('Выберите столбик 1-3: ')), 'X')
        if win_con:
            break
        vis_game()
        print('Ходит игрок O')
        p_turn(input_pos(input('Выберите строчку 1-3: ')), input_pos(input('Выберите столбик 1-3: ')), 'O')
        if win_con:
            break


game()
