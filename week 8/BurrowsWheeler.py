"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/suffix_array.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys

def SAIS(A):
    """
    Calculates suffix array in O(len(A) + max(A))
    Input:
    Int list A with A[i] >= 0 for all i
    """
    n = len(A)
    buckets = [0] * (max(A) + 2)
    for a in A:
        buckets[a + 1] += 1
    for b in range(1, len(buckets)):
        buckets[b] += buckets[b - 1]
    isL = [1] * n
    for i in reversed(range(n - 1)):
        isL[i] = +(A[i] > A[i + 1]) if A[i] != A[i + 1] else isL[i + 1]

    def induced_sort(LMS):
        SA = [-1] * (n)
        SA.append(n)
        endpoint = buckets[1:]
        for j in reversed(LMS):
            endpoint[A[j]] -= 1
            SA[endpoint[A[j]]] = j
        startpoint = buckets[:-1]
        for i in range(-1, n):
            j = SA[i] - 1
            if j >= 0 and isL[j]:
                SA[startpoint[A[j]]] = j
                startpoint[A[j]] += 1
        SA.pop()
        endpoint = buckets[1:]
        for i in reversed(range(n)):
            j = SA[i] - 1
            if j >= 0 and not isL[j]:
                endpoint[A[j]] -= 1
                SA[endpoint[A[j]]] = j
        return SA

    isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
    isLMS.append(1)
    LMS = [i for i in range(n) if isLMS[i]]
    if len(LMS) > 1:
        SA = induced_sort(LMS)
        LMS2 = [i for i in SA if isLMS[i]]
        prev = -1
        j = 0
        for i in LMS2:
            i1 = prev
            i2 = i
            while prev >= 0 and A[i1] == A[i2]:
                i1 += 1
                i2 += 1
                if isLMS[i1] or isLMS[i2]:
                    j -= isLMS[i1] and isLMS[i2]
                    break
            j += 1
            prev = i
            SA[i] = j
        LMS = [LMS[i] for i in SAIS([SA[i] for i in LMS])]
    return induced_sort(LMS)

while True:
    line = sys.stdin.readline()
    if line == "":
        break
    else:
        S = line[:-1]
        ln = len(S)
        S = S + S
        SA = SAIS([ord(c) for c in S])
        char = ""
        for i in SA:
            if i >= ln:
                pass
            elif i == 0:
                char += S[-1]
            else:
                char += S[i-1]
    print(char)