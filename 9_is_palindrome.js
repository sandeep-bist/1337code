/**
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 * Could you solve it without converting the integer to a string?
 * @param   {number}    x
 * @return  {boolean}
 */
const isPalindrome = x => {
  if (x < 0 || (x && x % 10 == 0)) return false
  let reversed = 0
  while (x > reversed) {
    reversed = reversed * 10 + (x % 10)
    x = Math.floor(x / 10)
  }
  return x === reversed || x === Math.floor(reversed / 10)
}

console.log(isPalindrome(121)) // true
console.log(isPalindrome(-121)) // false
console.log(isPalindrome(10)) // false
console.log(isPalindrome(12344321)) // true
