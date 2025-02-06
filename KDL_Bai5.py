# Tính Khoảng cách Euclid
from math import *
#Nhap toa do 2 diem
x1,y1,x2,y2=map(int,input().split())

#Tinh khoang cach 2 diem toa do
s=sqrt(pow((x1-x2),2)+pow((y1-y2),2)) # s=sqrt((x1-x2)**2 + (y1-y2)**2)

#In ra
print('%.2f' % s)