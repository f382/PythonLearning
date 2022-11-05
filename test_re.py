"""Unit tests to characterize python regular expressions"""

import re
from re import Pattern

import pytest


class TestRE:
    """Unit tests to characterize python regular expressions"""

    @pytest.fixture
    def regex1(self) -> Pattern:
        return re.compile(r'(?i)^[A-F]+.?\s{1,3}[^\w\s]*(?:a|b)$', re.M | re.S)

    @pytest.fixture
    def regex2(self) -> Pattern:
        return re.compile(r'(\d++).+?(?!\W)\b(.+)\1\W\2\Z')

    @pytest.fixture
    def regex3(self) -> str:
        return r'\b\s+'

    @pytest.fixture
    def string1(self) -> str:
        return 'acDB, \t-~/;a'

    @pytest.fixture
    def string2(self) -> str:
        return '0495_A=a0495!a'

    @pytest.fixture
    def string3(self) -> str:
        return 'foo  bar\t\v\fqux fnord'

    def test_match(self, regex1: Pattern, regex2: Pattern, string1: str, string2: str):
        assert regex1.match(string1)
        assert not regex1.match('FUDGE')
        assert isinstance(regex2.match(string2), re.Match)
        assert regex2.match('FUDGE') is None

    def test_search(self, regex2: Pattern, regex3: str, string2: str, string3: str):
        string_with_prefix = 'PR' + string2
        assert not regex2.match(string_with_prefix)
        assert regex2.search(string_with_prefix)
        assert re.search(regex3, string3, re.NOFLAG)

    def test_fullmatch(self, regex1: Pattern, string1: str):
        string_with_suffix = string1 + '\nS'
        assert regex1.match(string_with_suffix)
        assert not regex1.fullmatch(string_with_suffix)

    def test_split(self, regex3: str, string3: str):
        assert re.split(regex3, string3, 2, re.NOFLAG) == [
            'foo', 'bar', 'qux fnord']

    def test_findall(self, regex2: Pattern, string2: str, regex3: str, string3: str):
        assert regex2.findall(string2) == [('0495', 'a')]
        assert re.findall(regex3, string3) == ['  ', '\t\v\f', ' ']

    def test_finditer(self, regex2: Pattern, string2: str, regex3: str, string3: str):
        assert [m.expand(r'\1') for m in regex2.finditer(string2)] == ['0495']
        assert [m.group(0) for m in re.finditer(
            regex3, string3)] == ['  ', '\t\v\f', ' ']
