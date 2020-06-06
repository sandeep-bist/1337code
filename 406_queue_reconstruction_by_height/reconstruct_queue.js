/**
 * Time: O(n**2)
 * Space: O(n)
 */
const reconstructQueue = (people) => {
  if (!people) return []
  people.sort((a, b) => (a[0] !== b[0] ? b[0] - a[0] : a[1] - b[1]))
  const queue = []
  people.map((person) => queue.splice(person[1], 0, person))
  return queue
}
