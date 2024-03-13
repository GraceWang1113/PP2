import sys

sys.path.append("..")

import pytest
from python.Calc import calculator
import yaml


class TestCalc():
    def setup_method(self):
        self.cc = calculator()

    #加法：正常数值、非数值型字符
    @pytest.mark.parametrize(("a", "b", "c"), [(0, 0, 0), (60, 77, 137), (-1, -2, -3), (-1, 6, 5), (1.2, 4.3, 5.5)])
    def test_add_case01(self, a, b, c):
        result = self.cc.calc_add(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b"), [("a", "b"), ("a", 0), (-1, "b")])
    def test_add_case02(self, a, b, ):
        with pytest.raises(TypeError) as e:
            self.cc.calc_add(a, b)
        assert e.type == TypeError
        assert "can't add str" in str(e.value)

    #减法：正常数值、非数值型字符
    @pytest.mark.parametrize(("a", "b", "c"), [(0, 0, 0), (77, 60, 17), (-1, -2, 1), (-1, 6, -7), (6.6, 3.3, 3.3)])
    def test_sub_case01(self, a, b, c):
        result = self.cc.calc_sub(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b"), [("a", "b"), ("a", 0), (-1, "b")])
    def test_sub_case02(self,a,b):
        with pytest.raises(TypeError) as e:
            self.cc.calc_sub(a,b)
        assert e.type == TypeError

    #乘法：正常数值、非数值型字符
    @pytest.mark.parametrize(("a", "b", "c"), [(0, 0, 0), (77, 60, 4620), (-1, -2, 2), (-1, 6, -6), (6.8, 7.3, 49.64)])
    def test_mul_case01(self, a, b, c):
        result = self.cc.calc_mul(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b"), [("a", "b"), ("a", 0), (-1, "b")])
    def test_mul_case02(self,a,b):
        with pytest.raises(TypeError) as e:
            self.cc.calc_mul(a,b)
        assert e.type == TypeError
        assert "can't mul str" in str(e.value)


    #除法：正常数值、非数值型字符、除数为0
    @pytest.mark.parametrize(("a", "b", "c"), [(80, 2, 40), (-1, -2, 0.5), (-12, 6, -2), (6.6, 3.3, 2),(9,-3,-3),(100,33,3.03),(128,3,42.667)])
    def test_div_case01(self, a, b, c):
        result = self.cc.calc_div(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b"), [("a", "b"), ("a", 0), (-1, "b")])
    def test_div_case02(self,a,b):
        with pytest.raises(TypeError) as e:
            self.cc.calc_div(a,b)
        assert e.type == TypeError

    def test_div_case03(self):
        with pytest.raises(ZeroDivisionError) as e:
            self.cc.calc_div(1,0)
        assert e.type == ZeroDivisionError
        assert "division by zero" in str(e.value)

if __name__ == '__main__':
    pytest.main(["-v", "-s","test_calc.py"])
