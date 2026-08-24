class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def generate_subsets(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            generate_subsets(i + 1, cur, total + candidates[i])
            cur.pop()
            x= candidates[i]
            while i+1<len(candidates) and candidates[i+1]==x:
                i+=1
            generate_subsets(i + 1, cur, total)

        generate_subsets(0, [], 0)
        return res