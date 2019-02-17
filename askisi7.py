
 
import random
 
 
def draw_board(pinakas):
    # ektiposi tou pinaka
    # lista me 10  stings
    print('\n')
    print(' 7' + ' '*4 + '|' + '8' + ' '*4 + '|' + '9' + ' '*4)
    print('   ' + pinakas[7] + '  ' + '|' + '  ' + pinakas[8] + '  ' + '|' + '  ' + pinakas[9] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print(' -----+-----+-----')
    print(' 4' + ' '*4 + '|' + '5' + ' '*4 + '|' + '6' + ' '*4)
    print('   ' + pinakas[4] + '  ' + '|' + '  ' + pinakas[5] + '  ' + '|' + '  ' + pinakas[6] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print(' -----+-----+-----')
    print(' 1' + ' '*4 + '|' + '2' + ' '*4 + '|' + '3' + ' '*4)
    print('   ' + pinakas[1] + '  ' + '|' + '  ' + pinakas[2] + '  ' + '|' + '  ' + pinakas[3] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print('\n')
 
 
def eisodosxristi():
   
    sign = ''
    while not (sign == 'X' or sign == 'O' or sign == 'Χ' or sign == 'Ο'):
        print('You want to play with Χ or Ο;')
        sign = input().upper()
 
    
    if sign == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
 
def sira():
   #dialegoume tixaia pios paizei protos o ipoloistis i o paxtis
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
 
def make_move(pinakas, sign, move):
    pinakas[move] = sign
 
 
def win(pinakas, mark): 
    # elegxos an nikise kapoios
    return ((pinakas[7] == mark and pinakas[8] == mark and pinakas[9] == mark) or 
    (pinakas[4] == mark and pinakas[5] == mark and pinakas[6] == mark) or 
    (pinakas[1] == mark and pinakas[2] == mark and pinakas[3] == mark) or 
    (pinakas[7] == mark and pinakas[4] == mark and pinakas[1] == mark) or 
    (pinakas[8] == mark and pinakas[5] == mark and pinakas[2] == mark) or 
    (pinakas[9] == mark and pinakas[6] == mark and pinakas[3] == mark) or 
    (pinakas[7] == mark and pinakas[5] == mark and pinakas[3] == mark) or 
    (pinakas[1] == mark and pinakas[5] == mark and pinakas[9] == mark)) 
 
def copy_board(pinakas):
    # antigrafi listas kai emfanisi
    pinakasCopy = []
    for i in pinakas:
        pinakasCopy.append(i)
    return pinakasCopy
 
def free_space(pinakas, move):
    # elexos eleftheris kinisis
    return pinakas[move] == ' '
 
def player_move(pinakas):
    # o paixtis dialegi kinisi
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(pinakas, int(move)):
        print('what is your next move?  [1-9]: ')
        move = input()
    return int(move)
 
def random_move(pinakas, movesList):
    # kinisi pou mpori na kani, none an den iparxi 
    possibleMoves = []
    for i in movesList:
        if free_space(pinakas, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def computer_move(pinakas, computerLetter):
    # grama tou ipologisti 
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
   #elegos an mpori na nikisi to pc
    for i in range(1, 10):
        pinakasCopy = copy_board(pinakas)
        if free_space(pinakasCopy, i):
            make_move(pinakasCopy, computerLetter, i)
            if win(pinakasCopy, computerLetter):
                return i
 
    #block
    for i in range(1, 10):
        boardCopy = copy_board(pinakas)
        if free_space(pinakasCopy, i):
            make_move(pinakasCopy, playerLetter, i)
            if win(pinakasCopy, playerLetter):
                return i
 
    # elegxos gonion 
    move = random_move(pinakas, [1, 3, 7, 9])
    if move != None:
        return move
 
    # epilogi kentrou
    if free_space(pinakas, 5):
        return 5
 
    # epilogi plevras
    return random_move(pinakas, [2, 4, 6, 8])
 
def full_board(pinakas):
   #true an iparxi xoros ston pinaka,alios false
    for i in range(1, 10):
        if free_space(pinakas, i):
            return False
    return True
 
 
print('Tic Tac Toe')
 
while True:
    
    theBoard = [' '] * 10
    playerLetter, computerLetter = eisodosxristi()
    turn = sira()
    print('First play: ' + turn)
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            # sira tou paixti
            draw_board(theBoard)
            move = player_move(theBoard)
            make_move(theBoard, playerLetter, move)
 
            if win(theBoard, playerLetter):
                draw_board(theBoard)
                print('Congratulations, you win!')
                gameIsPlaying = False
            else:
                if full_board(theBoard):
                    draw_board(theBoard)
                    print('draw!')
                    break
                else:
                    turn = 'computer'
 
        else:
            #sira ipologisti
            move = computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)
 
            if win(theBoard, computerLetter):
                draw_board(theBoard)
                print('Computer wins...Sorry you lost ')
                gameIsPlaying = False
            else:
                if full_board(theBoard):
                    draw_board(theBoard)
                    print('draw!')
                    break
                else:
                    turn = 'player'



    print('you want to play again? ')
    if not input().lower().startswith('y'):
        break
 

 
