class MyQueue:
    def _init_(self):
        self.queue = []
    def push(self, x):
        self.queue.append(x)
    def pop(self): 
        if len(self.queue)==0:
            return -1
        return self.queue.pop(0)
