class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nMap = {"2":"abc", "3":"def","4": "ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        letters=[]
        res = []
        def dfs(i, part):
            if len(part) == len(digits):
                res.append(part)
                return

            for c in nMap[digits[i]]:
                dfs(i+1, part + c)
        
        
        if digits:
            dfs(0, '')

        return res


        