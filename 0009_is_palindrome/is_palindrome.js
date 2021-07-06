/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number}    x
 * @return  {boolean}
 */
const isPalindrome = (x) => {
    if (x < 0 || isFactorOfTen(x)) {
        return false
    }
    let reverse = 0
    while (x > reverse) {
        reverse = reverse * 10 + (x % 10)
        x = Math.floor(x / 10)
    }
    return x === reverse || x === Math.floor(reverse / 10)
}

const isFactorOfTen = (x) => x && x % 10 == 0
