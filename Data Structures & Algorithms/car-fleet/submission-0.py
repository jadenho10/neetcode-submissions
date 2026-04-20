class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        stack = []

        # want descending order
        for pos, spd in sorted(pairs, reverse=True):
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
