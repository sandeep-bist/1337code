/**
 * Given a paragraph and a list of banned words, return the most frequent
 * word that is not in the list of banned words.  It is guaranteed there
 * is at least one word that isn't banned, and that the answer is unique.
 * Words in the list of banned words are given in lowercase, and free of
 * punctuation.  Words in the paragraph are not case sensitive. The
 * answer is in lowercase.
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
const mostCommonWord = (paragraph, banned) => {
  const s = new Set(banned)
  const h = {}
  const p = paragraph.replace(/[^A-Za-z]/g, " ").split(" ")
  for (let w of p) {
    var temp = w.toLowerCase()
    if (!s.has(temp) && temp.length) {
      if (temp in h) h[temp]++
      else h[temp] = 1
    }
  }
  let maxCount = 0
  let maxKey = ""
  for (let [key, value] of Object.entries(h)) {
    if (value > maxCount) {
      maxCount = value
      maxKey = key
    }
  }
  return maxKey
}

const paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
console.log(most_common_word(paragraph, ["hit"])) // "ball"
