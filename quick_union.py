class QuickUnion():
    num = {}

    def __init__(self, N):
        for i in range(N):
            self.num[i]=i
        print (self.num)

    def root(self, n):
        #rootn = self.num[n]
        while not (self.num[n] == n):
            n = self.num[n]
        return n
    
    def union(self,p,q):
        qroot = self.root(q)
        proot = self.root(p)
        self.num[proot] = qroot
        print(self.num)
    
    def connected(self,p,q):
        if self.root(p) == self.root(q):
            print ("{} and {} are connected".format(p,q))
        else:
            print ("{} and {} are not connected".format(p,q))

import time
start_time = time.time()
a = QuickUnion(10)
a.union(4,3)
a.union(3,8)
a.union(6,5)
a.union(9,4)
a.union(2,1)
a.connected(8,9)
a.connected(5,4)
a.union(5,0)
a.union(7,2)
a.union(6,1)
a.union(7,3)
print ("Time Taken: ",start_time-time.time())