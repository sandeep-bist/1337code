def min_remove_to_make_valid(s)
    # Time: O(n)
    # Space: O(n)
    stack = []
    str = s.split("")
    str.each_with_index do |char, index|
      if char == '('
          stack.push(index)
      elsif char == ')'
          if !stack.empty?
              stack.pop
          else
              str[index] = ""
          end
      end
    end
    until stack.empty?
        str[stack.pop] = ""
    end
    str.join("")
end