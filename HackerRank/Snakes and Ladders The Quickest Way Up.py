# https://www.hackerrank.com/challenges/the-quickest-way-up/problem

def start(snakes, ladders):
    # BFS slightly modified
    openNodes = [1]
    rolls = [float('inf')]*101
    rolls[1] = 0
    while(len(openNodes)!=0):
        p = openNodes.pop(0)
        for i in range(p+6, p,-1):
            if(i > 100):
                continue
            if(i in snakes):
                i=snakes[i]
            if(i in ladders):
                i=ladders[i]
            if(rolls[i] == float('inf')):
                rolls[i] = min(rolls[p]+1,rolls[i])
                openNodes.append(i)
    return rolls[100] if(rolls[100]!=float('inf')) else -1


for _ in range(int(input())):
    ladder = {}
    for _ in range(int(input())):
        l, r = map(int, input().split())
        ladder[l] = r
    snake = {}
    for _ in range(int(input())):
        l, r = map(int, input().split())
        snake[l] = r

    print(str(start(snake, ladder)))