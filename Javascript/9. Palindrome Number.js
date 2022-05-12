const x = -10 
let xString = x.toString()

let isPalindrome = true
let size = xString.length
for(let i = 0; i < (size / 2); i++) {
    if(xString[i] != xString[size-i-1]) {
        isPalindrome = false
    }
}
console.log(isPalindrome)