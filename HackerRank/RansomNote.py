

def checkMagazine(magazine, note):
    dict={}
    for i in range(0,len(magazine)):
        if(magazine[i] not in dict.keys()):
            dict[magazine[i]]=1
            continue
        dict[magazine[i]]+=1
    for i in range(0,len(note)):
        if(note[i] not in dict.keys()):
            print('No')
        if(dict[note[i]]<=0):
            print('No')
        dict[note[i]]-=1
    print('Yes')