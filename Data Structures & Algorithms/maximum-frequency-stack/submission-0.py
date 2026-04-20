class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.count = defaultdict(int) # freq list

    def push(self, val: int) -> None:
        self.count[val] += 1
        freq = self.count[val]

        if len(self.stack) == freq:
            self.stack.append([])
        self.stack[freq].append(val)

    def pop(self) -> int:
        val = self.stack[-1].pop()
        self.count[val] -= 1
        if not self.stack[-1]:
            self.stack.pop()
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()