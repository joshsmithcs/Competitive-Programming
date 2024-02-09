"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/kruskal.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def kruskal(n, U, V, W):
    union = UnionFind(n)
    cost, merge_cnt = 0, 0
    mst_u, mst_v = [], []
    order = sorted(range(len(W)), key=lambda x: W[x])
    for i in range(len(W)):
        u, v = U[order[i]], V[order[i]]
        find_u, find_v = union.find(u), union.find(v)
        if find_u != find_v:
            cost += W[order[i]]
            merge_cnt += 1
            union.parent[find_v] = find_u
            mst_u.append(u), mst_v.append(v)
    return cost, mst_u, mst_v, n == 1 + merge_cnt

n, m, p = map(int, input().split())
insecureBuildingsString = input().split()
iS = []
for i in insecureBuildingsString:
    iS.append(int(i))
iS = sorted(iS)
insecureIter = 0
insecureBuildings = set()
secureMapping = dict()
numSecure = n - p
for i in range(1, n+1):
    if len(iS) > insecureIter and iS[insecureIter] == i:
        insecureBuildings.add(i)
        insecureIter += 1
    else:
        secureMapping[i] = i - insecureIter
insecureMin = dict()
U = []
V = []
W = []
for i in range(m):
    u, v, w = map(int, input().split())
    if u not in insecureBuildings and v not in insecureBuildings:
        U.append(secureMapping[u] - 1)
        V.append(secureMapping[v] - 1)
        W.append(w)
    elif u in insecureBuildings and v in insecureBuildings:
        pass
    elif u in insecureBuildings:
        if u in insecureMin:
            insecureMin[u] = min(w, insecureMin[u])
        else:
            insecureMin[u] = w
    else:
        if v in insecureMin:
            insecureMin[v] = min(w, insecureMin[v])
        else:
            insecureMin[v] = w
if n == 1:
    print(0)
elif m == 0:
    print("impossible")
elif n == 2 and p == 2: 
    print(w)
else:
    weight, _, _, ln = kruskal(numSecure, U, V, W)
    if not(ln):
        print("impossible")
    else: 
        possible = True
        for i in insecureBuildings:
            if i in insecureMin:
                weight += insecureMin[i]
            else: 
                possible = False
        if possible:
            print(weight)
        else:
            print("impossible")
        