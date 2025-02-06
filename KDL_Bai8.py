#Nhập vào 2 số nguyên, in ra tổng, hiệu, tích, thương(lấy độ chính xác với 4 chữ số) của 2 số đó.

#Nhap DL
a,b=map(int,input().split())

#Prossing va IN ra kq
print(a+b)
print(a-b)
print(a*b)
if b==0 :
    print('INVALID')
else:
 print('%.4f' % (a/b))
