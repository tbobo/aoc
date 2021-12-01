def solve_p1():
    with open('p1.in', 'r') as f:
        ans = 0
        measurements = [int(line) for line in f]
        for i, x in enumerate(measurements):
            if i > 0 and x > measurements[i - 1]:
                ans += 1
        print(ans)


def solve_p2():
    with open('p1.in', 'r') as f:
        ans = 0
        measurements = [int(line) for line in f]
        for i, x in enumerate(measurements):
            if i >= 3 and x > measurements[i - 3]:
                ans += 1
        print(ans)


if __name__ == '__main__':
    solve_p1()
    solve_p2()
