class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let i = 0;
        let k = 1;
        while(i<nums.length -1){
            if(nums[i]+nums[k] === target){
                return [i,k]
            }
            if(k===nums.length -1){
                i++;
                k=i+1
            }else{
                k++
            }
        }

    }
}
