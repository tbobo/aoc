def solve_p1():
    MATCH = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    };
    POINTS = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    };

    with open('p1.in', 'r') as f:
        score = 0
        for line in f:
            stack = []
            for c in line.strip():
                if c not in MATCH:
                    stack.append(c)
                else:
                    if stack:
                        if stack[-1] != MATCH[c]:
                            # Corrupt
                            score += POINTS[c]
                            break
                        else:
                            stack.pop()
                    else:
                        # Incomplete
                        break
        print(score)


def solve_p2():
    MATCH = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    };
    RMATCH = {v: k for k, v in MATCH.items()}
    POINTS = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    };

    with open('p2.in', 'r') as f:
        scores = []
        for line in f:
            score = 0
            stack = []
            for c in line.strip():
                if c not in MATCH:
                    stack.append(c)
                else:
                    if stack:
                        if stack[-1] != MATCH[c]:
                            # Corrupt
                            break
                        else:
                            stack.pop()
                    else:
                        # Closed without opening -- shouldn't happen
                        assert False
            for c in reversed(stack):
                score = 5 * score + POINTS[RMATCH[c]]
            scores.append(score)
        scores.sort()
        print(scores[len(scores) // 2])


if __name__ == '__main__':
    solve_p1()
    solve_p2()
