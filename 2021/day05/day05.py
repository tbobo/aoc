import collections

def solve_p1():
    with open('p1.in', 'r') as f:
        coord_cnts = collections.Counter()
        for line in f:
            (x1, y1), (x2, y2) = [[int(c) for c in coord.split(',')] for coord in line.strip().split(' -> ')]
            if x1 == x2:
                if y2 < y1:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    coord_cnts[(x1, y)] += 1
            elif y1 == y2:
                if x2 < x1:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    coord_cnts[(x, y1)] += 1

        intersection_cnt = 0
        for cnt in coord_cnts.values():
            if cnt > 1:
                intersection_cnt += 1
        print(intersection_cnt)


def solve_p2():
    with open('p2.in', 'r') as f:
        coord_cnts = collections.Counter()
        for line in f:
            (x1, y1), (x2, y2) = [[int(c) for c in coord.split(',')] for coord in line.strip().split(' -> ')]
            if x1 == x2:
                if y2 < y1:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    coord_cnts[(x1, y)] += 1
            elif y1 == y2:
                if x2 < x1:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    coord_cnts[(x, y1)] += 1
            else:
                x_dist = x2 - x1
                y_dist = y2 - y1
                x_norm = abs(x_dist)
                y_norm = abs(y_dist)
                assert x_norm == y_norm
                x_dir = (x_dist) // x_norm
                y_dir = (y_dist) // y_norm
                for i in range(x_norm + 1):
                    coord_cnts[(x1 + i * x_dir, y1 + i * y_dir)] += 1

        intersection_cnt = 0
        for cnt in coord_cnts.values():
            if cnt > 1:
                intersection_cnt += 1
        print(intersection_cnt)


if __name__ == '__main__':
    solve_p1()
    solve_p2()

