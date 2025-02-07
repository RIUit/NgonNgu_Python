# Domino
#Nhap vao m x n sap xep thanh domino 2 x 1 vao day m x n.Tinh so thanh domino

#Nhap vao m x n :
m,n=map(int,input().split())
#Processing:
if n % 2 == 0 :
 print(n // 2 * m)
else:
 print((n-1) // 2 * m + m // 2)
