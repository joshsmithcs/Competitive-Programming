"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/scc.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
"""
Given a directed graph, find_SCC returns a list of lists containing 
the strongly connected components in topological order.
Note that this implementation can be also be used to check if a directed graph is a
DAG, and in that case it can be used to find the topological ordering of the nodes.
"""
def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)

    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


#How many edges need to be added to make a strongly connected graph
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append([])
    #print(graph)
    for j in range(m):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
    #print("graph", graph)
    s = find_SCC(graph)
    if len(s) == 1:
        print(0)
    else:
        #print(s)
    
        oldgraph = graph
        graph = []
        for i in range(len(s)):
            graph.append([]) 
        i = 0
        d = dict()
        for con in s:
            for e in con:
                d[e] = i
                #print(e)
                for v in oldgraph[e]:
                    #print("v", v)
                    if v not in graph[i] and v not in con:
                        graph[i].append(v)   
            i += 1
        #print(oldgraph)
        #print(graph)
        uniqueSet = set()
        leaf = 0
        for lst in graph:
            if len(lst) == 0:
                leaf += 1
            else: 
                for i in lst:
                    uniqueSet.add(d[i])
        head = len(graph) - len(uniqueSet)
        solution = max(leaf, head)
        print(solution)
    