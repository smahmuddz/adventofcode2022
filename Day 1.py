f = open("1.txt", "r")
sum=0;
load=[]

for line in f:
  if (line.strip()):
    sum+=int(line)
  else:
      load.append(sum)
      sum=0
print(max(load))      

load.sort(reverse=True)
print(load[0]+load[1]+load[2])
