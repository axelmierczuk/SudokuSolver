SIZE = 9
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
    found = find_empty(board)
    if not found:
        return True
    else:
        row, col = found
    
    for a in range(1, SIZE + 1):
        if valid(board, a, (row, col)):
            board[row][col] = a

            if solve(board):
                return True

            board[row][col] = 0
    
    return False

def valid(board, val, position):
    for a in range(SIZE):
        if board[position[0]][a] == val and position[1] != a:
            return False
    for a in range(SIZE):
        if board[a][position[1]] == val and position[0] != a:
            return False                

    boxX = position[1] // 3
    boxY = position[0] // 3

    for a in range(boxY * 3, boxY * 3 + 3):
        for b in range(boxX * 3, boxX * 3 + 3):
            if board[a][b] == val and (a, b) != val:
                return False
    return True

def find_empty(board):
    for a in range(SIZE):
        for b in range(SIZE):
            if board[a][b] == 0:
                return (a, b)
    return None

def print_board(board):
    
    for a in range(SIZE):
        if a % int((SIZE / 3)) == 0 and a != 0:
            print("-----------------------")
        for b in range(SIZE):
            if b % int((SIZE / 3)) == 0 and b != 0:
                print(" | ", end="")
            if b == 8:
                print(board[a][b])
            else:
                print(str(board[a][b]) + " ", end="")
    print("\n\n")
    

print("Here is the unsolved board!")
print_board(board)
solve(board)
print("Here is the solved board!")
print_board(board)