/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number} x
 * @return  {number}
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
