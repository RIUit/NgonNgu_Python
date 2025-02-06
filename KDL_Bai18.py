#Chuyển đổi in hoa in thường

#Nhap ky tu
c=input()

#Processing
if c.islower():
    print(c.upper())
elif c.isupper():
    print(c.lower())
else:
    print(c)