# Python solution for the Kattis problem cinema2
# For CMPUT 403
# Zachary Friggstad - 2022

# Normally not great variable names, but they agree with
# the input specification so it makes debugging easier.
n, m = map(int, input().split())

# Read in the groups as a list.
groups = list(map(int, input().split()))

# While we can seat the next group, do it!
# This is actually an O(m^2) impelentation, can you see why? What would
# you have to do to make it O(m)?
seated = 0
while seated < m and sum(groups[:seated+1]) <= n:
    seated += 1

print(m-seated)