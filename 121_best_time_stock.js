/**
 * Say you have an array for which the ith element is the price of a given
 * stock on day i. If you were only permitted to complete at most one
 * transaction (i.e., buy one and sell one share of the stock), design an
 * algorithm to find the maximum profit.
 * Note that you cannot sell a stock before you buy one.
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

const arr = [7, 1, 5, 3, 6, 4] // 5
console.log(maxProfit(arr))

const arr2 = [7, 5, 4, 3, 2, 1] // 0
console.log(maxProfit(arr2))

const arr3 = [2, 4, 1, 2] // 2
console.log(maxProfit(arr3))
