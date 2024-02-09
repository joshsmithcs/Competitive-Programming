"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
def euclid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    rem = a % b
    return euclid(b, rem)
    
def mincommon(bx, by):
    if bx == 0:
        return 0, 1
    if by == 0:
        return 1, 0
    if bx >= by:
        cf = euclid(bx, by)
    else:
        cf = euclid(by, bx)
    return bx // cf, by // cf  
        
(bx, by) = map(int, input().split())
x, y = mincommon(bx,by)
(clearingminx, clearingminy, clearingmaxx, clearingmaxy) = map(int, input().split())
finish = True
if x >= clearingminx and y >= clearingminy and bx-x <= clearingmaxx and by-y <= clearingmaxy:
    print("Yes")
elif bx == x and by == y:
        print("Yes")
elif x < clearingminx or y < clearingminy: 
    print("No")
    print(str(x) + " " + str(y))
else:
    iterationsx = clearingmaxx // x
    iterationsy = clearingmaxy // y
    itr = min(iterationsx, iterationsy) + 1
    print("No")
    print(str(x*itr) + " " + str(y*itr))