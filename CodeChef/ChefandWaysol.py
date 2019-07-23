from math import inf, log
from heapq import heappush, heappop
from sys import stdin, stdout

def process_input():
    [n, k] = map(int, stdin.readline().split())
    spec = to_list(stdin.readline())
    stdout.write(str(process_case(n, k, spec)) + '\n')

def process_case(n, k, spec):
    precs = [None] * n
    max_i = -1
    spec2 = list(map(log, spec))
    heap = []
    heappush(heap, (spec2[0], -1, 0))
    while True:
        (dist, prec, i) = heappop(heap)
        if precs[i] == None:
            precs[i] = prec
            if i == n - 1:
                return compute_dist(n - 1, precs, spec) % 1000000007
            elif i > max_i :
                max_i = i
                for j in range(i + 1, min(i + k + 1, n)):
                    heappush(heap, (dist + spec2[j], i, j))

def to_list(string):
    return list(map(int, string.split()))

def compute_dist(n, precs, spec):
    dist = 1
    while n != -1:
        dist *= spec[n]
        n = precs[n]
    return dist
    
process_input()