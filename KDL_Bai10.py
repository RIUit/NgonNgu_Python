#Tam giác hợp lệ ?

#Nhap vao 3 canh cua mot tam giac
a,b,c=map(int,input().split())

#Prossing
if a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b :
    print('YES')
else: 
    print('NO')
