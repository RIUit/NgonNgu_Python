# Kiểm tra chữ cái
'''Nhap một kí tự, bạn hãy kiểm tra kí tự nhập vào là chữ cái in hoa, in thường, chữ số hay kí tự đặc biệt
     (các kí tự không phải là chữ cái và chữ số)
     In hoa in ra "UPPER". 
     In thường in ra "LOWER". 
     Chữ số in ra "DIGIT". 
    Kí tự đặc biệt in ra "SPECIAL".                         '''

#Nhap vao ky tu
c=input()
if c.islower() :
    print('LOWER')
elif c.isupper() :
    print('UPPER')
elif c.isdigit() :
    print('DIGIT')
else:
    print('SPECIAL')