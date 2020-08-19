# https://leetcode.com/discuss/interview-question/759687/CodeNation-Online-Coding-Assessment-Questions#

a = 5*10**5
x = 10**10

finalLi=[]


class NumTree:
    def __init__(self, num, lessThan, prev_node):
        self.num = num
        self.lessThan = lessThan
        self.prev = prev_node

    def getVal(self) -> int:
        curr = self
        retV = 0
        i=0
        while curr != None:
            retV += curr.num*(10**i)
            curr = curr.prev
            i+=1
        return retV

    def __repr__(self) -> str:
        return str(self.getVal())


def getNextLevel(curr: NumTree, skip0=False):
    global a,finalLi
    ret = []
    for i in range(1 if(skip0) else 0, 10):
        if(i ** 2 <= curr.lessThan):
            a -= 1
            finalLi.append(NumTree(i, curr.lessThan-i**2, curr))
            ret.append(NumTree(i, curr.lessThan-i**2, curr))
            if(a == 0):
                print(finalLi[-1])
                return None
        else:
            break
    return ret


try:
    print(finalLi[a-1])
except:
    finalLi.clear()
    li = (getNextLevel(NumTree(0, x, None), True))
    while True:
        nextLi = []
        try:
            for node in li:
                nextLi += (getNextLevel(node))
        except:
            # print(finalLi)
            break
        li = nextLi

