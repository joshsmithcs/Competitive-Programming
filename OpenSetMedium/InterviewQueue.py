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

numCandidates = int(input())
candidates = [int(x) for x in input().split()]
changed = True
removedList = []
step = 0
while(True):
    newList = []
    removed = []
    if len(candidates) == 1:
        removedList.append(candidates)
        break        
    if candidates[0] < candidates[1]:
        removed.append(candidates[0])
    else:
        newList.append(candidates[0])
    for i in range(1, len(candidates) - 1):
        if candidates[i-1] > candidates[i] or candidates[i] < candidates[i+1]:
            removed.append(candidates[i])
        else:
            newList.append(candidates[i])
    if candidates[-2] > candidates[-1]:
        removed.append(candidates[-1])
    else:
        newList.append(candidates[-1])
    if len(removed) == 0:
        removedList.append(candidates)
        break
    else:
        removedList.append(removed)
        step += 1
        candidates = newList
print(step)
for i in range(len(removedList)):
    print(' '.join(map(str,removedList[i])))