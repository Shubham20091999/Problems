# https://www.hackerrank.com/challenges/organizing-containers-of-balls/forum

# 1) Make a table of box totals (capacity of each box)
# 2) Make a table of ball totals (total quantity of each ball type)
# 3) Sort both tables
# 4) If they are identical print Possible, otherwise print Impossible

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())

    # Number of balls in a container
    containers = [0]*n
    # Number of each types of ball
    balls = [0]*n

    for i in range(n):
        inp = list(map(int, input().split()))
        containers[i] = sum(map(int, inp))
        for n in range(len(inp)):
            balls[n] += inp[n]
    # Checking if the number of balls of a specific type and number of balls in each container satisfy
    containers.sort()
    balls.sort()
    if containers == balls:
        print("Possible")
    else:
        print("Impossible")
