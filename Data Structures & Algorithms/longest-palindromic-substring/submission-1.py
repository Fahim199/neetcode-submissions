class Solution:
    def longestPalindrome(self, s: str) -> str:
        lSub = ""
        mLen = 0


        for i in range(len(s)):
            l, r = i,i
            
            #odd
            while l>=0 and r<= len(s)-1 and s[l] == s[r]:
                if (r-l +1) > mLen:
                    lSub = s[l:r +1]
                    mLen = r-l +1
                
                l-=1
                r+=1
            
            l,r = i, i+1
            #even
            while l>=0 and r<= len(s)-1 and s[l] == s[r]:
                if (r-l +1) > mLen:
                    lSub = s[l: r+1]
                    mLen = r-l +1
                
                l-=1
                r+=1
        
        return lSub

            

        

        