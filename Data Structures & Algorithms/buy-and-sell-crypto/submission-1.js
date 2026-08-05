class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l=0;
        let maxP=0;
        for(let r=1;r< prices.length;r++){
            if(prices[l]<prices[r]){
                maxP = Math.max(maxP, prices[r]-prices[l])
            }else{
                l=r
            }
        }
        return maxP;
    }
}
