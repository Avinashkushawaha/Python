def solve(board):
    if not board: return
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'E'
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r+dr, c+dc)
    
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)
    for j in range(cols):
        dfs(0, j)
        dfs(rows-1, j)
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'E':
                board[r][c] = 'O'
