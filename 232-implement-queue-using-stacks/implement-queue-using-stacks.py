class MyQueue(object):

    def __init__(self):
        self.main = deque()
        self.rv = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.main.append(x)



    def pop(self):
        """
        :rtype: int
        """
        while self.main:
            self.rv.append(self.main.pop())

        rs = self.rv.pop()

        while self.rv:
            self.main.append(self.rv.pop())

        return rs
        

    def peek(self):
        """
        :rtype: int
        """
        while self.main:
            self.rv.append(self.main.pop())

        rs = self.rv[-1]

        while self.rv:
            self.main.append(self.rv.pop())

        return rs

    def empty(self):
        """
        :rtype: bool
        """

        return len(self.main) == 0 and len(self.rv) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()