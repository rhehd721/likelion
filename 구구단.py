# 2020.06.15
# 작성자 = 20143208 박병호

a = []
for i in range(2,10):
  a.append(i)

for j in range(0,8):
  k=1
  print('\n')
  print(a[j],'단')
  while k < 10:
    print(a[j],'*',k,'=',a[j]*k," ", end='')
    k=k+1