class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        def dfs(start, path):
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                res.append(path[:])
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])

        return res


        