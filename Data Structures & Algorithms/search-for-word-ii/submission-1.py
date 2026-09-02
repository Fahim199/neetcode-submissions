class Trie:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        result = []

        def insert(word):
            curr = root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = Trie()

                curr = curr.children[c]

            curr.word = word

        for word in words:
            insert(word)

        def dfs(i, j, curr):
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return

            if board[i][j] == "*":
                return

            c = board[i][j]

            if c not in curr.children:
                return

            curr = curr.children[c]

            if curr.word:
                result.append(curr.word)
                curr.word = None

            board[i][j] = "*"

            dfs(i + 1, j, curr)
            dfs(i - 1, j, curr)
            dfs(i, j + 1, curr)
            dfs(i, j - 1, curr)

            board[i][j] = c

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return result