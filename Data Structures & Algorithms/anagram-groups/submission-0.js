class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let len = strs.length;
        let sortedArray = [];

        for (let i = 0; i < len; i++) {
            sortedArray.push(strs[i].split('').sort().join(''));
        }

        let indexTracker = new Map();

        for (let i = 0; i < len; i++) {
            if (indexTracker.has(sortedArray[i])) {
                indexTracker.get(sortedArray[i]).push(i);
            } else {
                indexTracker.set(sortedArray[i], [i]);
            }
        }

        let outputArr = [];

        for (const [key, value] of indexTracker) {
            let nArr = [];
            for (let idx of value) {
                nArr.push(strs[idx]);
            }
            outputArr.push(nArr);
        }

        return outputArr;
    }
}
