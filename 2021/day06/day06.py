def solve_p1():
    with open('p1.in', 'r') as f:
        ages = [int(x) for x in f.readline().strip().split(',')]
        age_cnts = [0 for _ in range(9)]
        for a in ages:
            age_cnts[a] += 1
        for _ in range(80):
            age_cnts = age_cnts[1:7] + [age_cnts[0] + age_cnts[7], age_cnts[8], age_cnts[0]]
        print(sum(age_cnts))


def solve_p2():
    with open('p2.in', 'r') as f:
        ages = [int(x) for x in f.readline().strip().split(',')]
        age_cnts = [0 for _ in range(9)]
        for a in ages:
            age_cnts[a] += 1
        for _ in range(256):
            age_cnts = age_cnts[1:7] + [age_cnts[0] + age_cnts[7], age_cnts[8], age_cnts[0]]
        print(sum(age_cnts))


if __name__ == '__main__':
    solve_p1()
    solve_p2()

