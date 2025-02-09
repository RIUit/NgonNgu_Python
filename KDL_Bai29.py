# Cấp số nhân
'''Cho 4 số a, b, c, d. Hãy kiểm tra xem 4 số này có thể theo 
thứ tự tạo thành 1 cấp số nhân với công bội nguyên theo đúng thứ tự a, b, c, d hay không?       '''

#Nhap vao day so 
a,b,c,d = map(int,input().split())

#Processing va output
if b % a == 0 :
    
    q = b // a

    if b * q == c and c * q == d :
        print('YES')
    else:
        print('NO')

else:
    print('NO')