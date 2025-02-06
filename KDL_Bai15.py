#  Mua nước
''' 
Anh ta cần mua chính xác n lít nước.
Chỉ có hai loại chai nước 1 lít và chai 2 lít.
Có vô số chai của hai loại này trong cửa hàng.
Chai loại 1 có gía a burles và chai loại 2 có giá tương ứng b burles.
Anh muốn chi càng ít tiền càng tốt.
Tìm ra số tiền tối thiểu (bằng burles)?,Anh cần mua chính xác n lít nước ở cửa hàng  '''

#Nhap vao n lit nuoc,gia chai loai 1 lit va loai 2 lit :
n,a,b=map(int,input().split())

#Prossing
if a < b /2 :
    print(n*a)
else:
    if n % 2 == 0 :
        print(n//2 *b)
    else:
        print((n-1) // 2 * b + a)