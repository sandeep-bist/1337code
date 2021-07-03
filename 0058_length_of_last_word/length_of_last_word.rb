def length_of_last_word(s)
    res = 0
    i = s.length - 1
    until i.negative?
        if s[i] != ' '
            res += 1
        elsif res.positive?
            return res
        end
        i -= 1
    end
    res
end