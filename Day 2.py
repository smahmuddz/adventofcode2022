r=["".join(l.strip().split()) for l in open("solution.txt","r")]
r1 = {"AX":4,"AY":8,"AZ":3,"BX":1,"BY":5,"BZ":9,"CX":7,"CY":2,"CZ":6}
r2 = {"AX":3,"AY":4,"AZ":8,"BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7}
print(sum([r1[i] for i in r]))
print(sum([r2[i] for i in r]))

