# coding=utf-8

import random
from tools.UnionFind import UnionFind

_debug = False


def get_block_union_id(index: list, standard_num_cols: int) -> int:
    # ================================================
    # V1.0 改动：
    # 因为把所有的墙壁也放入了并查集，那么对应的节点编号应该改变
    # ================================================
    # return int(int(index[0] - index[0] / 2) * standard_num_cols + index[1] / 2)
    return index[0] * standard_num_cols + index[1]


def build_twist(num_rows: int, num_cols: int) -> list:
    # 初始化带墙体迷宫
    map = list(list(0 if j & 1 is 0 else 1 for j in range(num_cols)) if i & 1 is 0 else [1] * num_cols for i in
               range(num_rows))

    # ================================================
    # V1.0 改动：
    # 因为将所有的墙体都放入了并查集，那么并查集标准行数和列数就是迷宫的行数和列数
    # ================================================
    # standard_num_cols = int(num_cols / 2) + 1
    # standard_num_rows = (int(num_rows / 2) + 1)
    standard_num_cols = num_cols
    standard_num_rows = num_rows

    # 初始化并查集
    # ================================================
    # V1.0 改动，将整个迷宫中每一格都放入并查集，以用来合并墙体
    # 所以并查集的长度应该为 rows * cols
    # ================================================
    union_find = UnionFind(num_rows * num_cols)

    # ================================================
    # V1.0 注释：此时仍然设置起点为左上角，终点为右下角
    # ================================================
    start_point_union_id = 0
    end_point_union_id = union_find.set_count - 1

    # 初始化墙壁集合
    wall_set = []
    for i in range(num_rows):
        if i & 0x1 is 1:
            for j in range(num_cols):
                wall_set.append([i, j])
        else:
            for j in range(1, num_cols, 2):
                wall_set.append([i, j])

    # 定义一个墙壁交叉处集合，避免不断地在循环中取到错误的墙壁而造成的时间浪费
    cross_block = []

    while union_find.set_count is not 1 and len(wall_set) is not 0:
        wall = random.choice(wall_set)

        # 移除这面墙
        wall_set.remove(wall)

        if wall[0] & 0x1 is 1:
            # 奇数下标的墙壁全部开上下
            top = [wall[0] - 1, wall[1]]
            bottom = [wall[0] + 1, wall[1]]
            # 如果刚好拿到了墙壁交叉处，即如果它的上下有一个是墙的话，则放弃本次选取
            if top in wall_set or bottom in wall_set:
                # 加入交叉墙壁表，以免下次又拿到它
                cross_block.append(wall)
                continue
            first_union_id = get_block_union_id(top, standard_num_cols)  # 上
            second_union_id = get_block_union_id(bottom, standard_num_cols)  # 下
        else:
            # 偶数下标的墙壁全部开左右
            left = [wall[0], wall[1] - 1]
            right = [wall[0], wall[1] + 1]
            # 如果刚好拿到了墙壁交叉处，即如果它的左右有一个是墙的话，则放弃本次选取
            if left in wall_set or right in wall_set:
                # 加入交叉墙壁表，以免下次又拿到它
                cross_block.append(wall)
                continue
            first_union_id = get_block_union_id(left, standard_num_cols)  # 左
            second_union_id = get_block_union_id(right, standard_num_cols)  # 右

        if len(cross_block) is not 0:
            # 只要程序能成功运行到这里，就说明拿到了正确的墙壁，那么需要把所有的交叉墙壁归还回去
            wall_set.extend(cross_block)
            cross_block.clear()

        # 拿到并查集根节点
        first_root = union_find.get_root(first_union_id)
        second_root = union_find.get_root(second_union_id)

        # 如果墙两侧的区块在并查集中同祖先，即这个墙即使不打通，两个区块也可以互相到达
        # 所以这面墙打通是没有意义的

        if first_root != second_root:
            # 当墙两侧的区块位于不同路径时，则需要合并
            union_find.union(first_union_id, second_union_id)
            # 打通这面墙
            map[wall[0]][wall[1]] = 0
            # ================================================
            # V1.0 改动：
            # 既然已经合并了，那么根节点应该是相同的
            # ================================================
            merged_root = union_find.get_root(first_union_id)
            # ================================================
            # V1.0 改动：
            # 因为打通了墙壁，那么这面墙也形成了一个通路，将墙壁也与合并后的结果统一合并
            # ================================================
            wall_id = union_find.get_root(get_block_union_id(wall, standard_num_cols))
            union_find.union(wall_id, merged_root)

        if union_find.get_root(start_point_union_id) == union_find.get_root(end_point_union_id):
            # 如果起点和终点之间有路了，那么可以直接退出掉
            break

    return map
