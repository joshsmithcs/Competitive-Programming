"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://pythonguides.com/python-sort-list-of-tuples/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys

unread, new, JaneEyre = map(int, input().split())
minutes = 0
for i in range(unread):
    _, title, pagec = sys.stdin.readline().split("\"")
    if title < "Jane Eyre":
        minutes += int(pagec)
booklist = []
for i in range(new):
    time, title, pagec = sys.stdin.readline().split("\"")
    if title < "Jane Eyre":
        booklist.append((int(time.rstrip(" ")), pagec.rstrip("\n")))
booklist.sort()
for book in booklist:
    if minutes >= book[0]:
        minutes += int(book[1])
    else:
        break
minutes += JaneEyre
print(minutes)
        
         