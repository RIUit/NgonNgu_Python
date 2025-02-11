# Ghép số
'''Gần đây Anton tìm thấy một hộp có chữ số trong phòng của mình. Có k2 chữ số 2, k3 chữ số 3,
k5 chữ số 5 và k6 chữ số 6. Số nguyên yêu thích của Anton là 32 và 256. Anh quyết định soạn số 
nguyên này từ các chữ số anh có. Anh ta muốn làm cho tổng của các số nguyên này càng lớn càng tốt. 
Giúp anh ta giải quyết nhiệm vụ này! Mỗi chữ số có thể được sử dụng không quá một lần, tức là các 
số nguyên tổng hợp nên chứa không quá k2 chữ số 2, k3 chữ số 3, v.v. Tất nhiên, các chữ số không 
sử dụng không được tính vào tổng.           '''
#INPUT:Dòng duy nhất của đầu vào chứa bốn số nguyên k2, k3, k5 và k6 - số chữ số 2, 3, 5 và 6 tương ứng
#OUTPUT:In một số nguyên-tổng số tối đa có thể có của các số nguyên yêu thích của Anton có thể được tạo bằng các chữ số từ hộp.

#Nhập vào số lần chữ số 2 3 5 6
k2,k3,k5,k6 = map(int,input().split())

#Tim so lan kep thanh 256
k256 = min(k2,k5,k6)

#Tim so lan kep thanh 32
k32 = min(k3,k2 - k256)

#OUTPUT: Tổng số lần ghép thành 256 và 32
print(k256 * 256 + k32 * 32)