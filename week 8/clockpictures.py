"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/kmp.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi

def string_find(s, pat):
    pi = partial(pat)

    g = 0
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            return True

    return False

n = int(input())
clock1 = [int(x) for x in input().split()]
clock2 =  [int(x) for x in input().split()]
clock1.sort()
clock2.sort()
s1 = []
s2 = []
for i in range(n-1):
    s1.append(str(clock1[i+1] - clock1[i]))
    s2.append(str(clock2[i+1] - clock2[i]))
s1 = "".join(s1)
s2 = "".join(s2)
s1 = s1 + str(clock1[0] - clock1[-1] + 360000)
s2 = s2 + str(clock2[0] - clock2[-1] + 360000) 
s2 = s2 + s2

possible = string_find(s2, s1)
if possible:
    print("possible")
else:
    print("impossible")