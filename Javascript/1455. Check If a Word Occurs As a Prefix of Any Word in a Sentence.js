/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
  const splitted = sentence.split(" ")
  const searchWordLength = searchWord.length
  let res = -1 

  for(let i = 0; i < splitted.length; i++ ) {
      console.log(splitted[i])
      if(splitted[i].slice(0, searchWordLength) === searchWord) {
          res = i + 1
          break
      }
  }
  return res 
};