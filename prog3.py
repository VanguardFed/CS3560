#******************************************************************* 
#                                                                    
#  Program:     Project 3                                            
#                                                                     
#  Author:      Trent Thompson
#  Email:       tt948912@ohio.edu
#                                                                    
#  Description: brief description of the program                    
#                                                                    
#  Date:        Febuary 28, 2017
#                                                                    
#*******************************************************************

import random

default_board=[['#' for col in range(4)] for row in range(4)]

def print_board(board):
    
    # for loop for rows
    for i in range(0,4):
        print "|--------------|--------------|--------------|--------------|"
        
        #for loop for row parts
        for k in range(0,6):
            print'|',
            
            #for loop for columns
            for j in range(0,4):
                sqr_num=j+i*4
                if k==0:
                    if sqr_num<10:
                        print '',sqr_num,
                    elif sqr_num>=10:
                        print sqr_num,
                else:
                    print '  ',
                print print_piece(board[i][j],k),'|',
                
            #new line after each row part
            print '\n',
            
    #line at bottom of board
    print "|--------------|--------------|--------------|--------------|"

def print_piece(piece, line):
    #the X piece dictionary
    x_dic={
        0:"         ",
        1:" \  /    ",
        2:"  \/     ",
        3:"  /\     ",
        4:" /  \    ",
        5:"         ",
    }
    #the O piece dictionary
    o_dic={
        0:"  __     ",
        1:" /  \    ",
        2:"|    |   ",
        3:"|    |   ",
        4:" \__/    ",
        5:"         ",
    }
    if piece=='x':
        return x_dic[line]
    elif piece=='o':
        return o_dic[line]
    else:
        return "         "

def who_won(board):
    if board[0][0]==board[1][1]==board[2][2]==board[3][3] and board[0][0]!='#':
        return board[0][0]
    elif board[0][3]==board[1][2]==board[2][1]==board[3][0] and board[0][3]!='#':
        return board[0][0]
    for i in range(0,4):
        if board[i][0]==board[i][1]==board[i][2]==board[i][3] and board[i][0]!='#':
            return board[i][0]
        elif board[0][i]==board[1][i]==board[2][i]==board[3][i] and board[0][i]!='#':
            return board[i][0]
    return '#'

def translate(board,sq):
    if sq<4:
        return board[0][sq]
    elif sq<8:
        return board[1][sq-4]
    elif sq<12:
        return board[2][sq-8]
    elif sq<16:
        return board[3][sq-12]
    else:
        return '#'

def move(board,sq,marker):
    if sq<4 and board[0][sq]=='#':
        board[0][sq]=marker
        return True
    elif sq<8 and sq>=4 and board[1][sq-4]=='#':
        board[1][sq-4]=marker
        return True
    elif sq<12 and sq>=8 and board[2][sq-8]=='#':
        board[2][sq-8]=marker
        return True
    elif sq<16 and sq>=12 and board[3][sq-12]=='#':
        board[3][sq-12]=marker
        return True
    else:
        print "ERROR: Invalid input"
        return False

def print_help(turn,players):
    line="-------------------\n"
    print"  0 |  1 |  2 |  3 \n"+line+"  4 |  5 |  6 |  7 \n"+line+"  8 |  9 | 10 | 11 \n"+line+" 12 | 13 | 14 | 15 \n"
    if turn=='x':
        player=players[0]
    else:
        player=players[1]
    print"It is "+player+"'s turn.\n"

def play_next_move(board,turn):
    moving=True
    while moving==True:
        square=input(turn+"'s move, enter the square to take: ")
        if square>=0 and square<=15 and translate(board,square)=='#':
            move(board,square,turn)
            moving=False
        else:
            print "ERROR:",square,"is not a valid square, try again."

def change_turn(turn):
    if turn=='x':
        return 'o'
    if turn=='o':
        return 'x'

def play():
    #game set up
    ingame_players=["player1","player2"]
    save=raw_input("Do you want to load a saved game? (y/n): ").lower()
    if save.lower()=='y':
        filename=raw_input("Enter the name of the save file: ")
        save=open(filename)
        #LOAD SAVE FILE HERE
        print "ok"
    else:
        ingame_players[0]=raw_input("Name of first player: ")
        ingame_players[1]=raw_input("Name of second player: ")
        playerX=random.choice(ingame_players)
        ingame_turn='x'
        ingame_board=default_board
        player0_wins=0
        player1_wins=0

    #main game loop
    quit=False
    while not quit:
        while who_won(ingame_board)=='#':
            active_turn=True
            while active_turn:
                choice=raw_input()
                if choice.lower()=='p':
                    print_board(ingame_board)
                elif choice.lower()=='h':
                    print_help(ingame_turn,ingame_players)
                elif type(eval(choice))==int:
                    if eval(choice)>=0 and eval(choice)<=15:
                        if move(ingame_board,eval(choice),ingame_turn):
                            active_turn=False
                    else:
                        print "ERROR: Enter a number between 0 and 15"
                elif choice.lower()=='s':
                    #SAVE GAME HERE
                    print'ok'
                elif choice.lower()=='r':
                    for i in range(0,4):
                        ingame_board[0][i]=change_turn(ingame_turn)
                    active_turn=False
                elif choice.lower()=='q':
                    quit=True
                    active_turn=False
                    return
                else:
                    print "ERROR: Invalid command/n"+"    Enter 'p' to print the board\n"+"    Enter 'h' to see square numbers and current turn\n"+"    Enter a number between 0 and 15 to play a piece in the square of the number you entered\n"+"    Enter 's' to save the game\n"+"    Enter 'r' to resign\n"+"    enter 'q' to quit without saving\n"
            #play_next_move(ingame_board,ingame_turn)
            counter=0
            for i in range(0,4):
                for j in range(0,4):
                    if ingame_board[i][j]=='#':
                        counter+=1
            if counter==0:
                break
            ingame_turn=change_turn(ingame_turn)

        if who_won(ingame_board)=='x':
            print "Game over,",playerX,"has won the game."
            ingame_board=default_board
            if playerX==ingame_players[0]:
                player0_wins+=1
            else:
                player1_wins+=1
            
            
        elif who_won(ingame_board)=='o':
            print "Game over,",playerO,"has won the game."
            ingame_board=default_board
            if playerO==ingame_players[0]:
                playerO_wins+=1
            else:
                player1_wins+=1
        else:
            print "Game over, draw."
            ingame_board=default_board
        
#GAME STARTER
play()
