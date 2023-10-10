global n
n=int(input("Enter:"))
def prinsolution(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print(".",end=" ") 
    print()
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
        for i,j in Zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        for i,j in Zip(range(row,n,1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
    return True
def check(board,col):
    if col>=n:
        return True
    for i in range(n):
        if issafe(board,i,col):
            board[i][col]=1
            if check(board,col,-1):
                return True
            boar[i][col]=0
    return False
def solveNQ():
    board=[]
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(0)
        board.append(k)
    if check(board,0) is False:
        print("Solution Not found")
        return False
    printsloution(board)
    return True
solveNQ()
