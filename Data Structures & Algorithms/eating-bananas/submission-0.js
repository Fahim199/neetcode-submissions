class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let n = piles.length;
        let maxB= 1
        for(let i=0; i<n; i++){
            if(piles[i]>maxB) maxB = piles[i]
        }

        let l=0;
        while(l<= maxB){

            let mid = Math.floor((l+maxB)/2)
            let hrs =0;
            for(let i=0;i<n;i++){
                hrs += Math.ceil(piles[i]/mid)
            }
            if(hrs>h){
                l=mid+1
            }else{
                maxB =mid-1
            }
        }

        return l
    }
}
