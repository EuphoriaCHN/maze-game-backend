# coding=utf-8

"""
Algorithm named Breadth-First Search, is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'),
and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It uses the opposite strategy as depth-first search,
which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.

From [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
"""

from queue import Queue


def breadth_first_search(maze: list, start: list, end: list) -> list:
    MAX_ROWS = len(maze)
    MAX_COLUMNS = len(maze[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    step = {
        (-1, 0): 2,
        (1, 0): 1,
        (0, -1): 4,
        (0, 1): 3
    }

    for rows in range(0, MAX_ROWS):
        for cols in range(0, MAX_COLUMNS):
            maze[rows][cols] = -1 if maze[rows][cols] is 1 else 0

    queue = Queue()
    queue.put(start)

    ans = []

    while not queue.empty():
        now_at = queue.get()
        for i in range(0, 4):
            temp_x = now_at[0] + dx[i]
            temp_y = now_at[1] + dy[i]
            if 0 <= temp_x < MAX_ROWS and 0 <= temp_y < MAX_COLUMNS:
                if maze[temp_x][temp_y] is not -1:
                    if maze[temp_x][temp_y] is 0:
                        if [temp_x, temp_y] != start:
                            queue.put([temp_x, temp_y])
                            maze[temp_x][temp_y] = maze[now_at[0]][now_at[1]] + 1
                    else:
                        calculate_value = maze[now_at[0]][now_at[1]] + 1
                        if maze[temp_x][temp_y] > calculate_value:
                            queue.put([temp_x, temp_y])
                            maze[temp_x][temp_y] = calculate_value

    x_cur, y_cur = end

    while [x_cur, y_cur] != start:
        for i in range(0, 4):
            temp_x = x_cur + dx[i]
            temp_y = y_cur + dy[i]
            if 0 <= temp_x < MAX_ROWS and 0 <= temp_y < MAX_COLUMNS:
                if maze[temp_x][temp_y] == maze[x_cur][y_cur] - 1:
                    ans.append(step.get((dx[i], dy[i])))
                    x_cur, y_cur = temp_x, temp_y
                    break

    ans.reverse()
    return ans
