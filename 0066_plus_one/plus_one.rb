def plus_one(digits)
    i = digits.length - 1
    while digits[i] == 9
        digits[i] = 0
        i -= 1
    end
    return [1] + digits if i.negative?
     digits.tap { |d| d[i] += 1 }
  end