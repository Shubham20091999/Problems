
def matchingStrings(strings, queries):
    ans=[0]*len(queries)
    for i in range(len(queries)):
        for j in range(len(strings)):
            if(strings[j]==queries[i]):
                ans[i]+=1
                strings.pop(i)
    return ans


