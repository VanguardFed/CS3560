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


'''print_board(board) takes a board and then gives all the print statements needed to print out the full board.'''
def print_board(board):
    # for loop for rows
    for i in range(0,len(board)):
        print "|--------------"*len(board[0])+"|"
        #for loop for row parts
        for k in range(0,6):
            print'|',
            #for loop for columns
            for j in range(0,len(board[0])):
                sqr_num=j+i*len(board[0])
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
    print "|--------------"*len(board[0])+"|"

'''print_piece(piece, line) will return the string that is to be displayed as the 'line'th line of 'piece' piece.'''
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

'''who_won(board) will return either 'x' or 'o' if either has a winning position, otherwise it will return '#'.'''
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

'''move(board, sq, marker) will alter the board 'board' at square 'sq' to marker 'marker'.'''
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

'''print_help(turn,players) will print a diagram of which numbers \
corespond to which squares as well as who's turn it is.'''
def print_help(turn,players):
    line="-------------------\n"
    print"  0 |  1 |  2 |  3 \n"+line+"  4 |  5 |  6 |  7 \n"+line+"  8 |  9 | 10 | 11 \n"+line+" 12 | 13 | 14 | 15 \n"
    if turn=='x':
        player=players[0]
    else:
        player=players[1]
    print"It is "+player+"'s turn.\n"

'''play() will start and maintain a game of tic-tac-toe'''
def play():
    #game set up
    ingame_board=[['#' for col in range(4)] for row in range(4)]
    ingame_turn='x'
    ingame_players=["player1","player2"]
    player0_wins=0
    player1_wins=0
    draws=0
    savegame=raw_input("Do you want to load a saved game? (y/n): ").lower()
    if savegame.lower()=='y':
        #load saved game
        filename=raw_input("Enter the name of the save file: ")
        savefile=open(filename,'r')
        save=savefile.read().splitlines()
        ingame_players[0]=save[0]
        ingame_players[1]=save[1]
        player0_wins=eval(save[2])
        player1_wins=eval(save[3])
        draws=eval(save[4])
        ingame_board=eval(save[5])
        ingame_turn=save[6]
        savefile.close()
    else:
        ingame_players[0]=raw_input("Name of first player: ")
        ingame_players[1]=raw_input("Name of second player: ")
        playerX=random.choice(ingame_players)
        if playerX==ingame_players[0]:
            playerO=ingame_players[1]
        else:
            playerO=ingame_players[0]


    #main game loop
    quit=False
    while not quit:
        while who_won(ingame_board)=='#':
            active_turn=True
            while active_turn:
                choice=raw_input()
                try:
                    choice=int(choice)
                    #make a move
                    if choice>=0 and choice<=15:
                        if move(ingame_board,choice,ingame_turn):
                            active_turn=False
                    else:
                        print "ERROR: Enter a number between 0 and 15"
                except:
                    if len(choice)>1:
                        print "ERROR: Only submit a single character"
                    elif choice.lower()=='p':
                        #print baord
                        print_board(ingame_board)
                    elif choice.lower()=='h':
                        #run help
                        print_help(ingame_turn,ingame_players)
                    elif choice.lower()=='s':
                        #save game
                        filename=raw_input("Enter the name of the save file: ")
                        open(filename,'w')
                        save=open(filename,'w')
                        save.write(ingame_players[0]+'\n')
                        save.write(ingame_players[1]+'\n')
                        save.write(str(player0_wins)+'\n')
                        save.write(str(player1_wins)+'\n')
                        save.write(str(draws)+'\n')
                        save.write(str(ingame_board)+'\n')
                        save.write(ingame_turn+'\n')
                        save.close()
                    elif choice.lower()=='r':
                        #resign game
                        for i in range(0,4):
                            ingame_board[0][i]=ingame_turn
                        active_turn=False
                    elif choice.lower()=='q':
                        #quit game
                        quit=True
                        active_turn=False
                        return
                    else:
                        print "ERROR: Invalid command\n"+\
                              "    Enter 'p' to print the board\n"+\
                              "    Enter 'h' to see square numbers and current turn\n"+\
                              "    Enter a number between 0 and 15 to play a piece in the square of the number you entered\n"+\
                              "    Enter 's' to save the game\n"+\
                              "    Enter 'r' to resign\n"+\
                              "    enter 'q' to quit without saving\n"
            #check for draw
            counter=0
            for i in range(0,4):
                for j in range(0,4):
                    if ingame_board[i][j]=='#':
                        counter+=1
            if counter==0:
                break

            #change turns
            if ingame_turn=='x':
                ingame_turn='o'
            elif ingame_turn=='o':
                ingame_turn='x'
                
        #playerX congrats
        if who_won(ingame_board)=='x':
            print "Game over,",playerX,"has won the game."
            if playerX==ingame_players[0]:
                player0_wins+=1
            else:
                player1_wins+=1

        #playerO congrats
        elif who_won(ingame_board)=='o':
            print "Game over,",playerO,"has won the game."
            if playerO==ingame_players[0]:
                player0_wins+=1
            else:
                player1_wins+=1
        else:
            print "Game over, draw."
            draws+=1
        ingame_turn='x'
        ingame_board=[['#' for col in range(4)] for row in range(4)]

#GAME STARTER
play()
