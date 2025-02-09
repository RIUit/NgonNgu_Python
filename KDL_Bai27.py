# Làm tròn số
'''Cho một số thực a, hãy tìm số nguyên gần a nhất.
 Trong trường hợp phần thực của a = 0.5 thì làm tròn lên    '''

from math import *
#Nhap vao so thuc a
a=float(input())

#Processing va output
if a - int(a) >= 0.5 :
    print(ceil(a))
else:
    print(int(a))