class QuickFind():
    number = 0
    nums = {}

    def __init__(self, number):
        QuickFind.number = number
        for i in range(QuickFind.number):
            QuickFind.nums[i] = i
        print (QuickFind.nums)

    def connected(self, p, q):
        return QuickFind.nums[p] == QuickFind.nums[q]
    
    def union(self, p, q):
        idp = QuickFind.nums[p]
        idq = QuickFind.nums[q]
        for i in range(len(QuickFind.nums)):
            if QuickFind.nums[i] == idp :
                QuickFind.nums[i] = idq

a = QuickFind(10)
# print(a.connected(6,6))
a.union(1,2)
print (a.nums)
a.union(1,7)
print (a.nums)