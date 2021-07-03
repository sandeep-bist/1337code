def climb_stairs(n)
    return 1 if n == 1
    dp = Array.new(n, 0)
    dp[0] = 1
    dp[1] = 2
    2.upto(n - 1) { |i| dp[i] = dp[i - 1] + dp[i - 2] }
    dp.last
end