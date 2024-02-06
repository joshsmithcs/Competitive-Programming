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
from sys import stdin, stdout

x = 200
N, Q = map(int, input().split())
nums = [0] * (N+1)
d = []
for i in range(x):
    r = []
    for j in range(i):
        r.append(0)
    d.append(r)
for _ in range(Q):
    inp = stdin.readline()
    if inp[0] == "1":
        A, B, C = map(int, inp[2:].split())
        if B < x:
            d[B][A] += C
        else:
            while A <= N:
                nums[A] += C
                A += B
    else:
        k = int(inp[2:])
        n = nums[k]
        for i in range(1,x):
            n += d[i][k%i]
        stdout.write(str(n))
        stdout.write("\n")