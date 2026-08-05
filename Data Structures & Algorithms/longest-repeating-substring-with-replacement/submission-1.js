class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let cnt = new Map();
        let res=0;
        let l=0;
        for(let r=0; r<s.length;r++){
            cnt.set(s[r], (cnt.get(s[r])||0) +1)
            while((r-l+1 - Math.max(...cnt.values()))>k){
                cnt.set(s[l], cnt.get(s[l]) - 1)
                l++
            }
            res = Math.max(r-l+1, res)
        }
        return res
    }
}
