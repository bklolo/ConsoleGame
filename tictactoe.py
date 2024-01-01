
def printBoard(board):
    print(board['A1'] + '|' + board['A2'] + '|' + board['A3'])
    print('-+-+-')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'])
    print('-+-+-')
    print(board['C1'] + '|' + board['C2'] + '|' + board['C3'])

        

def checkWin(board):
    win = False

    # Check vertical wins
    for i in range(1, 4):
        if board[f'A{i}'] == board[f'B{i}'] == board[f'C{i}'] != ' ':
            win = True
            break

    # Check horizontal wins
    if board['A1'] == board['A2'] == board['A3'] != ' ':
        win = True
    elif board['B1'] == board['B2'] == board['B3'] != ' ':
        win = True
    elif board['C1'] == board['C2'] == board['C3'] != ' ':
        win = True

    # Check diagonal wins
    elif board['A1'] == board['B2'] == board['C3'] != ' ':
        win = True
    elif board['A3'] == board['B2'] == board['C1'] != ' ':
        win = True
    return win      


def is_draw(board):
    for val in board.values():
        if val == ' ':
            return False
    return True



board = {'A1':' ','A2':' ','A3':' ',
         'B1':' ','B2':' ','B3':' ',
         'C1':' ','C2':' ','C3':' '}

p1Turn = True

while True:
    # check win conditions
    if checkWin(board):
        printBoard(board)
        print(player + ' wins!')
        break
    # check draw condition
    if is_draw(board):
        printBoard(board)
        print("It's a draw!")
        break
    # ternary operator
    letter, player = ('X', 'Player 1') if p1Turn else ('O', 'Player 2')

    printBoard(board)
    print(player + ' move.')
    move = input()
    if move in board and board[move] == ' ':
        board[move] = letter
    else:
        print('Invalid input. Try again.')
        p1Turn = not p1Turn
    p1Turn = not p1Turn
