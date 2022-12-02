import sys
load=sorted([sum([int(n) for n in l.split('\n')]) for l in open("input.txt").read().split('\n\n')])
print(max(load))
print(sum(load[-3:]))
