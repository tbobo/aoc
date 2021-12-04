import collections

def solve_p1():
    with open('p1.in', 'r') as f:
        order = [int(x) for x in f.readline().strip().split(',')]
        boards = []
        locs = []
        row_cnt = []
        col_cnt = []
        while f.readline():
            board = []
            loc = collections.defaultdict(list)
            for r in range(5):
                row = [int(x) for x in f.readline().strip().split()]
                for c, x in enumerate(row):
                    loc[x].append((r, c))
                board.append(row)
            boards.append(board)
            locs.append(loc)
            row_cnt.append([0 for _ in range(5)])
            col_cnt.append([0 for _ in range(5)])

        for call in order:
            for i, board in enumerate(boards):
                for r, c in locs[i][call]:
                    board[r][c] = 0
                    row_cnt[i][r] += 1
                    col_cnt[i][c] += 1
                    if row_cnt[i][r] == 5 or col_cnt[i][c] == 5:
                        print(sum(x for row in board for x in row) * call)
                        return


def solve_p2():
    with open('p1.in', 'r') as f:
        order = [int(x) for x in f.readline().strip().split(',')]
        boards = []
        locs = []
        row_cnt = []
        col_cnt = []
        while f.readline():
            board = []
            loc = collections.defaultdict(list)
            for r in range(5):
                row = [int(x) for x in f.readline().strip().split()]
                for c, x in enumerate(row):
                    loc[x].append((r, c))
                board.append(row)
            boards.append(board)
            locs.append(loc)
            row_cnt.append([0 for _ in range(5)])
            col_cnt.append([0 for _ in range(5)])

        won_cnt = 0
        board_won = [False for _ in boards]
        for call in order:
            for i, board in enumerate(boards):
                for r, c in locs[i][call]:
                    board[r][c] = 0
                    row_cnt[i][r] += 1
                    col_cnt[i][c] += 1
                    if not board_won[i] and (row_cnt[i][r] == 5 or col_cnt[i][c] == 5):
                        board_won[i] = True
                        won_cnt += 1
                        if won_cnt == len(boards):
                            print(sum(x for row in board for x in row) * call)
                            return


if __name__ == '__main__':
    solve_p1()
    solve_p2()

