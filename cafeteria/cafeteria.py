n = int(input())
impostores_index = []
nomes = []
dist = [n]*n
for i in range(n):
  classe, nome = input().split()
  nomes.append(nome)
  if classe == 'IMPOSTOR':
    impostores_index.append(i)
    dist[i] = 0


for impostor in impostores_index:
  for i in range(1,n):
    index_right = (impostor+i)%n
    index_left = (impostor-i)%n
    if i < dist[index_right]:
      dist[index_right] = i
    if i < dist[index_left]:
      dist[index_left] = i

maxdst = max(dist)
ans = []
for i in range(n):
  if maxdst == dist[i]:
    print(nomes[i])
