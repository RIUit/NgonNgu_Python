# Con ếch
'''
Một con ếch hiện đang ở điểm 0 trên trục tọa độ Ox.
    Nó nhảy theo thuật toán sau: bước nhảy thứ nhất là a đơn vị về bên phải,
    bước nhảy thứ hai là b đơn vị về bên trái, bước nhảy thứ ba là a đơn vị bên phải, 
    bước nhảy thứ tư là b đơn vị bên trái, v.v.
Nếu con ếch đã nhảy một số lần chẵn (trước lần nhảy hiện tại),
     nó nhảy từ vị trí hiện tại x sang vị trí x + a, mặt khác, 
     nó nhảy từ vị trí hiện tại x sang vị trí x - b. Nhiệm vụ của bạn là tính toán vị trí của ếch sau k bước nhảy   '''

#Nhap a dv ve phai , b dv ve trai , k so lan buoc
a,b,k = map(int,input().split())

#Processing
right , left = 0 , 0
if k % 2 == 0 :
 right = k // 2
 left = k // 2
else:
left = k // 2
right = left + 1

#Output:
print(right * a - b * left)