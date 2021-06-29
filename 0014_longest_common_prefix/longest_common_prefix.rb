# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    first = strs[0]
    first.each_char.with_index do |c, i|
        strs[1..].each do |str|
            return first[0, i] if str.empty? || c != str[i]
        end
    end
    first
end