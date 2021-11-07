# @param {String} num1
# @param {String} num2
# @return {String}
def multiply(num1, num2)
    # Time: O(n * m)
    # Space: O(n + m)
    res = Array.new(num1.length + num2.length + 1, 0)
    num1 = num1.reverse
    num2 = num2.reverse
    for i in (0...num1.length)
        for j in (0...num2.length)
            res[i + j] += num1[i].to_i * num2[j].to_i
            res[i + j + 1] += res[i + j]/10
            res[i + j] %= 10
        end
    end
    res = res.reverse
    start = 0
    start += 1 while res[start] == 0 && start < res.length - 1
    res[start..-1].join()
end