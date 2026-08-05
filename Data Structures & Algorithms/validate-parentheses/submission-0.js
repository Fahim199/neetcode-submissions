class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let sMap = new Map();
        sMap.set("(",")")
        sMap.set("{","}")
        sMap.set("[","]")
        let opening = [...sMap.keys()]
        let closing = [...sMap.values()]
        let stacks = []
        for(let i=0;i<s.length;i++){
            if(opening.includes(s[i])){
                stacks.push(s[i])
            }else{
                if(sMap.get(stacks.pop()) != s[i]){
                    return false;
                }
            }
        }
        return stacks.length == 0;
    }
}
