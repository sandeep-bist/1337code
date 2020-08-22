class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap = [[0] + start]
        dists = defaultdict(lambda: float('inf'))
        dists[tuple(start)] = 0
        while heap:
            distance, i, j = heapq.heappop(heap)
            if [i, j] == destination:
                return distance
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c, count = i, j, distance
                while len(maze) > r + x >= 0 and len(maze[0]) > c + y >= 0 and maze[r + x][c + y] == 0:
                    r, c, count = r + x, c + y, count + 1
                if count < dists[(r, c)]:
                    heapq.heappush(heap, (count, r, c))
                    dists[(r, c)] = count
        return -1
