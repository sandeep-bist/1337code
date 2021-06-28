/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number} x
 * @return  {number}
 */
const reverse = x => {
  const INT_MAX = 2**31 - 1
  const INT_MIN = -(2**31)
  const sign = Math.sign(x)
  let res = 0
  x = Math.abs(x)
  while (x) {
      res = res * 10 + x % 10
      x = Math.floor(x / 10)
  }
  return res < INT_MAX && res > INT_MIN ? res * sign : 0
}
