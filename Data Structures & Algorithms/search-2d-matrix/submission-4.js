class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let rSize = matrix[0].length-1;
        let cSize = matrix.length-1;
        let l=0;
        let reqA=[]

        while(l<=cSize){
            let mid = Math.floor((l+cSize)/2)
            if(target>= matrix[mid][0] && target<= matrix[mid][rSize] ){
                reqA = matrix[mid]
                break
            }

            if(target>matrix[mid][rSize]){
                l= mid+1
            }else{
                cSize=mid-1
            }
            
        }
        
        l=0

        while(l<=rSize && reqA.length>0){
            let mid = Math.floor((l+rSize)/2)
            if(reqA[mid] == target) return true;
            if(reqA[mid]>target) rSize=mid-1
            else l= mid+1
        }
        return false
        

    }
}
