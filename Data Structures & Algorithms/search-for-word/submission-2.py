class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        width = len(board[0])

        def dfs(start, i, j):
            if start==len(word):
                return True
            if i<0 or i==length or j<0 or j==width or board[i][j] != word[start]:
                return False

            # mark as visited
            temp = board[i][j]
            board[i][j] = "#"

            found = (
                dfs(start + 1, i - 1, j) or
                dfs(start + 1, i + 1, j) or
                dfs(start + 1, i, j - 1) or
                dfs(start + 1, i, j + 1)
            )

            # restore
            board[i][j] = temp

            return found
        
        for i in range(length):
            for j in range(width):
                if board[i][j]==word[0]:
                    if dfs(0,i,j):
                        return True
        return False

        

