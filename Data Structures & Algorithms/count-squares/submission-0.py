class CountSquares:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.hashmap[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (x == px or y == py) or (abs(x - px) != abs(y - py)):
                continue
            res += self.hashmap[(px, y)] * self.hashmap[(x, py)]
        return res
