class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(strs.length===0){
            return "nai"
        }
        if(strs.length===1){
            return strs[0]
        }
        return strs.join("FAHIM")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str==="nai"){
            return []
        }
        if(str.length===0){
            return [""]
        }
        if(str.length===1){
            return [str]
        }
        return str.split("FAHIM")
    }
}
