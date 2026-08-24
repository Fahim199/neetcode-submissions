class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, candidates):
            if not candidates:
                res.append(path[:])
                return

            for i in range(len(candidates)):
                copy = candidates.copy()
                path.append(candidates[i])
                copy.remove(candidates[i])
                dfs(path, copy)
                path.pop()
        
        dfs([], nums)
        return res

        