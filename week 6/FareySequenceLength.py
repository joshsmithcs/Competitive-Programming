"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925890/mod_resource/content/4/403_numtheory_2022.pdf

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
arr = [1] * (10001)
ans = 2
ansArr = [0] * (10001)
for i in range(2, 10001):
    ans += i - arr[i]
    for j in range(i*2, 10001, i):
        arr[j] += i - arr[i]
    ansArr[i] = ans
cases = int(input())
for _ in range(cases):
    case, num = map(int, input().split())
    print(case, ansArr[num])
