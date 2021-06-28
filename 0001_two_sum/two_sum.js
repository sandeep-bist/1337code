/**
 * Time:    O(n)
 * Space:   O(n)
 * @param   {number[]}  nums
 * @param   {number}    target
 * @return  {number[]}
 */
const twoSum = (nums, target) => {
    const map = {}
    for (let i in nums) {
        const curr = nums[i]
        const compliment = target - curr
        if (map[compliment] !== undefined) {
            return [map[compliment], i]
        }
        map[curr] = i
    }
    return []
}
