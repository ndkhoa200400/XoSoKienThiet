Nguyễn Đăng Khoa  
MSSV: 18127121  
Trường Đại học Khoa Học Tự Nhiên - HCMC  
Bộ môn: Mạng máy tính  
# XoSoKienThiet
### App dò xổ số kiến thiết
### Ngôn ngữ: Python  
- Giao thức TCP
- Xử lý đa luồng
- Sử dụng tkinter làm giao diện
- Socket  
- SQLite  

### Cách thi hành  
- Mở file scr/server.py  
- Sau đó mở scr/customer.py  
- Có thể chịu được 5 customers cùng một lúc  

### Ngữ cảnh:
Công ty Xổ số kiến thiết muốn thực hiện một chương trình hỗ trợ người dùng trong
việc tra cứu kết quả xổ số hàng ngày. Người dùng sử dụng một chương trình client kết
nối đến server của công ty để nhận kết qủa. Có hai hình thức nhận kết quả như sau:
- Người dùng gửi tên tỉnh thành, hệ thống trả về kết quả tất cả các giải của tỉnh đó
(nếu tỉnh thành đó có mở thưởng).
- Người dùng gửi tên tỉnh thành và số vé, hệ thống tra cứu và trả về kết quả vé số
đó có trúng giải không, nếu trúng thì giải mấy, số tiền bao nhiêu.
### Yêu cầu:
#### a. Server:
- Nhận kết nối từ client
- Nhận truy vấn từ client
- Tìm kiếm và trả về kết quả cho client
#### b. Client:
- Kết nối đến server
- Gửi nội dung truy vấn đến server
- Nhận kết quả truy vấn và hiện thị kết quả.

##### Xem thêm file PDF để hiểu rõ yêu cầu
