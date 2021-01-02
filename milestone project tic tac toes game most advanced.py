print('Welcome to tic tac toe game')
re=['#','1','2','3','4','5','6','7','8','9']

def display(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
display(re)

def name_ask():
    import random
    a1=input('player1 what is your good name ')
    a2=input('player2 what is your good name ')
    x=input(f'{a1} choose your character to play ')
    y=input(f'{a2} choose your character to play ')
    l=random.choice([1,2])
    if l==1:
        print(f'{a1} wins the toss')
        p1=a1
        p2=a2
        lo=x
        le=y
    elif l==2:
        print(f'{a2} wins the toss')
        p1=a2
        p2=a1
        lo=y
        le=x
        
    k=[p1,p2,lo,le]
    return k


def player1_ask(l):
    a1=l[0]
    a2=l[1]
    x=l[2]
    y=l[3]
    c1=False
    c2=False
    while c1==False:
        e=input(f'{a1} choose the position in which you want to enter {x} on num pad ')
        if e.isdigit():
            if int(e) in range(1,10):
                c1=True
            else:
                print('You are out of range, choose a position between 1-9 on num pad')
        else:
            print('Sorry it is not a digit')
        
    a2= int(e)
    return a2

def player1_allocation(a,t,o):
    x=t[2]
    board=o
    if board[a]==' ':
            board[a]=x
    else:
            print('Sorry this position is already taken')
            player1_allocation(player1_ask(t),t,o)
    return board
            
def player2_ask(l):
    a1=l[0]
    a2=l[1]
    x=l[2]
    y=l[3]
    c1=False
    c2=False
    while c1==False:
        e=input(f'{a2} choose the position in which you want to enter {y} on num pad ')
        if e.isdigit():
            if int(e) in range(1,10):
                    c1=True
            else:
                print('You are out of range, choose a position between 1-9 on num pad')
        else:
            print('Sorry it is not a digit')
    a2= int(e)
    return a2
def player2_allocation(a,t,o):
    board=o
    y=t[3]
    if board[a]==' ':
            board[a]=y
    else:
            print('Sorry this position is already taken')
            player2_allocation(player2_ask(t),t,o)
    return board
            
def check_winner(l,t):
    board=t
    a1=l[0]
    a2=l[1]
    x=l[2]
    y=l[3]
    t1=' '
    #diagonal check
    if board[1]==board[5] and board[1]==board[9] and board[1]==x:
        print(f'{a1} wins!')
        return False
    if board[1]==board[5] and board[1]==board[9] and board[1]==y:
        print(f'{a2} wins!')
        return False
    if board[7]==board[5] and board[7]==board[3] and board[5]==x:
        print(f'{a1} wins!')
        return False
    if board[7]==board[5] and board[7]==board[3] and board[5]==y:
        print(f'{a2} wins!')
        return False
    
    #columns check
    if board[7]==board[4] and board[7]==board[1] and board[7]==x:
        print(f'{a1} wins!')
        return False
    if board[7]==board[4] and board[7]==board[1] and board[7]==y:
        print(f'{a2} wins!')
        return False
    if board[8]==board[5] and board[8]==board[2] and board[8]==x:
        print(f'{a1} wins!')
        return False
    if board[8]==board[5] and board[8]==board[2] and board[8]==y:
        print(f'{a2} wins!')
        return False
    if board[9]==board[6] and board[9]==board[3] and board[9]==x:
        print(f'{a1} wins!')
        return False
    if board[9]==board[6] and board[9]==board[3] and board[9]==y:
        print(f'{a2} wins!')
        return False
    
    #rows check
    if board[9]==board[8] and board[9]==board[7] and board[9]==x:
        print(f'{a1} wins!')
        return False
    if board[9]==board[8] and board[9]==board[7] and board[9]==y:
        print(f'{a2} wins!')
        return False
    if board[4]==board[5] and board[4]==board[6] and board[4]==x:
        print(f'{a1} wins!')
        return False
    if board[4]==board[5] and board[4]==board[6] and board[4]==y:
        print(f'{a2} wins!')
        return False
    if board[1]==board[2] and board[1]==board[3] and board[1]==x:
        print(f'{a1} wins!')
        return False
    if board[1]==board[2] and board[1]==board[3] and board[1]==y:
        print(f'{a2} wins!')
        return False
    #match draw
    elif t1 not in board:
        print('Match draw!')
        return False
    else:
        return True
def game_play(t):
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    e=board
    game=t
    if game==True:
        j=name_ask()
    while game==True:
        e=player1_allocation(player1_ask(j),j,board)
        board=e
        display(e)
        game=check_winner(j,board)
        if game==True:
            e=player2_allocation(player2_ask(j),j,board)
            board=e
            display(board)
            game=check_winner(j,board)
        if game==False:
            game=check_game(1) 
            game_play(game)
            break
        
def check_game(i):
        o=i
        game='t'
        if o==0:
            return True
        elif o==1:
            while game!=True or game!=False:
                ki=input('Do you want to play again? y or n? ')
                if ki=='y':
                    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
                    game=True
                    return True
                    continue
                elif ki=='n':
                    game=False
                    return False
                else:
                    print('Sorry I cannot understand!')

game_play(check_game(0))          
