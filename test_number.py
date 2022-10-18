"""Unit tests to characterize python numbers"""

import math
import pytest


class TestNumber:
    """Unit tests to characterize python numbers"""

    @pytest.fixture
    def i(self) -> complex:
        return 1.0j

    def test_int_literals(self):
        assert 2147483647 == 0x7fffffff == 0o17777777777 == 0b1111111111111111111111111111111
        assert 1000000 == 1_000_000

    def test_float_literals(self):
        assert 0.0 == .0 == 0. == 0e0

    def test_complex_number(self, i):
        assert +i == 1.0j
        assert -i == -1.0j
        assert i.real == 0.0
        assert i.imag == 1.0
        assert i.conjugate() == -1.0j
        assert abs(i) == 1.0
        assert i ** 2 == -1.0

    def test_number_truth(self):
        assert -0.3j
        assert not 0

    def test_integer_division(self):
        assert 7 // 3 == 2

    def test_power(self):
        assert 3 ** 4 == 81

    def test_round(self):
        assert round(3.1415926536, 2) == 3.14

    def test_abs(self):
        assert abs(-15) == 15

    def test_divmod(self):
        assert divmod(23, -7) == (-4, -5)

    def test_bin(self):
        assert bin(27) == '0b11011'

    def test_hex(self):
        assert hex(27) == '0x1b'

    def test_oct(self):
        assert oct(27) == '0o33'

    def test_float(self):
        assert float(3) == 3.0

    def test_int(self):
        assert int(3.14) == 3

    def test_bool(self):
        assert bool(3)

    def test_int_from_base(self):
        assert int('11', 9) == 10

    def test_pow_neg_mod(self):
        assert pow(3, -2, 7) == 4

    def test_bit_length(self):
        assert (6).bit_length() == 3

    def test_bit_count(self):
        assert (6).bit_count() == 2

    def test_trunc(self):
        assert math.trunc(-2.718) == -2

    def test_floor(self):
        assert math.floor(2.718) == 2

    def test_ceil(self):
        assert math.ceil(3.142) == 4

    def test_as_integer_ratio(self):
        assert 1.25.as_integer_ratio() == (5, 4)

    def test_is_integer(self):
        assert 7.0.is_integer()

    def test_none_false(self):
        assert not None
