class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {

        let l=0
        let h = nums.length-1;
        while(l<h){
            let mid = Math.floor((l+h)/2)
            if (nums[mid]>nums[h]) {
                l =mid+1
            }else{
                h=mid
            }
        }
        let lowest =l;
        l=0;
        h = nums.length-1;

        if (
            target >= nums[lowest] &&
            target <= nums[nums.length - 1]
        ) {
            l = lowest;
            h = nums.length - 1;
        } else {
            l = 0;
            h = lowest - 1;
        }
        while(l<=h){
            let mid= Math.floor((l+h)/2)
            if(nums[mid] == target)return mid
            if(nums[mid]>target){
                h=mid-1
            }else{
                l=mid+1
            }
        }
        return -1

    }
}
