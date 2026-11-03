class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        matches =[-1,-1,-1]
        for ele in triplets:
            if target[0] == ele[0] and target[1]>= ele[1] and target[2]>= ele[2]:
                matches[0]=0
            if target[0] >= ele[0] and target[1] == ele[1] and target[2]>= ele[2]:
                matches[1]=0
            if target[0] >= ele[0] and target[1]>= ele[1] and target[2]== ele[2]:
                matches[2]=0


        return True if matches[0]==matches[1]==matches[2]==0 else False

        