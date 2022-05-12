strs = ["dog","racecar","car"]

function longestCommonPrefix(strs) {
    let prefix = ""
    let minStr = strs[0].length
    for(let i = 0; i < strs.length; i++) {
        if(strs[i].length < minStr) {
            minStr = strs[i].length
        }
    }
    for(let i = 0; i < minStr; i++) {
        const check = strs[0][i]
        let same = true
        for(let j = 1; j < strs.length; j++) {
            if(strs[j][i] != check) {
                same = false
            }
        }
        if(same == true) {
            prefix += check
        }
        else if(same == false) {
            return prefix
        }
    }
    return prefix
}
console.log(longestCommonPrefix(strs))