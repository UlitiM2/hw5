game_board = [['', '', ''], ['', '', ''], ['', '', '']]

def print_board(board):
    print('-------------')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

player = 'X'
while True:
    print_board(game_board)
    row = int(input('Введите номер строки (от 1 до 3): ')) - 1
    col = int(input('Введите номер столбца (от 1 до 3): ')) - 1
    if row < 0 or row > 2 or col < 0 or col > 2:
        print('Некорректные координаты. Попробуйте еще раз.')
        continue
    if game_board[row][col] != '':
        print('Эта клетка уже занята. Попробуйте еще раз.')
        continue
    game_board[row][col] = player
    if check_win(game_board):
        print_board(game_board)
        print('Игрок', player, 'победил!')
        break
    if all([cell != '' for row in game_board for cell in row]):
        print_board(game_board)
        print('Ничья!')
        break
    player = 'O' if player == 'X' else 'X'
