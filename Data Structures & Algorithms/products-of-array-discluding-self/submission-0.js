class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length
        let output = new Array(n)

        let leftProd = 1;

        for (let i=0;i<n;i++){
            output[i] = leftProd;
            leftProd *= nums[i];
        }

        let rightProd =1;
        for (let i=n-1;i>=0;i--){
            output[i] *= rightProd
            rightProd *= nums[i];
        }

        return output;
    }
}
