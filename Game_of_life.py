def game_of_life(board):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            live = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    nr, nc = r + i, c + j
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live += 1
            if board[r][c] == 1 and (live < 2 or live > 3):
                board[r][c] = -1
            if board[r][c] == 0 and live == 3:
                board[r][c] = 2
    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0
