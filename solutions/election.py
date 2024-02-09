"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.quora.com/What-is-the-probability-of-tossing-k-heads-in-n-trials-of-a-fair-coin

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import math

def chance_of_getting(needed, remaining):
    spare_coins = remaining-needed
    total_chance = 0
    for i in range(spare_coins+1):
        target = needed + i
        chance = math.factorial(remaining)/math.factorial(target)/math.factorial(remaining-target)*(1/2)**remaining
        total_chance += chance
    return total_chance * 100
cases = int(input())
for i in range(cases):
    N, V1, V2, W = map(int, input().split())
    votes_remaining = N-V1-V2
    votes_needed = math.floor(N/2) - V1 + 1
    if votes_needed > votes_remaining:
        print("RECOUNT!")
    elif votes_needed <= 0:
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    elif chance_of_getting(votes_needed, votes_remaining) > W:
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    else:
        print("PATIENCE, EVERYONE!")