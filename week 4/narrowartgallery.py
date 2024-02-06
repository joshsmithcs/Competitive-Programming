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

(N, K) = map(int,input().split())
L = dict()
R = dict()
for i in range(N+1):
    for j in range(K+1):
        L[(i,j)] = -101
        R[(i,j)] = -101
L[(0,0)] = 0
R[(0,0)] = 0
for i in range(1, N+1):
    (l, r) = map(int,input().split())
    k = min(i, K)
    for j in range(k+1):
        if j == 0:
            L[(i,0)] = L[(i-1,0)] + l + r
            R[(i,0)] = R[(i-1,0)] + l + r
        else:
            L[(i,j)] = max(max(L[(i-1,j)], R[(i-1,j)]) + l + r, L[(i-1,j-1)] + l)
            R[(i,j)] = max(max(L[(i-1,j)], R[(i-1,j)]) + l + r, R[(i-1,j-1)] + r)
print(max(L[(i,K)], R[(i,K)]))
        