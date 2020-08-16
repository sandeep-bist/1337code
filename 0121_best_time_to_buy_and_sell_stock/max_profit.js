/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} prices
 * @return  {number}
 */
const maxProfit = prices => {
  let minPrice = Number.MAX_SAFE_INTEGER
  return prices.reduce((maxProfit, e) => {
    if (e < minPrice) minPrice = e
    else if (e - minPrice > maxProfit) maxProfit = e - minPrice
    return maxProfit
  }, 0)
}
