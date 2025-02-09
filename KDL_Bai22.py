# Đồng xu
'''Bạn có số lượng xu không giới hạn với các giá trị 1,2,3,……n (từ 1 tới n). 
   Bạn muốn chọn một số bộ tiền có tổng giá trị S. Nó được phép có nhiều đồng tiền có cùng giá trị trong tập hợp. 
   Số lượng đồng xu tối thiểu cần thiết để có được tổng S là bao nhiêu?                                               '''

#Nhap vao 2 so nguyen n:gia tri xu va S:Tong so xu
n,s=map(int,input().split())

#Processing
if s % n == 0 :
    print(s // n)
else:
    print(s // n + 1)