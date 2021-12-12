def solve_p1():
    with open('p1.in', 'r') as f:
        grid = [[int(x) for x in line.strip()] for line in f]

        def dfs(i, j):
            if grid[i][j] > 9:
                flashes = 1
                grid[i][j] = 0
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] > 0:
                            grid[ni][nj] += 1
                            flashes += dfs(ni, nj)
                return flashes
            return 0

        def step():
            flashes = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid[i][j] += 1

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] > 0:
                        flashes += dfs(i, j)
            return flashes
        
        flashes = 0
        for _ in range(100):
            flashes += step()
        print(flashes)


def solve_p2():
    with open('p2.in', 'r') as f:
        grid = [[int(x) for x in line.strip()] for line in f]

        def dfs(i, j):
            if grid[i][j] > 9:
                flashes = 1
                grid[i][j] = 0
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] > 0:
                            grid[ni][nj] += 1
                            flashes += dfs(ni, nj)
                return flashes
            return 0

        def step():
            flashes = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid[i][j] += 1

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] > 0:
                        flashes += dfs(i, j)
            return flashes
        
        step_no = 0
        while True:
            step_no += 1
            if step() == len(grid) * len(grid[0]):
                break
        print(step_no)


if __name__ == '__main__':
    solve_p1()
    solve_p2()
