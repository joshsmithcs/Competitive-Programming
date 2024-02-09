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
def solve(colorsUsed):
    cur = len(solution)
    if cur == N:
        return colorsUsed
    possibleColors = set()
    for i in range(colorsUsed):
        possibleColors.add(i)
    for i in range(cur):
        if (i, cur) in d and solution[i] in possibleColors:
            possibleColors.remove(solution[i])
    s = 12 
    for i in possibleColors:
        solution.append(i)
        ans = solve(colorsUsed)
        if ans: 
            s = min(s, ans)
        solution.pop()
    if s == colorsUsed:
        return s 
    else:
        solution.append(colorsUsed)
        ans = solve(colorsUsed+1)
        if ans: 
            s = min(s, ans)
        solution.pop()
        return s

N = int(input())
d = dict()
solution = [0]
for i in range(N):
    vertices = map(int, input().split())
    for j in vertices:
        if i < j:
            d[(i,j)] = True
s = solve(1)
print(s)