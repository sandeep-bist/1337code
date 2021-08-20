def add_binary(a, b)
    i = a.length - 1
    j = b.length - 1
    res = []
    c = 0
    while i >= 0 || j >= 0 || c > 0
        c += i < 0 ? 0 : a[i].to_i
        c += j < 0 ? 0 : b[j].to_i
        i -= 1
        j -= 1
        res << (c % 2).to_s
        c /= 2
    end
    res.reverse.join
end