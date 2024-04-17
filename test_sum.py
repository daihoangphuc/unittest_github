import unittest  
from sum import sum  

class TestSum(unittest.TestCase):  # Khai báo lớp kiểm thử, kế thừa từ unittest.TestCase

    def test_sum_positive_numbers(self):  # Định nghĩa test case kiểm tra với số dương
        self.assertEqual(sum(1, 2), 3, "Kết quả phải là 3")

    def test_sum_negative_numbers(self):  # Định nghĩa test case kiểm tra với số âm
        self.assertEqual(sum(-1, -2), -3, "Kết quả phải là -3")  

    def test_sum_mixed_numbers(self):  # Định nghĩa test case kiểm tra với số hỗn hợp
        self.assertEqual(sum(-1, 2), 1, "Kết quả phải là 1") 

    def test_sum_zero(self):  # Định nghĩa test case kiểm tra với số 0
        self.assertEqual(sum(0, 0), 0, "Kết quả phải là 0") 

    def test_sum_large_numbers(self):  # Định nghĩa test case kiểm tra với số lớn
        self.assertEqual(sum(1000000, 2000000), 3000000, "Kết quả phải là 3000000") 

    def test_sum_float_numbers(self):  # Định nghĩa test case kiểm tra với số thập phân
        self.assertAlmostEqual(sum(0.1, 0.2), 0.3, places=1, msg="Kết quả phải là 0.3")  


if __name__ == '__main__':  # Kiểm tra nếu script được chạy trực tiếp
    unittest.main()  # Chạy tất cả các test case trong lớp TestSum
