# THE CLASSIC N-QUEENS PROBLEM
# Author : ASHIN BASIL JOHN
#
# Date: 08/18/18
#
# 00 01 02 #
# 10 11 12 #
# 20 21 22 #

board=[]
bs=5   #boardsize

#Make Board
for i in range(0,bs):
    board.append([])
    for j in range (0,bs):
        board[i].append(0)

def showboard():
    global board
    for i in range(0,bs):
            print( board[i])
#showboard()

# This function check if the given position is safe by checking
# row-wise, colums-wise, diagonal-wise, off-diagonal wise
# open paths will be marked by 0.

def issafe(row,column):
    global board
    #Row Check
    for i in range (0,bs):
        #board[row][i]=1
        if board[row][i] != 0:
            return False
    #Column Check
    for j in range (0,bs):
        #print(j,column)
        #board[j][column]=1
        if board[j][column]!=0:
            return False
    #Diagonal
    for i in range(0,bs):
        #print('row',row-i,column-i)
        
        if row-i >=0 and column-i >=0: 
            #board[row-i][column-i]=1
            if board[row-i][column-i] != 0:
                return False
        if row+i <bs and column+i <bs:
            #board[row+i][column+i]=1
            if board[row+i][column+i] !=0:
                return False
    #Off Diagonal
    for i in range(0,bs):
        #print('row',row-i,column+i)
        
        if row-i >=0 and column+i <bs: 
            #board[row-i][column+i]=1
            if board[row-i][column+i] !=0:
                return False
        if row+i <bs and column-i >=0: 
            #board[row+i][column-i]=1
            if board[row+i][column-i] !=0:
                return False

    return True
#issafe(10,10)
#showboard()
def putqueen(queen,row,column):
    global board
    if row>bs or column> bs:
        return False
    else:
        if issafe(row,column):
            board[row][column]=queen;
            return True
        else:
            board[row][column]=0;
            putqueen(queen,row,column+1)

#number of queens will be board size -1 
for queen in range(1,bs+1):
    putqueen(queen,queen-1,0)

showboard()
