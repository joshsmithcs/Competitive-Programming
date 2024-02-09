"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925875/mod_resource/content/2/paintings.cpp
  https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys 

def solve():
    if len(order) == numStudents:
        return order    
    for i in range(numStudents):
        if not(students[i] in order) and not(order[-1], students[i]) in rules:
            order.append(students[i])
            o = solve()
            if o:
                return o
            order.pop()
    return 0
def solve1():
    for i in range(numStudents):
        order.append(students[i])
        o = solve()   
        if o:
            return o
        order.pop()       

numStudents = input()
while True:        
    if numStudents == "":
        break
    numStudents = int(numStudents)
    students = []
    for i in range(numStudents):
        students.append(input())
    students = sorted(students)
    numPairs = int(input())
    rules = []
    for i in range(numPairs):
        a, b = input().split(" ")
        rules.append((a, b))
        rules.append((b, a))
    rules = set(rules)
    order = []
    d = solve1()
    if d:
        print(" ".join(d))
    else:
        print("You all need therapy.")
    numStudents = sys.stdin.readline()
