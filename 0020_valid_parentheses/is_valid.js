// Time:    O(n)
// Space:   O(n)
const isValid = (str) => {
    const map = {
        ']': '[',
        ')': '(',
        '}': '{',
    }
    const stack = []
    for (let c of str) {
        if (c in map) {
            if (stack.pop() != map[c]) {
                return false
            }
        } else stack.push(c)
    }
    return stack.length === 0
}
