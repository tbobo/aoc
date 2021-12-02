def solve_p1():
    with open('p1.in', 'r') as f:
        hpos = 0
        depth = 0
        for line in f:
            dir, delta = line.split()
            delta = int(delta)
            if dir == 'forward':
                hpos += delta
            elif dir == 'down':
                depth += delta
            elif dir == 'up':
                depth -= delta
        print(hpos * depth)


def solve_p2():
    with open('p2.in', 'r') as f:
        hpos = 0
        depth = 0
        aim = 0
        for line in f:
            dir, delta = line.split()
            delta = int(delta)
            if dir == 'forward':
                hpos += delta
                depth += aim * delta
            elif dir == 'down':
                aim += delta
            elif dir == 'up':
                aim -= delta
        print(hpos * depth)


if __name__ == '__main__':
    solve_p1()
    solve_p2()

