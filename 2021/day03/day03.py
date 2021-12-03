def solve_p1():
    with open('p1.in', 'r') as f:
        nums = [line.strip() for line in f]
        cnts = [0 for _ in nums[0]]
        for x in nums:
            for i, bit in enumerate(x):
                cnts[i] += int(bit)
        gamma = ''.join('1' if cnt * 2 >= len(nums) else '0' for cnt in cnts)
        epsilon = ''.join('0' if bit == '1' else '1' for bit in gamma)
        print(int(gamma, 2) * int(epsilon, 2))


def solve_p2():
    class Trie:
        class Node:
            def __init__(self):
                self.cnt = 0
                self.children = [None, None]

        def __init__(self):
            self.root = Trie.Node()

        def add(self, s):
            cur = self.root
            for c in s:
                cur.cnt += 1
                bit = int(c)
                if not cur.children[bit]:
                    cur.children[bit] = Trie.Node()
                cur = cur.children[bit]
            cur.cnt += 1

        def walk(self, f):
            cur = self.root
            bits = []
            while cur.children[0] or cur.children[1]:
                next_bit = f(cur)
                bits.append(str(next_bit))
                cur = cur.children[next_bit]
            return int(''.join(bits), 2)

    with open('p2.in', 'r') as f:
        nums = [line.strip() for line in f]
        trie = Trie()
        for x in nums:
            trie.add(x)

        def pick_common(node):
            if not node.children[0]:
                return 1
            if not node.children[1]:
                return 0
            if node.children[0].cnt > node.children[1].cnt:
                return 0
            else:
                return 1

        def pick_uncommon(node):
            if not node.children[0]:
                return 1
            if not node.children[1]:
                return 0
            if node.children[0].cnt <= node.children[1].cnt:
                return 0
            else:
                return 1

        oxy_rating = trie.walk(pick_common)
        co2_rating = trie.walk(pick_uncommon)
        print(oxy_rating * co2_rating)


if __name__ == '__main__':
    solve_p1()
    solve_p2()

