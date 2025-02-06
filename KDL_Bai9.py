# Kiểm tra năm nhuận ?
  # Năm nhuận là năm chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100)

#Nhap vao 1 nam
n=int(input())

#Prossing
if n%400==0 or (n % 4 == 0 and n % 100 != 0) :

    #OUTPUT:
    print('YES')
else:
      #OUTPUT:
    print('NO')