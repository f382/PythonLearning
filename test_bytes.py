"""Unit tests to characterize python bytes and bytearrays"""

import struct


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

    def test_pack(self):
        assert struct.pack('<xc1b?lL4s', b'\xFF', 32, True, -1000, 3000,
                           b'abcd') == bytes.fromhex('00 FF 20 01 18FCFFFF B80B0000 61626364')

    def test_unpack(self):
        assert struct.unpack('<xc1b?lL4s', bytes.fromhex('00 FF 20 01 18FCFFFF B80B0000 61626364')) == (
            b'\xFF', 32, True, -1000, 3000, b'abcd')
