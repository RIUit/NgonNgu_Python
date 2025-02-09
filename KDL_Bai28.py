#  Cấp số cộng
'''Cho cấp số cộng có n phần tử, cho biết phần tử đầu tiên trong dãy là u1 và công sai d.
Hãy tính tổng các phần tử của cấp số cộng này.          '''
 #Nhap vao n phan tu, u1 , d
n,u1,d = map(int,input().split())

#Processing:
un = u1 + (n-1) * d
s = n * (u1 + un) // 2

#Output
print(s)