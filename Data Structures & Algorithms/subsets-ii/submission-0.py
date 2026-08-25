class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        def dfs(start, path):
            if start == len(nums):
                return
            
            
            path.append(nums[start])
            res.append(path[:])
            dfs(start+1, path)
            path.pop()
            while start+1< len(nums) and nums[start+1]==nums[start]:
                start+=1
            
            dfs(start+1, path)
        
        dfs(0, [])

        return res


        