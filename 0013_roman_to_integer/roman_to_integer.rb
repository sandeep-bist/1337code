def roman_to_int(s)
    # Time: O(n)
    # Space: O(n)
    hash = {i: 1, v: 5, x: 10, l: 50, c: 100, d: 500, m: 1000}
    res, prev = 0, 0
    s.chars.reverse.each do |c|
        curr = hash[c.downcase.to_sym]
        res += prev > curr ? -curr : curr
        prev = curr
    end
    res
end