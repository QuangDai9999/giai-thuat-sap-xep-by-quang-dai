from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_sapxep_click(self, **event_args):
        # Nhận danh sách từ text box và chuyển đổi thành danh sách số nguyên
        arr_input = self.box_nhapphantu.text.split()
        
        # Kiểm tra số lượng phần tử
        if len(arr_input) != int(self.box_nhapn.text):
            raise ValueError("Lỗi: Số lượng phần tử không đúng!")
            return  # Dừng việc sắp xếp nếu số lượng không đúng

        arr = [int(x) for x in arr_input]

        # Sắp xếp và hiển thị kết quả
        self.box_truockhisapxep.text = "Dãy số nguyên trước khi sắp xếp: " + ' '.join(map(str, arr))

        sorted_arr = arr.copy()
        self.insertion_sort(sorted_arr)
        self.box_InsertionSort.text = "Insertion Sort: " + ' '.join(map(str, sorted_arr))

    # Hàm sắp xếp chèn
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key