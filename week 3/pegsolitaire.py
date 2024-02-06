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
def pegSolver(d):
    totalmin = len(d)
    if totalmin != 1:
        s = []
        for i in d:
            s.append(i)
        for i in s:
            (a, b) = i
            if (a, b + 1) in d and not((a, b + 2) in d) and (a, b + 2) in valid:
                del d[(a, b)]
                del d[(a, b + 1)]
                d[(a, b + 2)] = True
                mn1 = pegSolver(d)
                d[(a, b)] = True
                d[(a, b + 1)] = True
                del d[(a, b + 2)]
                totalmin = min(mn1, totalmin)
            if (a, b - 1) in d and not((a, b - 2) in d) and (a, b - 2) in valid:
                del d[(a, b)]
                del d[(a, b - 1)]
                d[(a, b - 2)] = True
                mn2 = pegSolver(d)
                d[(a, b - 1)] = True
                d[(a, b)] = True
                del d[(a, b - 2)]
                totalmin = min(mn2, totalmin)
            if (a + 1, b) in d and not((a + 2, b) in d) and (a + 2, b) in valid:
                del d[(a, b)]
                del d[(a + 1, b)]
                d[(a + 2, b)] = True
                mn3 = pegSolver(d)
                d[(a, b)] = True
                d[(a + 1, b)] = True
                del d[(a + 2, b)]
                totalmin = min(mn3, totalmin)
            if (a - 1, b) in d and not((a - 2, b) in d) and (a - 2, b) in valid:
                del d[(a, b)]
                del d[(a - 1, b)]
                d[(a - 2, b)] = True
                mn4 = pegSolver(d)
                d[(a - 1, b)] = True
                d[(a, b)] = True
                del d[(a - 2, b)]
                totalmin = min(mn4, totalmin)
    return totalmin
        
            
cases = int(input())
valid = {(0, 3), (0, 4), (0, 5),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), 
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), 
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), 
         (4, 3), (4, 4), (4, 5)}
for i in range(cases):
    if i != 0:
        _ = input()
    d = dict()
    startPegs = 0
    for i in range(5):
        line = input()
        for j in range(9):
            if line[j] == "o":
                d[i,j] = True
                startPegs += 1
    mn = pegSolver(d)
    print(str(mn) + " " + str(startPegs-mn))
    
    
        
        
