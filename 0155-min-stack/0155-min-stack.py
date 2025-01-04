class MinStack(object):

    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk.append(val)
        if len(self.mstk) == 0:
            self.mstk.append(val)
        else:
            self.mstk.append(min(self.mstk[-1], val))

    def pop(self):
        """
        :rtype: None
        """
        if self.stk:
            self.stk.pop(-1)
            self.mstk.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()