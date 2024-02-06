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

N, K = map(int,input().split())
unsafe = 0
lastWatch = 0
for i in range(K):
    watch = int(input())
    diff = watch - lastWatch - 1
    if diff >= 1:
        unsafe += diff * (diff + 1) / 2
    lastWatch = watch
if lastWatch != N:
    diff = N - lastWatch
    unsafe += diff * (diff + 1) / 2
total = N * (N + 1) / 2
print(int(total-unsafe))