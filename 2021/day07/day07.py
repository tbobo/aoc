import math

def solve_p1():
    with open('p1.in', 'r') as f:
        a = [int(x) for x in f.readline().strip().split(',')]
        a.sort()
        ans = 0
        for x in a:
            ans += abs(x - a[len(a) // 2])
        print(ans)


def solve_p2():
    with open('p2.in', 'r') as f:
        a = [int(x) for x in f.readline().strip().split(',')]
        lower = int(math.floor(sum(a) / len(a)))
        upper = int(math.ceil(sum(a) / len(a)))
        ans_lower = 0
        ans_upper = 0
        for x in a:
            d_lower = abs(x - lower)
            d_upper = abs(x - upper)
            ans_lower += d_lower * (d_lower + 1) // 2
            ans_upper += d_upper * (d_upper + 1) // 2
        print(min(ans_lower, ans_upper))


if __name__ == '__main__':
    solve_p1()
    solve_p2()

