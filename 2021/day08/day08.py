import itertools

def solve_p1():
    with open('p1.in', 'r') as f:
        ans = 0
        for line in f:
            _, output = [part.split() for part in line.strip().split(' | ')]
            for value in output:
                if len(value) in (2, 4, 3, 7):
                    ans += 1
        print(ans)


def solve_p2():
    SIGNALS = 'abcdefg'
    DIGIT_SIGNALS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    with open('p2.in', 'r') as f:
        ans = 0
        for line in f:
            patterns, output = [part.split() for part in line.strip().split(' | ')]
            for mapped in itertools.permutations(SIGNALS):
                table = str.maketrans(SIGNALS, ''.join(mapped))
                if {''.join(sorted(p.translate(table))) for p in patterns} == set(DIGIT_SIGNALS):
                    value = 0
                    for value_digit in output:
                        value = 10 * value + DIGIT_SIGNALS.index(''.join(sorted(value_digit.translate(table))))
                    ans += value
                    break
        print(ans)


if __name__ == '__main__':
    solve_p1()
    solve_p2()
