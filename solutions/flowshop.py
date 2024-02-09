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

N, M = map(int, input().split())
blocker = [0] * M
work = []
ans = ""
for i in range(N):
    w = input().split()
    for i in range(M):
        w[i] = int(w[i])
    work.append(w)
for i in range(N):
    time = 0
    for j in range(M):
        if time < blocker[j]:
            time = blocker[j]
        time += work[i][j] 
        blocker[j] = time
    if i == 0:
        ans += str(time)
    else:
        ans = ans + " " + str(time)
print(ans)
                