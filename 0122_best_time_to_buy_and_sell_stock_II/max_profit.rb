# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    # Time: O(n)
    # Space: O(1)
    res = 0
    return res if prices.length < 2
    prices.each_with_index do |p, i|
      res += (prices[i + 1] - p) if prices[i + 1] && prices[i + 1] > p
    end  
    res
end