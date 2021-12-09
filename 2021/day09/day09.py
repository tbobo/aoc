import functools
import heapq
import operator

def solve_p1():
    with open('p1.in', 'r') as f:
        heightmap = [[int(x) for x in line.strip()] for line in f]
        ans = 0
        for i, row in enumerate(heightmap):
            for j, x in enumerate(row):
                if (
                    (i == 0 or heightmap[i - 1][j] > x)
                    and (i + 1 == len(heightmap) or heightmap[i + 1][j] > x)
                    and (j == 0 or heightmap[i][j - 1] > x)
                    and (j + 1 == len(row) or heightmap[i][j + 1] > x)
                ):
                    ans += x + 1
        print(ans)


def solve_p2():
    with open('p2.in', 'r') as f:
        heightmap = [[int(x) for x in line.strip()] for line in f]
        seen = [[False for _ in row] for row in heightmap]

        def dfs(i, j):
            size = 1
            seen[i][j] = True
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (
                    0 <= ni < len(heightmap)
                    and 0 <= nj < len(heightmap[ni])
                    and heightmap[ni][nj] != 9
                    and not seen[ni][nj]
                ):
                    size += dfs(ni, nj)
            return size

        basin_sizes = []
        for i, row in enumerate(heightmap):
            for j, x in enumerate(row):
                if not seen[i][j] and x != 9:
                    basin_sizes.append(dfs(i, j))
        print(functools.reduce(operator.mul, heapq.nlargest(3, basin_sizes)))


if __name__ == '__main__':
    solve_p1()
    solve_p2()
