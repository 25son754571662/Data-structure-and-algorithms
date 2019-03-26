class Solution:
    def __init__(self):
        self.l=[]
        self.minelem=[]
    def push(self, node):
        self.l.insert(0,node)
        self.minelem.insert(0,node if self.minelem==[] else min(self.minelem[0],node))
    def pop(self):
        self.minelem.pop(0)
        return self.l.pop(0)
    def top(self):
        return self.l[0]
    def min(self):
        return self.minelem[0]