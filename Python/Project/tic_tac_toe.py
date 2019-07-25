def checkWinner():
    if(board['TL'] == board['TM'] == board['TR'] or 
       board['ML'] == board['MM'] == board['MR'] or 
       board['BL'] == board['BM'] == board['BR'] or 
       board['TL'] == board['ML'] == board['BL'] or 
       board['TM'] == board['MM'] == board['BM'] or 
       board['TR'] == board['MR'] == board['BR'] or 
       board['TL'] == board['MM'] == board['BR'] or 
       board['TR'] == board['MM'] == board['BL']):
        return True
    else:
        return False

board = {'TL':'#', 'TM':'#', 'TR':'#',
         'ML':'#', 'MM':'#', 'MR':'#', 
         'BL':'#', 'BM':'#', 'BR':'#'}

print('Welcome to Tic-Tac-Toe!!!')

winner = False
count = 0

marker = input("Player 1: Select the marker to Play 'X' or 'O':")
player1Marker = marker

while winner != True:
    print('Positions are TL TM TR ML MM MR BL BM BR ')
    print('Player 1: Select the position to enter the value:')
    position = input()
    
    count+=1

    if count>=5:
        if(checkWinner()):
            if player1Marker == marker:
                print('Player 1 Won the Match!!!')
                break
            else:
                print('Player 2 won the Match!!!')
                break

    if marker == "X":
        board[position] = 'X'
        marker = 'O'
    else:
        board[position] = 'O'
        marker = 'X'

    print('Player 2: Select the position to enter the value:')
    position = input()
    
    count+=1
    
    if marker == "X":
        board[position] = 'X'
        marker = 'O'
    else:
        board[position] = 'O'
        marker = 'X'

    if count>=5:
        if(checkWinner()):
            if player1Marker == marker:
                print('Player 1 Won the Match!!!')
                break
            else:
                print('Player 2 won the Match!!!')
                break
