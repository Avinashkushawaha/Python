class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_words(board, words):
    root = TrieNode()
    for w in words:
        node = root
        for c in w:
            node = node.children.setdefault(c, TrieNode())
        node.word = w

    res, rows, cols = [], len(board), len(board[0])

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return
        node = node.children[char]
        if node.word:
            res.append(node.word)
            node.word = None
        board[r][c] = '#'
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, node)
        board[r][c] = char

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)
    return res

board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))  # ['oath', 'eat']
