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

count, divisor = map(int, input().split())
numbers = input().split()
d = dict()
i = 0
ans = 0
while i < count:
    res = int(numbers[i])//divisor
    if res in d:
        ans += d[res]
        d[res] = d[res] + 1 
    else:
        d[res] = 1
    i+=1
print(ans)