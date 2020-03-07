/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} prices
 * @return  {number}
 */
const maxProfit = prices => {
  return prices.reduce((max, el, i) => {
    if (el > prices[i - 1]) max += el - prices[i - 1]
    return max
  }, 0)
}
