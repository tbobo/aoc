import collections

def solve_p1():
    with open('p1.in', 'r') as f:
        polymer = f.readline().strip()
        f.readline()
        rules = {}
        while line := f.readline().strip():
            pair, c = line.split(' -> ')
            rules[pair] = c

        def step(polymer):
            npolymer = []
            for i, c in enumerate(polymer):
                if i > 0 and (pair := polymer[i - 1] + c) in rules:
                    npolymer.append(rules[pair])
                npolymer.append(c)
            return ''.join(npolymer)

        for _ in range(10):
            polymer = step(polymer)
        cnts = collections.Counter(polymer)
        print(max(cnts.values()) - min(cnts.values()))


def solve_p2():
    with open('p2.in', 'r') as f:
        polymer = f.readline().strip()
        f.readline()
        rules = {}
        while line := f.readline().strip():
            pair, c = line.split(' -> ')
            rules[pair] = c
        polymer = '^' + polymer + '$'

        pair_cnts = collections.Counter(a + b for a, b in zip(polymer, polymer[1:]))
        def step(pair_cnts):
            ncnts = collections.Counter()
            for (a, b), cnt in pair_cnts.items():
                if a + b in rules:
                    c = rules[a + b]
                    ncnts[a + c] += cnt
                    ncnts[c + b] += cnt
                else:
                    ncnts[a + b] = cnt
            return ncnts

        for _ in range(40):
            pair_cnts = step(pair_cnts)
        element_cnts = collections.Counter()
        for (a, b), cnt in pair_cnts.items():
            element_cnts[a] += cnt
            element_cnts[b] += cnt
        sorted_cnts = [v // 2 for _, v in element_cnts.most_common() if v > 1]
        print(sorted_cnts[0] - sorted_cnts[-1])


if __name__ == '__main__':
    solve_p1()
    solve_p2()
