import collections

def solve_p1():
    with open('p1.in', 'r') as f:
        adj = collections.defaultdict(list)
        for line in f:
            u, v = line.strip().split('-')
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(u):
            if u == "end":
                return 1
            if u.islower():
                visited.add(u)
            ways = 0
            for v in adj[u]:
                if v not in visited:
                    ways += dfs(v)
            if u.islower():
                visited.remove(u)
            return ways

        print(dfs("start"))


def solve_p2():
    with open('p2.in', 'r') as f:
        adj = collections.defaultdict(list)
        for line in f:
            u, v = line.strip().split('-')
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        small_twice = None
        def dfs(u):
            nonlocal small_twice
            if u == "end":
                return 1
            if u.islower():
                if u not in visited:
                    visited.add(u)
                else:
                    small_twice = u
            ways = 0
            for v in adj[u]:
                if v not in visited or (small_twice is None and v != "start"):
                    ways += dfs(v)
            if u.islower():
                if small_twice != u:
                    visited.remove(u)
                else:
                    small_twice = None
            return ways

        print(dfs("start"))


if __name__ == '__main__':
    solve_p1()
    solve_p2()
