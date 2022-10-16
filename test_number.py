"""Unit tests to characterize python numbers"""

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

    def test_divmod(self):
        assert divmod(23, -7) == (-4, -5)
