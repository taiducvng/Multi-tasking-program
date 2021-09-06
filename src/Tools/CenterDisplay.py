from tkinter import *


def makecenter(root):
    """Vì mỗi màn hình có độ phân giải khác nhau, do đó chúng ta không thể cài đặt các giá trị tĩnh cho việc hiển thị hộp thoại của 
    chương trình ở giữa màn hình nên việc lấy chiều cao và chiều rộng của màn hình ở mỗi máy là cần thiết, và việc chúng ta cần 
    làm là lấy 1 nửa độ dài màn hình trừ 1 nữa độ dài geometry của chương trình hiện lên. """
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))