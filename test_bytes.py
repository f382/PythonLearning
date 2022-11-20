"""Unit tests to characterize python bytes and bytearrays"""


class TestBytes:
    """Unit tests to characterize python bytes and bytearrays"""

    def test_create_bytes(self):
        assert bytes(4) == bytes((0, 0, 0, 0)) == bytes(
            bytearray(b'\x00\x00\x00\x00')) == b'\x00\x00\x00\x00'

    def test_create_bytearray(self):
        assert bytearray() == bytearray([])
        assert bytearray(4) == bytearray(
            [0, 0, 0, 0]) == bytearray(b'\x00\x00\x00\x00')

    def test_bytes_hex(self):
        assert bytes.fromhex('7fff') == b'\x7F\xFF'
        assert b'\x7F\xFF'.hex() == '7fff'

    def test_bytearray_hex(self):
        assert bytearray.fromhex('7fff') == bytearray(b'\x7F\xFF')
        assert bytearray(b'\x7F\xFF').hex() == '7fff'
