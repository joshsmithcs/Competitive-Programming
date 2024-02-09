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
import sys
n = int(input())

array1 = [None] * n * 2
array2 = [None] * n * 2

e1 = e2 = n 
s1 = s2 = e1 + 1
count1 = count2 = 0

for i in range(n):
    if count1 > count2+11:
        for i in range(5):
            s2 -= 1
            array2[s2] = array1[e1]
            e1 -= 1
            count1 -= 1
            count2 += 1
    if count2 > count1 + 10:
        for i in range(5):
            e1 += 1
            array1[e1] = array2[s2]
            count1 += 1
            s2 += 1
            count2 -= 1            
    command, num = sys.stdin.readline().split()
    if command == "push_back":
        e2 += 1
        array2[e2] = num 
        count2 += 1
    elif command == "push_front":
        s1 -= 1
        array1[s1] = num
        count1 += 1
    elif command == "push_middle":
        while(count1 > count2+1):
            s2 -= 1
            array2[s2] = array1[e1]
            e1 -= 1
            count1 -= 1
            count2 += 1
        while(count2 > count1):
            e1 += 1
            array1[e1] = array2[s2]
            count1 += 1
            s2 += 1
            count2 -= 1
        if count1 > count2:
            s2 -= 1
            array2[s2] = num
            count2 += 1
        else:
            e1 += 1
            array1[e1] = num
            count1 += 1
    else:
        num = int(num)
        if num >= count1:
            num -= count1
            print(array2[s2+num])
        else:
            print(array1[s1+num])

2
<<hate<<<<loves[steva<en ] cs2040c< and also cs2040c
my ]]name]] is]] steva<en]<n halim]]]]]
            
            
        
    
    

