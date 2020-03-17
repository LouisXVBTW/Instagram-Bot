from time import strftime
import os, ast, random, insta, time
def main():
  print(strftime("%H"))
  i=4
  photos=getphotos()
  caption=getcaption()
  #upload(photos, i)
  #time.sleep(27660)
  while 1:
    # 08:00 post
    upload(photos, i)
    i+=1
    time.sleep(14400)
    
    # 12:00 post
    upload(photos, i)
    i+=1
    time.sleep(18000)
    
    # 17:00 post
    print("hour is ",strftime("%H"))
    upload(photos, i)
    i+=1
    time.sleep(18000)
    
    # 22:00 post
    print("hour is ",strftime("%H"))
    upload(photos, i)
    i+=1
    time.sleep(36000)

    
  
  
def upload(photos, cappos):
  done=getdone()
  caption=getcaption()
  var = False
  while var == False:
    rand = random.randint(0,347)
    if photos[rand] in done:
      pass
    else:
      print(photos[rand])
      uploadimg = insta.upload(photos[rand], caption=caption[cappos])
      updatedone(photos[rand])
      return True
  #print(photos, done, caption)
  
def getphotos():
  f=open('order.txt', 'r')
  for i in f:
    order=i.replace('\n', '')
  order = ast.literal_eval(order)
  f.close()
  return order

def getdone():
  d = open('done.txt','r')
  done=[]
  for line in d:
      nline=line.replace('\n','')
      done.append(nline)
  d.close()
  return done
def updatedone(fname):
  d = open('done.txt','a')
  nl = fname+'\n'
  d.write(nl)
  d.close()
def getcaption():
  i=0
  smashm={}
  s = open('smash.txt','r')
  for line in s:
      nline=line.replace('\n','')
      smashm[i] = nline
      i+=1
  s.close()
  return smashm
  
  
  
if __name__ == '__main__':
  main()