# Bizon the champion
'''Bizon the Champion được gọi là Champion vì một lý do.
 Bizon the Champion gần đây đã có một món quà - một tủ kính mới với
n kệ và anh quyết định đặt tất cả những món quà của mình ở đó. Tất cả các món quà có thể được
chia thành hai loại: huy chương và cúp. Bizon the Champion có a1 cúp giải nhất, a2 cúp giải nhì
và a3 cúp giải ba. Bên cạnh đó, anh có b1 huy chương giải nhất, b2 huy chương giải nhì và b3 huy chương giải ba.

Đương nhiên, phần thưởng trong tủ phải sắp xếp cho thật 
đẹp, đó là lý do Bizon the Champion quyết định tuân theo các quy tắc:
Bất kỳ kệ nào cũng không thể chứa cả cúp và huy chương cùng một lúc;
Không có kệ có thể chứa nhiều hơn năm cúp;
Không có kệ có thể có hơn mười huy chương.
Giúp Bizon the Champion tìm hiểu xem chúng tôi có thể đặt tất cả các phần thưởng 
để tất cả các điều kiện được đáp ứng hay không.             '''

#Nhap vao so cup giai c1 c2 c3 va huy chuong giai h1 h2 h3
c1,c2,c3,h1,h2,h3=map(int,input().split())
n=int(input()) # số k

#Tinh tong so cup , tong so huy chuong
cup=c1+c2+c3
hc=h1+h2+h3
ke1,ke2=0,0
if cup % 5 == 0 :
    ke1= cup // 5
else:
    ke1= cup // 5 +1
if hc % 10 == 0 :
    ke2= hc // 10
else:
    ke2= hc // 10 + 1
if ke1 + ke2 <= n :
    print('YES')
else:
    print('NO')