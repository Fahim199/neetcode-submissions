class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let b =new Set(nums);
        return b.size != nums.length
    }
}
