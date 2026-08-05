class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l =0;
        let h = nums.length
        while(l<=h){
            let m= Math.floor((l+h)/2)

            if(nums[m]== target) return m;
            if(nums[m]>target) h=m-1
            else l = m+1
        }
        return -1;
    }
}
