def gcd(a,b): #MDC de 2
  if a == 0:
    return abs(b)
  return gcd(b%a,a)

def lcm(lst): ## MMC da lista
  ans = lst[0]
  for i in range(1,len(lst)):
    current = lst[i]
    ans = abs(current*ans)/gcd(current,ans)
  return ans

def fat(n):
  if n == 1 or n == 0:
    return 1
  return n*fat(n-1)  

def gcdL(lst): # MDC da lista
  a = lst[0]
  for i in range(1,len(lst)):
    b = lst[i]
    a = gcd(a,b)
  return a  


def solve():
  n = int(input())
  l = list(map(int,input().split()))
  mmc = lcm(l)
  mdc = gcdL(l)
  return mmc,mdc,n


if __name__ == '__main__':
  qtd = int(input())
  for i in range(qtd):
    mmc,mdc,size = solve()
    if mdc == 1 or mmc == mdc:
      print("Numeros feios")
    else:
      razao = mmc/mdc
      print("Numeros magicos! "+str(fat(size)+razao))
