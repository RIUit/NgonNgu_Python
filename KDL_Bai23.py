# Doremon leo cầu thang
'''Doremon muốn leo lên một cầu thang gồm n bước.
   Anh ta có thể leo 1 hoặc 2 bước mỗi lần di chuyển.
   Doremon muốn số lần di chuyển là bội số của một số nguyên m.
   Số lượng di chuyển tối thiểu làm cho anh ta leo lên đỉnh cầu thang thỏa mãn điều kiện của anh ta là gì?          '''
#Nhap vao n va m
n,m= map(int,input().split())

#Processing
min_step,max_step=0,n
if n % 2 == 0 :
    min_step = n // 2
else:
    min_step = n // 2 + 1
res= (min_step + m - 1) // m * m
if res <= max_step :
    print(res)
else:
    print(-1)