"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925890/mod_resource/content/4/403_numtheory_2022.pdf

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""


def update(p, q):
    return (p[1], p[0] - q*p[1])
def gcdex(r):
    s = [1,0]
    t = [0,1]
    while r[1]:
        q = r[0]//r[1]
        r = update(r,q)
        s = update(s,q)
        t = update(t,q)
    return [s[0],t[0]], r[0]

def linDiop(a, b):
    d = 1
    p, g = gcdex([a, b])

    if (d%g != 0):
        print("IMPOSSIBLE")
    else:
        ans = int(p[0])
        while (ans - b) > 0:
            ans -= b
        while ans <= 0:
            ans += b
        if ans > 1000000000:
            print("IMPOSSIBLE")
        else:
            print(ans)

cases = int(input())
for i in range(cases):
    K, C = map(int, input().split())
    if K > 1 and C > 1:
        linDiop(C, K)
    else: 
        if K == 1:
            if C == 1:
                print(2)
            else: 
                print(1)
        else:
            if K == 1000000000:
                print("IMPOSSIBLE")
            else:
                print(K+1)
    