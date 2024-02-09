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
def dist(a, b, c, d):
    return (abs(c-a)**2 + abs(d-b)**2)**0.5

def composite(num):
    # 142^2 > 20,000 
    i = 2
    while i < 142:
        if num%i == 0 and num != i:
            return True
        i+=1
    return False


cases = int(input())
for i in range(cases):
    N, D = map(int, input().split())
    travelled = 0.0
    locationx = 0.0
    locationy = 0.0
    d = dict()
    for j in range(N):
        d[j] = input()
    flower = 0
    while (travelled < D and flower < N):
        f = d[flower]
        x, y = map(int, f.split())
        travelled = travelled + dist(locationx, locationy, x, y)
        locationx = x
        locationy = y
        flower += 1
    if travelled > D:
        flower -= 1
    if i == 0 or i == 1:
        print("0")
    else:
        while(composite(flower) and flower != 0):
            flower -= 1
        print(flower)
    
    
