import collections

def solve_p1():
    with open('p1.in', 'r') as f:
        coord_cnts = collections.Counter()
        for line in f:
            start_coords, end_coords = line.strip().split(' -> ')
            x1, y1 = [int(c) for c in start_coords.split(',')]
            x2, y2 = [int(c) for c in end_coords.split(',')]
            x_dist = x2 - x1
            y_dist = y2 - y1
            x_dir = -1 if x_dist < 0 else 1 if x_dist > 0 else 0
            y_dir = -1 if y_dist < 0 else 1 if y_dist > 0 else 0
            if x1 == x2 or y1 == y2:
                x, y = x1, y1
                while x != x2 or y != y2:
                    coord_cnts[(x, y)] += 1
                    x += x_dir
                    y += y_dir
                coord_cnts[(x, y)] += 1

        intersection_cnt = 0
        for cnt in coord_cnts.values():
            if cnt > 1:
                intersection_cnt += 1
        print(intersection_cnt)


def solve_p2():
    with open('p2.in', 'r') as f:
        coord_cnts = collections.Counter()
        for line in f:
            start_coords, end_coords = line.strip().split(' -> ')
            x1, y1 = [int(c) for c in start_coords.split(',')]
            x2, y2 = [int(c) for c in end_coords.split(',')]
            x_dist = x2 - x1
            y_dist = y2 - y1
            x_dir = -1 if x_dist < 0 else 1 if x_dist > 0 else 0
            y_dir = -1 if y_dist < 0 else 1 if y_dist > 0 else 0
            x, y = x1, y1
            while x != x2 or y != y2:
                coord_cnts[(x, y)] += 1
                x += x_dir
                y += y_dir
            coord_cnts[(x, y)] += 1

        intersection_cnt = 0
        for cnt in coord_cnts.values():
            if cnt > 1:
                intersection_cnt += 1
        print(intersection_cnt)


if __name__ == '__main__':
    solve_p1()
    solve_p2()

