from collections import deque
class FreqStack:

    def __init__(self):
        self.l = deque()
        self.freqs = collections.Counter()
        

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        if self.freqs[val] - 1 < len(self.l):
            self.l[self.freqs[val] - 1].append(val)
        else:
            self.l.append([val])

        

    def pop(self) -> int:
        ans = self.l[-1].pop()
        if not self.l[-1]:
            del self.l[-1]
        self.freqs[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()