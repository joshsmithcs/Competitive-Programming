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
import sys 
sys.setrecursionlimit(100000)
rightLookup = {(1,4) : 2, (1,2) : 3, (1,3) : 5, (1,5) : 4,
               (2,4) : 6, (2,6) : 3, (2,3) : 1, (2,1) : 4,
               (3,5) : 1, (3,1) : 2, (3,2) : 6, (3,6) : 5,
               (4,1) : 5, (4,5) : 6, (4,6) : 2, (4,2) : 1,
               (5,4) : 1, (5,1) : 3, (5,3) : 6, (5,6) : 4,
               (6,4) : 5, (6,5) : 3, (6,3) : 2, (6,2) : 4}
def search(x, y, top, up):
    if (x, y, top, up) in d:
        return False
    if x == end[0] and y == end[1] and top == end[2]:
        return True
    ans = False
    d[(x, y, top, up)] = ans
    #move up
    if y > 0 and forest[y-1][x] != "*":
        ans = search(x, y-1, up, 7-top)
    #move down
    if y < N-1 and forest[y+1][x] != "*":
        ans = ans or search(x, y+1, 7-up, top)
    #move left
    if x > 0 and forest[y][x-1] != "*":
        ans = ans or search(x-1, y, rightLookup[(top,up)], up)
    #move right
    if x < N-1 and forest[y][x+1] != "*":
        ans = ans or search(x+1, y, 7 - rightLookup[(top,up)], up)
    d[(x, y, top, up)] = ans
    #print(x, y, top, up, ans)
    return ans
cases = int(input())
for i in range(cases):
    N = int(input())
    forest = []
    start = None
    d = dict()
    for i in range(N):
        l = []
        line = input()
        for j in range(N):
            if line[j] == "S":
                start = (j, i, 1, 4)
            if line[j] == "H":
                end = (j, i, 2)
            l.append(line[j])
        forest.append(l)
    found = search(start[0], start[1], start[2], start[3])
    if found:
        print("Yes")
    else:
        print("No")