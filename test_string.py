"""Unit tests to characterize python strings"""

import textwrap
from datetime import date


class TestString:
    """Unit tests to characterize python strings"""

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

    def test_from_int(self):
        assert str(9) == '9'

    def test_to_int(self):
        assert int('9') == 9

    def test_type(self):
        assert isinstance("string", str)

    def test_nonempty(self):
        assert 'abcdef'
        assert not ''

    def test_length(self):
        assert len("abcdef") == 6

    def test_iterate(self):
        assert list("0123") == ['0', '1', '2', '3']

    def test_join(self):
        assert ','.join(['0', '1', '2', '3']) == '0,1,2,3'

    def test_split(self):
        assert '0,1,2,3'.split(',') == ['0', '1', '2', '3']
        assert '0 1 2 3'.split() == ['0', '1', '2', '3']

    def test_partition(self):
        assert '0,1,2,3'.partition(',') == ('0', ',', '1,2,3')

    def test_splitlines(self):
        assert '0\n1\n2\n3\n'.splitlines() == ['0', '1', '2', '3']

    def test_strip(self):
        assert ' x '.strip() == 'x'
        assert ' x '.lstrip() == 'x '
        assert ' x '.rstrip() == ' x'

    def test_count(self):
        assert 'xxx'.count('x') == 3

    def test_find(self):
        assert 'xxx'.find('x') == 0
        assert 'xxx'.rfind('x') == 2

    def test_replace(self):
        assert 'xxx'.replace('x', 'y') == 'yyy'

    def test_removeprefix_suffix(self):
        assert 'xyz'.removeprefix('x') == 'yz'
        assert 'xyz'.removesuffix('z') == 'xy'

    def test_starts_endswith(self):
        assert 'xyz'.startswith('x')
        assert 'xyz'.endswith('z')

    def test_upper_lower(self):
        assert 'xyz'.upper() == 'XYZ'
        assert 'XYZ'.lower() == 'xyz'

    def test_iswhatever(self):
        assert 'xyz'.isascii()
        assert 'xyz'.isalpha()
        assert 'xyz'.isalnum()
        assert 'xyz'.isidentifier()
        assert '123'.isdigit()
        assert '123'.isdecimal()
        assert '123'.isnumeric()
        assert 'xyz'.islower()
        assert 'XYZ'.isupper()
        assert ' \t\n\v\f\n'.isspace()

    def test_indent(self):
        assert textwrap.indent('a\nb\nc\n', '   ') == '   a\n   b\n   c\n'

    def test_dedent(self):
        assert textwrap.dedent('   a\n   b\n   c\n') == 'a\nb\nc\n'
