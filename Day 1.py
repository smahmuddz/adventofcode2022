load=sorted([sum([int(n) for n in l.split('\n')]) for l in open("input_d1.txt").read().split('\n\n')])
print('Solve 1: ',load[-1],'\nSolve 2: ',sum(load[-3:]))