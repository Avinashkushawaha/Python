def solveSudoku(board):
    rows, cols, boxes = [0]*9, [0]*9, [0]*9
    empties = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empties.append((i,j))
            else:
                mask = 1 << (int(board[i][j])-1)
                rows[i] |= mask
                cols[j] |= mask
                boxes[(i//3)*3 + j//3] |= mask
    
    def backtrack(k):
        if k == len(empties):
            return True
        i, j = empties[k]
        box = (i//3)*3 + j//3
        used = rows[i] | cols[j] | boxes[box]
        for d in range(9):
            if not (used >> d) & 1:
                mask = 1 << d
                rows[i] |= mask; cols[j] |= mask; boxes[box] |= mask
                board[i][j] = str(d+1)
                if backtrack(k+1): return True
                board[i][j] = '.'
                rows[i] ^= mask; cols[j] ^= mask; boxes[box] ^= mask
        return False
    
    backtrack(0)
    return board

sudoku = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
print(solveSudoku(sudoku))
