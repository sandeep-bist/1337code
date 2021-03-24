const map = new Map([
  [3, 'Fizz'],
  [5, 'Buzz'],
])

const fizzBuzz = (end = 20) => {
  const start = 1
  const res = []
  for (let i = start; i <= end; i++) {
    let tmp = ''
    map.forEach((val, key) => {
      if (i > 0 && i % key === 0) {
        tmp += val
      }
    })
    tmp = tmp || i
    res.push(tmp.toString())
  }
  return res
}
