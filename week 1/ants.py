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

cases = int(input())
for case in range(cases):
    lengthPole, numAnts = map(int, input().split())
    positions = 0
    closestToEnd = 0
    furthestFromEnd = 0
    while positions < numAnts:
        ants = input().split()
        positions += len(ants)
        for ant in ants:
            ant = int(ant)
            #minimum
            dist = min(ant, lengthPole-ant)
            if dist > furthestFromEnd:
                furthestFromEnd = dist
            #maximum
            dist = max(ant, lengthPole-ant)
            if dist > closestToEnd:
                closestToEnd = dist
    print(str(furthestFromEnd) + " " + str(closestToEnd))