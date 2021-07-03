def reverse(x)
    sign = x > 0 ? 1 : -1
    x = x.abs
    res = 0
    until x.zero?
        remainder = x.remainder(10)
        x /= 10
        res = (res * 10) + remainder
    end
    return 0 if res < int_min || res > int_max
    res * sign
end

def int_max
    2**31 - 1
end

def int_min
    -(2**31)
end