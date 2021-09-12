"""
TAGs: #leetcode, #hard, #leetcode_882
URL: https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

882. Reachable Nodes In Subdivided Graph
"""
import typing


def count_reachable_nodes(
        edges: typing.List[typing.List[int]], max_moves: int, n: int) -> int:
    graph, visited, moves = [{} for _ in range(n)], [-1] * n, [(0, max_moves)]

    for x, y, c in edges:
        graph[x][y], graph[y][x] = [0, c], [0, c]

    while moves:
        next_moves = []

        for pos, remain_moves in moves:
            if visited[pos] >= remain_moves:
                continue

            visited[pos] = remain_moves

            for next_pos, (m, c) in graph[pos].items():
                graph[pos][next_pos][0] = min(c, max(m, remain_moves))

                if remain_moves > c:
                    next_moves.append((next_pos, remain_moves - c - 1))

        moves = next_moves

    ans = sum(map(lambda v: v >= 0, visited))

    for x, y, c in edges:
        ans += min(graph[x][y][0] + graph[y][x][0], c)

    return ans


def test():
    # 0 .o.o.o.o.o.x.x.x.x.x. 1
    assert count_reachable_nodes([[0, 1, 10]], 0, 2) == 1

    # 0 .o.o.o.o.o.x.x.x.x.x. 1
    assert count_reachable_nodes([[0, 1, 10]], 5, 2) == 6

    # 0 .o.o.o.x.x.x.x.x.x.o. 1
    # .                       .
    # ...........2.............
    assert count_reachable_nodes([[0, 1, 10], [0, 2, 0], [1, 2, 0]], 3, 3) == 7

    # 0 .o.o.o.o.o.o.o.o.o.o. 1
    # .                       .
    # .......o...2.....o.......
    assert count_reachable_nodes([[0, 1, 10], [0, 2, 1], [1, 2, 1]], 20, 3) == 15

    # 0 .o.o.o.o.o.o.o.o.o.o. 1
    # .                       .
    # .......o...2.....o.......
    #
    # extra large max_moves
    assert count_reachable_nodes([[0, 1, 10], [0, 2, 1], [1, 2, 1]], 200000, 3) == 15
