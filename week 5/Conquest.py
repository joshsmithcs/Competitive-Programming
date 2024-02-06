"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dijkstra.py
  https://stackoverflow.com/questions/5518435/python-fastest-way-to-create-a-list-of-n-lists

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
from heapq import heappop, heappush
import sys
from itertools import repeat
import time


def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist = [float("inf")] * n
    dist[0] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        #print(path_len, v)
        if v-1 not in done:
            for w in graph[v-1]:
                if path_len < dist[w-1]:
                    if path_len < army[w-1]:
                        dist[w-1] = army[w-1]
                        heappush(queue, (dist[w-1], w))
                    else:
                        dist[w-1] = path_len
                        heappush(queue, (dist[w-1], w))
            done[v-1] = True

    return dist
done = dict()
#t0 = time.time()
#get edges that can be reached and order them by army size, conquer and add edges until no more can be conquered
N, M = map(int, input().split())
bridges = [[] for i in repeat(None, N)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    bridges[x-1].append(y)
    bridges[y-1].append(x)
army = []
for i in range(N):
    army.append(int(sys.stdin.readline().rstrip('\n')))
#t1 = time.time()
#print(t1-t0)
if M == 0:
    print(army[0])
else:
    dists = dijkstra(bridges, 1)
    #t2 = time.time()
    #print(t2-t1)
    reachableArmy = []
    for i in range(1, N):
        reachableArmy.append((dists[i], army[i]))
    reachableArmy.sort()
    curArmy = army[0]
    i = 0
    for i in range(len(reachableArmy)):
        if curArmy > reachableArmy[i][0]:
            curArmy += reachableArmy[i][1]
            i += 1
        else:
            break
    #t3 = time.time()
    #print(t3-t2)
    print(curArmy)