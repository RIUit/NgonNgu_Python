# Tổ hợp chập 2 của N
'''Trong lớp có N sinh viên, muốn chọn ra 2 bạn sinh viên để tham gia cuộc thi khiêu vũ, 
hỏi có bao nhiêu cách?          '''

#Nhap vao so hoc sinh
n = int(input())

#Processing va Output
print(n * (n-1) // 2)
# Chu y : nCk   =  n!   /  k!*(n-k)!
