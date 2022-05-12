const s = 'MCMXCIV' 
const roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

function romanToInt(s) {
    const roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    const integer = [1, 5, 10, 50, 100, 500, 1000]
    const size = s.length

    let val = 0
    for(let i = 0; i < size; i++) {
        if(i != size) {
            if(roman.indexOf(s[i + 1]) > roman.indexOf(s[i])) {
                val += integer[roman.indexOf(s[i + 1])] - integer[roman.indexOf(s[i])]
                i++
            }
            else { 
                val += integer[roman.indexOf(s[i])]
            }
        }   
    }
    return val 
}

console.log(romanToInt(s))

/*
MCMXCIV

M -> cek satu indeks sebelah kanan, C, M > C, val + M next
C -> cek satu indeks sebelah kanan, M, C < M, val + M-C
...

*/