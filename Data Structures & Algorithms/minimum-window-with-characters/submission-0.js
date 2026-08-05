class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if(t.length>s.length){
            return ''
        }
        let trackT= new Map();
        let trackS = new Map();
        for(let i=0;i< t.length;i++){
            trackT.set(t[i], (trackT.get(t[i]) || 0)+1)
        }
        let l=0;
        let maxL= Infinity;
        let uniqueCond = trackT.size
        let satisfiedCond = 0;
        let res =[]

        for(let r=0; r<s.length; r++){
            trackS.set(s[r], (trackS.get(s[r])||0) +1)
            if(trackT.has(s[r]) && trackT.get(s[r]) == trackS.get(s[r])){
                satisfiedCond++;
            }

            while(uniqueCond == satisfiedCond){
                let windowSize = r-l+1
                if(windowSize<maxL){
                    res = [l,r];
                    maxL = windowSize;
                }
                if(trackT.has(s[l])){
                    trackS.set(s[l], trackS.get(s[l]) -1)
                    if(trackT.get(s[l]) > trackS.get(s[l])) satisfiedCond--;
                }
                l++;

            }

        }

        return maxL==Infinity ? "" : s.substring(res[0],res[1]+1)

    }



}
