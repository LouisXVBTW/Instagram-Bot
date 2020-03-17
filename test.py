from InstagramAPI import InstagramAPI
from time import strftime
import os
import random


info={}
with open("info.txt") as f:
  for line in f:
      (key, val) = line.split()
      info[key] = val

#print (info)
#print(info["username"])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

 # login
fnames={}
smashm={}
i=0
for filenames in os.listdir('./source'):
  fnames[i]=filenames
  i+=1
print(fnames)
i=0
si=2
s = open('smash.txt','r')
for line in s:
    nline=line.replace('\n','')
    smashm[i] = nline
    i+=1
i=1
s.close()
print(smashm)
d = open('done.txt','r')
done=[]
for line in d:
    nline=line.replace('\n','')
    done.append(nline)
d.close()
print(done)
while 1:
  time1=strftime('%H')
  if time1 == '8':
    print(time1)

    
    if fnames[i] in done:
      pass
    else:
      done.append(fnames[i])
      d = open('done.txt','a')
      cont=fnames[i]+'\n'
      d.write(cont)
      d.close()
      
    
      path = 'source/'+fnames[i]
      print(path)
      si+=1
      InstagramAPI = InstagramAPI(info["username"], info["password"])
      InstagramAPI.login() 
      InstagramAPI.uploadPhoto(path, caption=smashm[si])
      print("uploaded!")
      print("waiting on next")
      while 1:
        if time1 == '8':
          pass
        else:
          break
      
  if time1 == '12':
    print(time1)

    
    if fnames[i] in done:
      pass
    else:
      done.append(fnames[i])
      d = open('done.txt','a')
      cont=fnames[i]+'\n'
      d.write(cont)
      d.close()
      
    
      path = 'source/'+fnames[i]
      print(path)
      si+=1
      InstagramAPI = InstagramAPI(info["username"], info["password"])
      InstagramAPI.login() 
      InstagramAPI.uploadPhoto(path, caption=smashm[si])
      print("uploaded!")
      print("waiting on next")
      while 1:
        if time1 == '12':
          pass
        else:
          break
          
  if time1 == '17':
    print(time1)

    
    if fnames[i] in done:
      pass
    else:
      done.append(fnames[i])
      d = open('done.txt','a')
      cont=fnames[i]+'\n'
      d.write(cont)
      d.close()
      
    
      path = 'source/'+fnames[i]
      print(path)
      si+=1
      InstagramAPI = InstagramAPI(info["username"], info["password"])
      InstagramAPI.login() 
      InstagramAPI.uploadPhoto(path, caption=smashm[si])
      print("uploaded!")
      print("waiting on next")
      while 1:
        if time1 == '17':
          pass
        else:
          break

