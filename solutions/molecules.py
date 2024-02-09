"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925929/mod_resource/content/3/403_numerical_algorithms.pdf
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/linear_algebra/max_xor.py
  https://eclass.srv.ualberta.ca/pluginfile.php/7925932/mod_resource/content/1/equationsolverplus.cpp

  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
EPS = 1e-8

def rref(m):
    nr = len(m)
    nc = len(m[0])
    r = -1
    for c in range(nc):
        #print(m)
        r += 1
        #Find a row to pivot on, choose the one with smallest absolute value for the pivot entry
        p = -1
        i = r
        while i < nr:
            if abs(m[i][c]) > EPS and (p == -1 or abs(m[i][c]) < abs(m[p][c])):
                p = i
            i += 1
            
        if p == -1:
            continue #no pivot
        
        #swap the pivot row into row r
        temp = m[p]
        m[p] = m[c]
        m[c] = temp
        #print(m)
        #normalize pivot row (now at row r) so the leading coefficient is 1
        tc = nc -1
        while tc >= c:
            m[r][tc] /= m[r][c]
            tc -= 1
            
        #use row operations to clear all remaining nonzeros in this column 
        for tr in range(nr):
            if (tr == r or abs(m[tr][c]) < EPS):
                continue #don't bother if it is already 0
            tc = nc-1
            while (tc >= c):
                m[tr][tc] -= m[r][tc]*m[tr][c]
                tc -= 1
    return m
           
        
        
        
n, m = map(int, input().split())
X = []
Y = []
matrix = []
Tmatrix = []
for i in range(n):
    ma = []
    for j in range(n):
        ma.append(0)
    matrix.append(ma)
    Tmatrix.append([])
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    if x >= 0:
        matrix[i][i] = 1
    else:
        matrix[i][i] = -1
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if X[a] == -1:
        Tmatrix[a].append(b)
    if X[b] == -1:
        Tmatrix[b].append(a)
for i in range(n):
    l = len(Tmatrix[i])
    for j in Tmatrix[i]:
        matrix[i][j] = 1/l
xm = []
ym = []
for i in range(len(matrix)):
    xm.append(list(matrix[i]))
    ym.append(list(matrix[i]))
for i in range(len(matrix)):
    xm[i].append(max(X[i],0))
    ym[i].append(max(Y[i],0))
xm = rref(xm)
ym = rref(ym)
for i in range(n):
    if X[i] > -1:
        print(X[i], Y[i])
    else:
        print(xm[i][-1], ym[i][-1])
    