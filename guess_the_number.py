#test code
import random, math
random.seed()
x = math.floor(random.random()*100)+1
z = 0
b = 0
while x != z:
    b=b+1
    z = int(input("Guess My Number: "))
    if z < x: print("Higher!")
    if z > x: print("Lower!")
print("Correct! " + str(b) + " tries.")
