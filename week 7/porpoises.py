"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.johndcook.com/blog/2008/12/10/fast-exponentiation/
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/linear_algebra/matrix.py

  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
#use linear recurrences
mat_mul = lambda A, B: [[sum(i * j for i, j in zip(row, col)) for col in zip(*B)] for row in A]
def eye(m):
    """returns an indentity matrix of order m"""
    identity = [[0] * m for _ in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1
    return identity
def mat_pow(mat, power):
    """returns mat**power"""

    result = eye(len(mat))

    while power > 1:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1
        for i in range(2):
            for j in range(2): 
                result[i][j] = result[i][j]%1000000000
                mat[i][j] = mat[i][j]%1000000000
    ans = mat_mul(result, mat)
    ans = ans[1][1]%1000000000
    return ans
cases = int(input())
for _ in range(cases):
    i, num = map(int, input().split())
    if num < 3:
        print(i, 1)
    else:
        mat = [[0,1], [1,1]]
        #pw = num - 2
        #res = mat_pow(mat, pw)
        #print(res)
        #res = mat_mul(res, [[1],[1],[0]])
        #print(res)
        #mat2 = [[1],[1],[0]]
        ans = mat_pow(mat, num-1)
        print(i, ans)
        
    
    
    
    