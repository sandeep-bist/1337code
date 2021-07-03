def is_valid(s)
    map = { ')' => '(', '}' => '{', ']' => '[' }
    stack = []
    s.each_char do |c|
        if map.key?(c)
            return false if stack.empty? || stack.pop != map[c]
        else
            stack << c
        end
    end
    stack.empty?
end