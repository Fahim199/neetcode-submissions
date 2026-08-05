class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let miniB=prices[0];
        let maxP=0;
        for(let i=1;i<prices.length;i++){
            maxP=Math.max(maxP, prices[i]-miniB)
            miniB= Math.min(miniB, prices[i])
            
        }
        return maxP;
    }
}
