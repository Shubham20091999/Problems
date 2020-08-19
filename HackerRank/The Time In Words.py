# https://www.hackerrank.com/challenges/the-time-in-words/problem

toWord = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine',  'ten',  'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

toWord.append('twenty')

for i in range(1,10):
    toWord.append('twenty '+toWord[i])

toWord.append('half')

h = int(input())
m = int(input())

past = True
if(m > 30):
    m = 60-m
    past = False

if(m == 0):
    print(toWord[h]+' '+'o\' clock')
elif(m == 1):
    print(toWord[m]+' minute', end=' ')
elif(m != 15 and m != 30):
    print(toWord[m] + ' minutes', end=' ')
else:
    print(toWord[m], end=' ')
if(m != 0):
    if(past):
        print('past '+toWord[h])
    else:
        print('to '+toWord[(h+1) % 12])
