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

N, B, R = map(int, input().split())
blueberryCoords = []
for i in range(B):
    x, y = map(int, input().split())
    blueberryCoords.append((x,y))
raspberryCoords = []
for i in range(R):
    x, y = map(int, input().split())
    raspberryCoords.append((x,y))
d = dict()
for i in range(B):
    for j in range(R):
        d[(i,j)] = (blueberryCoords[i][0] - raspberryCoords[j][0])**2 + (blueberryCoords[i][1] - raspberryCoords[j][1])**2
print(d)