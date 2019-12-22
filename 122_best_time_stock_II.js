/**
 * Say you have an array for which the ith element is the price of a given
 * stock on day i.
 * Design an algorithm to find the maximum profit. You may complete as many
 * transactions as you like (i.e., buy one and sell one share of the stock
 * multiple times).
 * Note: You may not engage in multiple transactions at the same time (i.e.,
 * you must sell the stock before you buy again).
 * @param   {number[]} prices
 * @return  {number}
 */
const maxProfit = prices => {
  return prices.reduce((max, el, i) => {
    if (el > prices[i - 1]) max += el - prices[i - 1]
    return max
  }, 0)
}

const arr = [7, 1, 5, 3, 6, 4] // 7
console.log(maxProfit(arr))

const arr2 = [7, 6, 5, 4, 3, 2] // 0
console.log(maxProfit(arr2))

const arr3 = [1, 2, 3, 4, 5] // 4
console.log(maxProfit(arr3))
