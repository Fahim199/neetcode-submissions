class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if(nums.length<2){
            return nums.length
        }
        nums.sort((a, b) => a - b)
        let maxi =1
        for (let i=1;i<nums.length;i++ ){
            
            let sum = 1 
            while(nums[i]- nums[i-1]<2){
                
                if(nums[i]>nums[i-1]){
                    sum++
                }
                i++

                maxi = Math.max(sum, maxi)
            }

        }
        return maxi;
    }
}
