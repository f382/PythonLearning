"""Unit tests to characterize python strings"""

from datetime import date


class TestString:
    """Unit tests to characterize python lists"""

    def test_string_literals(self):
        str1 = 'string'
        str2 = "string"
        str3 = ("str"
                "ing")
        str4 = """\
string\
"""
        assert str1 == str2 == str3 == str4

    def test_string_escaping(self):
        str1 = '\n'
        str2 = '\x0A'
        str3 = '\u000A'
        str4 = chr(10)
        assert str1 == str2 == str3 == str4

    def test_string_raw(self):
        str1 = r'C:\DOS'
        str2 = 'C:\\DOS'
        assert str1 == str2

    def test_string_formatting(self):
        name = "Bob"
        assert f"{name}" == "Bob"
        assert f"{name!r}" == repr(name) == "'Bob'"
        value, width, prec = 3.1415926536, 8, 5
        assert f"{value:{width}.{prec}}" == "  3.1416"
        my_date = date(2001, 1, 1)
        assert f"{my_date:%B %d, %Y}" == "January 01, 2001"
        num = 100
        assert f"{num:#0x}" == "0x64"
        assert f"{name=}" == "name='Bob'"
        assert f"{name=!r:20}" == "name='Bob'               "
        my_dict = {'x': 1}
        assert f"{my_dict['x']}" == "1"

    def test_bytes_literal(self):
        assert b"bytes" == bytes(ord(c) for c in "bytes")

    def test_string_encode(self):
        assert "ABC".encode() == bytes([65, 66, 67])

    def test_string_decode(self):
        assert bytes([65, 66, 67]).decode() == 'ABC'

    def test_type(self):
        assert isinstance("string", str)

    def test_length(self):
        assert len("abcdef") == 6
