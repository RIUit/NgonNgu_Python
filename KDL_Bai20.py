# Lát đá quảng trường
''' Quảng trường Nhà kích thước n × m mét 
    Mỗi viên đá hình vuông có kích thước a × a.
     Số lượng viên đá ít nhất cần thiết để lát Quảng trường là bao nhiêu?
(Nó được phép che phủ bề mặt lớn hơn Quảng trường Nhà hát.
 Nó không được phép phá vỡ các viên đá. Các cạnh của viên đá phải song song với các cạnh của Quảng trường.)   '''

#Nhap kich thuoc cua Quang truong:
n,m,a=map(int,input().split())

#Processing
x,y=0,0

 # Xét cột đứng là lẻ hay chẳn
if n % a == 0 :
    x = n // a
else:
    x = n // a + 1

 # Xét cột ngang là lẻ hay chẳn
if m % a == 0 :
    y = m // a
else: 
    y = m // a + 1

#Output:
print(x*y)