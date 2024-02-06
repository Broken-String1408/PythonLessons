# Тестирование

from task45 import sum_div, friendly_nums
from unittest import TestCase

class TestTask45(TestCase):
    def test_sum_div(self):
        self.assertEqual(sum_div(220), 284, 'Сумма делителей числа 220 должна быть равна 284')
        self.assertEqual(sum_div(284), 220)
    def test_friendly_nums(self):
        self.assertEqual(friendly_nums(300), [(220, 284)])
        # 1184 и 1210
        self.assertEqual(friendly_nums(1300), [(220, 284), (1184, 1210)])