# THE CLASSIC N-QUEENS PROBLEM
# Author : ASHIN BASIL JOHN
#
# Date: 08/18/18
#
# 00 01 02 #
# 10 11 12 #
# 20 21 22 #

board=[]
bs=25

#Make Board
for i in range(0,bs):
    board.append([])
    for j in range (0,bs):
        board[i].append(0)

def showboard():
    global board
    for i in range(0,bs):
            print( board[i])
showboard()

def issafe(row,column):
    global board
    #Row Check
    for i in range (0,bs):
        board[row][i]=1
    #Column Check
    for j in range (0,bs):
        #print(j,column)
        board[j][column]=1
    #Diagonal
    for i in range(0,bs):
        #print('row',row-i,column-i)
        
        if row-i >=0 and column-i >=0: 
            board[row-i][column-i]=1

        if row+i <bs and column+i <bs: 
            board[row+i][column+i]=1
    #Off Diagonal
    for i in range(0,bs):
        #print('row',row-i,column+i)
        
        if row-i >=0 and column+i <bs: 
            board[row-i][column+i]=1

        if row+i <bs and column-i >=0: 
            board[row+i][column-i]=1
        
issafe(10,10)
showboard()
