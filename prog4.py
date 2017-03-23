#*******************************************************************
#
#  Program:     Project 4
#
#  Author:      Trent Thompson
#  Email:       tt948912@ohio.edu
#
#  Description: Tic-tac-toe with variable board sizes
#
#  Date:        March 21th, 2017
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

'''create_board(n) will generate a square board with 'n' number of rows and columns.'''
def create_board(n):
    return [['#' for i in range(n)] for i in range(n))]

'''who_won(board) will return either 'x' or 'o' if either has a winning position, otherwise it will return '#'.'''
def who_won(board):
    num=len(board)
    for i in range(0,num):
        for j in range(0,num):
            #check for verticle win
            try:
                if board[i][j]!=board[i][j+1]:
                    break
            except:
                return board[i][j]
            #check for horizontal win
            try:
                if board[j][i]!=board[j+1][i]:
                    break
            except:
                return board[j][i]
            #check for left-to-right diagonal win
            try:
                if board[i][i]!=board[i+1][i+1]:
                    break
            except:
                return board[i][i]
            #check for left-to-right diagonal win
            try:
                if board[num-i][i]!=board[num-i+1][i+1]:
                    break
            except:
                return board[i][i]
    return '#'

'''move(board, sq, marker) will alter the board 'board' at square 'sq' to marker 'marker'.'''
def move(board,sq,marker):
    num=len(board)
    board[sq/num][sq%num]=marker

'''print_help(turn,players) will print a diagram of which numbers \
corespond to which squares as well as who's turn it is.'''
def print_help(turn,players,board):
    num=len(board)
    #print first line
    line="\n"+"------"*num
    #rows for loop
    for i in range(0,num):
        #columns for loop
        for j in range(0,num):
            #print the square number
            sq=i*num+j%num
            if sq<10:
                print "  "+str(sq),
            else:
                print " "+str(sq),
            if sq%num!=num-1: print '|',
        if i<num-1: print line
    #print who's turn it is
    if turn=='x':
        player=players[0]
    else:
        player=players[1]
    print"\nIt is "+player+"'s turn.\n"

'''play() will start and maintain a game of tic-tac-toe'''
def play():
    #game set up
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
        #get player names
        ingame_players[0]=raw_input("Name of first player: ")
        ingame_players[1]=raw_input("Name of second player: ")
        playerX=random.choice(ingame_players)
        if playerX==ingame_players[0]:
            playerO=ingame_players[1]
        else:
            playerO=ingame_players[0]
        ingame_turn='x'


    #main game loop
    quit=False
    while not quit:
        #get number of rows and columns
        choosing=True
        #while loop for getting board size
        while(choosing):
            tmp_num=raw_input("Number of rows and columns: ")
            try:
                if int(tmp_num)>=3 and int(tmp_num)<=100:
                    num=tmp_num
                    choosing=False
                else:
                    print "ERROR: Enter a number between 3 and 100"
            except:
                print "ERROR: Enter an integer"
        ingame_board=create_board(num)
        #while loop for game duration
        while who_won(ingame_board)=='#':
            active_turn=True
            #while loop for turn duration
            while active_turn:
                num=len(ingame_board)
                choice=raw_input()
                try:
                    choice=int(choice)
                    #make a move
                    if choice>=0 and choice<num*num:
                        if ingame_board[choice/num][choice%num]=="#":
                            move(ingame_board,choice,ingame_turn)
                            active_turn=False
                        else:
                            print "ERROR: Space taken"
                    else:
                        print "ERROR: Enter a number between 0 and 15"
                except:
                    if choice.lower()=='p':
                        #print baord
                        print_board(ingame_board)
                    elif choice.lower()=='h':
                        #run help
                        print_help(ingame_turn,ingame_players,ingame_board)
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
                        for i in range(0,num):
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
            for i in range(0,num):
                for j in range(0,num):
                    if ingame_board[i][j]=='#':
                        counter+=1
            if counter==0:
                break

            #change turns
            if ingame_turn=='x':
                ingame_turn='o'
            else:
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

#GAME STARTER
play()
