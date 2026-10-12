class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minN, maxN = 1,1
        for n in nums:
            
            tmp = maxN
            maxN = max(minN*n, maxN*n, n)
            minN = min(minN*n, tmp*n, n)

            res = max(maxN, res)
        
        return res


        