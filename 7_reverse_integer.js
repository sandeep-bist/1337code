/**
 * Given a 32-bit signed integer, reverse digits of an integer.
 * @param {number} x
 * @return {number}
 */
const reverse = x => {
  const INT_MAX = 2 ** 31 - 1
  const INT_MIN = -(2 ** 31)
  let res = 0
  while (x) {
    res = res * 10 + (x % 10)
    /* Math.floor will round down for negative numbers, so safer to use
       Math.trunc. */
    x = Math.trunc(x / 10)
  }
  return res < INT_MAX && res > INT_MIN ? res : 0
}

console.log(reverse(123)) // 321
console.log(reverse(120)) // 21
console.log(reverse(-914)) // -419
