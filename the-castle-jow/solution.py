def deCasteljau(t,controles):
  # P = (1-t)A + tB
  size = len(controles)
  if size == 1:
    return controles[0]
  novos = []
  for i in range(size-1):
    A = controles[i]
    B = controles[i+1]
    point = ((1-t)*A[0]+t*B[0],(1-t)*A[1]+t*B[1])
    novos.append(point)
  return deCasteljau(t,novos)
  

n = int(input())
controles = []
for i in range(n):
  controles.append(tuple(map(int,input().split())))
qtdT = int(input())
for i in range(qtdT):
  t = float(input())
  print("{0:.2f}".format(round(deCasteljau(t,controles)[0],2)),end = ' ')
  print("{0:.2f}".format(round(deCasteljau(t,controles)[1],2)))  
