def minimumBribes(Q):
    # Counting number of bribes taken by an individual
    moves = 0 

    for i,P in enumerate(Q):
        # i is the current position of P, 
        # P is the original position of P

        # if any P is more than two ahead of 
        # its original position
        if P - i > 2:
            return "Too chaotic"
        
        # Anyone who bribed P cannot get to higher than
        # one position in front of P's original position
        # if q bribes p(person in front of q) than q will be at pth position
        # and if again q bribes r(person in front of p) q will be at (p-1)th position

        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    return moves

for _ in range(int(input())):
    n=int(input())
    
    print(minimumBribes(list(map(lambda e: int(e)-1,input().split()))))