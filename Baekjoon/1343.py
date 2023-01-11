#폴리오미노 

board = list(input())

flag = 0
index = 0
while index < len(board):
    if board[index] == "X":
        if (index + 1) < len(board) and board[index + 1] == "X":
            if (index + 3) < len(board) and board[index + 2] == "X" and board[index + 3] == "X":
                for i in range(4):
                    board[index + i] = "A"
                index += 4
            else:
                for i in range(2):
                    board[index + i] = "B"
                index += 2
        else:
            print(-1)
            flag = 1
            break
    elif board[index] == ".":
        index += 1

if flag == 0:
    for x in board:
        print(x, end = "")

