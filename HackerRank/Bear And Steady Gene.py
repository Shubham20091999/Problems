# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

def steadyGene(gene):
    dic = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in gene:
        dic[i] += 1
    x = len(gene)
    factor = x/4

    if dic['A'] == factor and dic['T'] == factor and dic['C'] == factor and dic['G'] == factor:
        return 0

    upper = 0
    lower = 0
    minlen = x

    # This is comparing every upper and lower pair with which the freq.
    # of ATCG outside this is less than or equal to the factor required
    # and saving the minimum of these length

    # This is because we can always increase the number of char needed outside the 
    # substring by changing some char inside the substring but cannot increase it
    while upper < x:
        while (dic['A'] > factor or dic['C'] > factor or dic['T'] > factor or dic['G'] > factor) and upper < x:
            dic[gene[upper]] -= 1
            upper += 1
        while dic['A'] <= factor and dic['C'] <= factor and dic['T'] <= factor and dic['G'] <= factor:
            dic[gene[lower]] += 1
            lower += 1
        if upper - lower < minlen:
            minlen = upper-lower+1
    print(dic)
    print(gene[lower:upper])
    return minlen


n=int(input())
print(steadyGene(input()))
