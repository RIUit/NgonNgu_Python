# Đường đi ngắn nhất
'''Hôm nay Patrick chờ đợi một chuyến thăm từ người bạn SpPal của mình.
 Để chuẩn bị cho chuyến thăm, Patrick cần mua một số quà tặng ở hai cửa hàng gần nhà. 
 Có một con đường dài d1 mét giữa nhà anh ta và cửa hàng đầu tiên và một con đường dài d2 mét giữa nhà anh ta và cửa hàng thứ hai.
 Ngoài ra, có một con đường dài d3 kết nối trực tiếp hai cửa hàng này với nhau. 
 Giúp Patrick tính toán khoảng cách tối thiểu mà anh ta cần đi bộ để đến cả hai cửa hàng và trở về nhà. 
 Patrick luôn bắt đầu tại nhà của mình. Anh ta nên ghé thăm cả hai cửa hàng chỉ di chuyển dọc 
 theo ba con đường hiện có và trở về nhà của anh ta.
 Anh ta không ngại ghé thăm cùng một cửa hàng hoặc đi qua cùng một con đường nhiều lần.
 Mục tiêu duy nhất là giảm thiểu tổng quãng đường đã đi.                                        '''

#Nhap vao d1 d2 d3
d1,d2,d3=map(int,input().split())

#Processing va output
print(min(d1+d2+d3,2*(d1+d2),2*(d2+d3),2*(d3+d1)))