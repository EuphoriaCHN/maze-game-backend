# coding=utf-8

class UnionFind(object):
    def __init__(self, length: int):
        self.union_set = [i for i in range(length)]
        self.set_count = length

    def get_root(self, target: int) -> int:
        if target == self.union_set[target]:
            return target
        self.union_set[target] = self.get_root(self.union_set[target])
        return self.union_set[target]

    def union(self, x: int, y: int) -> None:
        x_root = self.get_root(x)
        y_root = self.get_root(y)
        if x_root != y_root:
            if x_root < y_root:
                self.union_set[y] = x
            else:
                self.union_set[x] = y
        self.set_count -= 1

    def is_same_union(self, x: int, y: int) -> bool:
        return self.get_root(x) == self.get_root(y)
