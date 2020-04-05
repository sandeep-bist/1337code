/**
 * Time: O(n)
 * Space: O(n)
 */
const countPrimes = (n) => {
  const primes = Array(n).fill(1)
  primes[0] = 0
  primes[1] = 0
  for (let i = 2; i < Math.sqrt(n); i++)
    if (primes[i]) for (let j = i * i; j < n; j += i) primes[j] = 0
  return primes.reduce((a, b) => a + b, 0)
}
