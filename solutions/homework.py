"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.codingem.com/python-maximum-recursion-depth/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys 
sys.setrecursionlimit(10000)


def solve(st, s1, s2):
    if not(len(st)):
        return True
    an1 = an2 = False
    if len(s1) and st[0] == s1[0]:
        if (st[1:], s1[1:], s2) in d:
            an1 = d[(st[1:], s1[1:], s2)]
            d[(st[1:], s1[1:], s2)] = an1
        else:
            an1 = solve(st[1:], s1[1:], s2)
    if len(s2) and st[0] == s2[0]:
        if (st[1:], s1, s2[1:]) in d:
            an2 = d[(st[1:], s1, s2[1:])]
        else:
            an2 = solve(st[1:], s1, s2[1:])
            d[(st[1:], s1, s2[1:])] = an2
    return an1 or an2

st = input()
s1 = input()
s2 = input()
d = dict()
ans = solve(st, s1, s2)
if ans:
    print("yes")
else:
    print("no")