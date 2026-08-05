class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let a  = new Map();
        for(let i= 0; i< nums.length; i++){
            let cnt = a.get(nums[i]) ?? 0;
            a.set(nums[i],cnt+1)
        }
        let sortedMap = new Map([...a].sort((a,b) => b[1]-a[1]))
        let result = [];
        
        for(const [key,value] of sortedMap){
            if(k>0){
                result.push(key)
            }
            k--;
        }
        return result
    }
}
