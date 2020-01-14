class DSU {
  /**
   * Disjoint Set constructor.
   */
  constructor() {
    this.parents = {}
    this.count = 0
  }

  /**
   * Finds parent of element with path compression functionality.
   * @param     {number}    x
   * @returns   {number}
   */
  find(x) {
    if (this.parents[x] != x) this.parents[x] = this.find(this.parents[x])
    return this.parents[x]
  }

  /**
   * Combines parent of two elements if they do not match.
   * @param     {number}    x
   * @param     {number}    y
   */
  union(x, y) {
    let par_x = this.find(x)
    let par_y = this.find(y)
    if (par_x !== par_y) {
      this.count--
      this.parents[par_x] = par_y
    }
  }

  /**
   * Adds an element into DSU.
   * @param     {number}   x
   */
  add(x) {
    if (x in this.parents) return
    this.parents[x] = x
    this.count++
  }
}

/**
 * A 2d grid map of m rows and n columns is initially filled with water.
 * We may perform an addLand operation which turns the water at position
 * (row, col) into a land. Given a list of positions to operate, count the
 * number of islands after each addLand operation. An island is surrounded
 * by water and is formed by connecting adjacent lands horizontally or
 * vertically. You may assume all four edges of the grid are all surrounded
 * by water.
 * @param   {number}        m
 * @param   {number}        n
 * @param   {number[][]}    positions
 * @returns {number}
 */
const numIslands2 = (m, n, positions) => {
  const surroundings = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
  ]
  const dsu = new DSU()
  const res = []
  positions.forEach(p => {
    const key = p[0] * n + p[1]
    dsu.add(key)
    surroundings.forEach(s => {
      const col = p[0] + s[0]
      const row = p[1] + s[1]
      const tmp = col * n + row
      if (row >= 0 && row < m && col >= 0 && col < n && tmp in dsu.parents)
        dsu.union(key, tmp)
    })
    res.push(dsu.count)
  })
  return res
}

const arr = [
  [0, 0],
  [0, 1],
  [1, 2],
  [2, 1]
]
console.log(numIslands2(3, 3, arr)) // [1, 1, 2, 3]

const arr2 = [
  [0, 0],
  [0, 1],
  [1, 2],
  [1, 2]
]
console.log(numIslands2(3, 3, arr2)) // [1, 1, 2, 2]
