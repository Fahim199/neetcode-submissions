class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, o, c):
            if n * 2 == len(s):
                if o==c:
                    res.append(s)
                return
            dfs(s + '(', o+1, c)
            if(c<o):
                dfs(s + ')', o, c+1)

        dfs("",0,0)
        return res