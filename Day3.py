import string

#Part One
letters=list(string.ascii_letters)
fun={}
for i in range(1,53,1):
    fun[letters[i-1]]=i
f=open("input_d3.txt").read().split('\n')
a=[]
for i in f:
    z=(list(set(i[0:len(i)//2])&set(i[len(i)//2:len(i)])))
    a.append(z[0])
print('Solve 1: ',sum(fun[i] for i in a))

#Part Two
b=[]
for i in range(0,len(f),3):
    z=list(set(f[i]) & set(f[i+1]) & set(f[i+2]))
    b.append(z[0])
print('Solve 2:',sum(fun[i] for i in b))