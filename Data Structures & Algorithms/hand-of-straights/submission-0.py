class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n =len(hand)
        if n%groupSize != 0:
            return False

        tracker = {}
        for i in hand:
            tracker[i] = tracker.get(i,0) +1

        hand.sort()
        for i in range(n):
            if tracker[hand[i]]>0:
                for j in range(hand[i], hand[i]+groupSize):
                    if j not in tracker or tracker[j]  == 0:
                        return False
                    
                    tracker[j]= tracker[j] -1
                
        return True


        
        