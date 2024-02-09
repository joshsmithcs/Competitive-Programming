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

N = int(input())
D = int(input())
binary = input()[2:]
dec = 0
j = 1/2
for i in binary:
    dec += int(i)*j
    j = j/2
string = ""
j = D/8
upper = 1 
lower = 0
for i in range(N):
    difference = upper - lower
    j = difference * D/8 + lower
    if dec >= j:
        string += "B"
        lower = j
    else:
        string += "A"
        upper = j
print(string)