#Ký tự kế tiếp
'''
Cho kí tự là chữ cái in hoa hoặc in thường,
in ra kí tự kế tiếp sau nó trong bảng chữ cái ở dạng in thường,
tức là kí tự nhập vào ở dạng in hoa hay in thường thì bạn đều in ra kí tự kế tiếp nó nhưng ở dạng in thường.
Coi kí tự kế tiếp của của chữ Z là chữ A.
'''
# A-> Z : 65-> 90
# a-> z : 97-> 122
#0-> 9 : 48-> 57

# ord() : chuyển ký tự sang mã ASCI
# chr() : chuyển mã ASCI sang ký tự 

#Nhap ki tu
kytu=input()

#Prossing
if kytu == 'z' or kytu =='Z' :
    print('a')
else:
    tam=ord(kytu)
    tam+=1
    print(chr(tam).lower()) #lower chuyen ky tu sang ky tu thuong
    