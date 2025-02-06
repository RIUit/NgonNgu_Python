# Đổi ngày sang năm, tuần, ngày
    # Cho trước N ngày, hãy đổi N thành số năm, số tuần và số ngày. Biết rằng một năm có 365 ngày.

#Nhap DL
n=int(input())

#Prossing
nam = n // 365
n = n % 365
tuan = n // 7
n = n % 7

#Output:
print(nam,tuan,n)