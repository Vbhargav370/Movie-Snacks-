"""
Movie Snacks
Chef is watching a movie, and during the intermission, wants to get himself some snacks.

A bucket of popcorn costs 
X
X rupees, and a drink costs 
Y
Y rupees.
There is also a combo offer available, which provides one bucket of popcorn and one drink at a cost of 
Z
Z rupees.

Chef wants to buy two buckets of popcorn and three drinks.
What's the minimum amount he needs to pay to do so?
"""
x,y,z = map(int, input().split())
mini = min(x+y, z)
total = (mini*2)+y
print(total)
