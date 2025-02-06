#Số ngày của tháng ?
    #Cho biết tháng và năm, hãy in ra số ngày tương ứng có trong tháng đó. Chú ý tháng 2 của năm nhuận có 29 ngày.

#Nhap vao thang va nam
thang,nam=map(int,input().split())

#Prossing
if thang > 0 and thang < 13 and nam > 0 :
    if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12 :
        print('31')
    elif thang==4 or thang==6 or thang==9 or thang==11 :
        print('30')
    else:
        if(nam % 400 == 0 or (nam % 4 == 0 and nam % 100 !=0)) :
            print('29')
        else:
            print('28')
else:
    print('INVALID')