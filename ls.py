import os, ast
fnames={}
i=0
for filenames in os.listdir('./source'):
  fnames[i]=filenames
  i+=1
print(fnames)


print('\n\n\n TESTING: \n\n\n')

f=open('order.txt', 'r')
for i in f:
  order=i.replace('\n', '')
order = ast.literal_eval(order)

print(order[1])



i=0
smashm={}
s = open('smash.txt','r')
for line in s:
    nline=line.replace('\n','')
    smashm[i] = nline
    i+=1
print(smashm)