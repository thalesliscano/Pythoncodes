num_itens1 = int(input())
tamap1 = list(map(int,input().split()))
# tamap1 = [11111,11222,12333,12444, 13555]

num_itens2 = int(input())
tamisd = list(map(int,input().split()))
# tamisd = [11101,11222,12333,12401]

ap1_isd = []

for i in tamap1:
  for j in tamisd:
    if i == j:
      ap1_isd.append(i)
print(ap1_isd)  