#Luyện tập viết câu điều kiện

#Nhap vao so nguyen duong
n=int(input())

#Tinh cac truong hop

#1.La so chan ?
if(n%2==0):
 print('YES')
else: print("NO")

#2.La so chia het cho 3 va 5 ?
if n%3==0 and n%5==0 :
 print('YES')
else: print('NO')

#3.La so chi het cho 3 ma ko chia het cho 7 ?
if n%3==0 and n%7!=0 :
 print('YES')
else: print('NO')

#4.La so chia het cho 3 or chia het cho 7
if n%3==0 or n%7==0 :
 print('YES')
else: print('NO')

#5.La so lon hon 30 va be hon 50
if n>30 and n<50 :
 print('YES')
else: print('NO')

#6.La so ko be hon 30 va chia het cho 1 trong 2,3,5
if n>=30 and (n%2==0 or n%3==0 or n%5==0) :
 print('YES')
else: print('NO')

#7.La so co 2 chu so va chu so tan cung la so nguyen to ?
res=n%10
if n>=10 and n<=99 and (res==2 or res==3 or res==5 or res==7) :
 print('YES')
else: print('NO')

#8.n ko vuot qua 100 va chia het cho 23 ko ?
if n<=100 and n%23==0 :
 print('YES')
else: print('NO')

#9.N không thuộc đoạn [10, 20]?
if n<10 or n>20 :
 print('YES')
else: print('NO')

#10.N có chữ số tận cùng là bội số của 3?
if res%3==0 :
 print('YES')
else: print('NO')