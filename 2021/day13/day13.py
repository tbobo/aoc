def fold_left(points, xmid):
    npoints = set()
    for x, y in points:
        if x < xmid:
            npoints.add((x, y))
        elif x > xmid:
            npoints.add((xmid - (x - xmid), y))
        else:
            assert False
    return npoints


def fold_up(points, ymid):
    npoints = set()
    for x, y in points:
        if y < ymid:
            npoints.add((x, y))
        elif y > ymid:
            npoints.add((x, ymid - (y - ymid)))
        else:
            assert False
    return npoints


def fold(points, axis):
    dir, coord = axis.split('=')
    f = fold_left if dir == 'x' else fold_up
    return f(points, int(coord))


def print_points(points):
    x_max = max(x for x, _ in points)
    y_max = max(y for _, y in points)
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            c = '#' if (x, y) in points else '.'
            print(c, end='')
        print()


def solve_p1():
    with open('p1.in', 'r') as f:
        points = set()
        while line := f.readline().strip():
            x, y = [int(c) for c in line.split(',')]
            points.add((x, y))

        axis = f.readline().strip().split()[-1]
        points = fold(points, axis)
        print(len(points))


def solve_p2():
    with open('p2.in', 'r') as f:
        points = set()
        while line := f.readline().strip():
            x, y = [int(c) for c in line.split(',')]
            points.add((x, y))

        while line := f.readline().strip():
            axis = line.split()[-1]
            points = fold(points, axis)
        print_points(points)


if __name__ == '__main__':
    solve_p1()
    solve_p2()
