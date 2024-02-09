"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

#topological sorting -> Kahn's that keeps track of each nodes initial connections and current and remove when it reaches half
C, P, X, L = map(int, input().split())
lst = []
for i in range(C):
    lst.append(set())
for i in range(P):
    x, y = map(int, input().split())
    lst[x-1].add(y)
    lst[y-1].add(x)
initSizes = []
for i in range(C):
    initSizes.append(len(lst[i]))
#print(lst)
queue = [L]
itr = 0
while(len(queue) != itr):
    t = queue[itr]
    #print(t)
    itr += 1
    if lst[t-1]:
        for i in lst[t-1]:
            #remove from
            lst[i-1].remove(t)
            if len(lst[i-1]) <= initSizes[i-1] // 2:
                queue.append(i)       
        lst[t-1] = 0
if lst[X-1]:
    print("stay")
else:
    print("leave")
            