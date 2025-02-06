#Số lớn nhất và nhỏ nhất

#Nhap 2 so nguyen a,b
a,b=map(int,input().split())

#số thứ 1 là số lớn nhất <= a mà chia hết cho b
res1=a//b *b
print(res1)
# số thứ 2 là số nhỏ nhất >=a mà chia hết cho b
if a%b==0 :
    print(a)
else:
    print(res1 +b)