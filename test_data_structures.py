"""Unit tests to characterize python data structures"""
import pytest


class TestDataStructures:
    """Unit tests to characterize python data structures"""

    @pytest.fixture
    def my_triple(self) -> tuple:
        return (0, 1, 2)

    @pytest.fixture
    def my_list(self) -> list:
        return [0, 1, 2]

    @pytest.fixture
    def my_set(self) -> set:
        return {0, 1, 2}

    @pytest.fixture
    def my_dict(self) -> dict:
        return {0: 'a', 1: 'b', 2: 'c'}

    @pytest.fixture
    def my_value_list(self) -> list:
        return ['a', 'b', 'c']

    def test_create_empty(self):
        assert not ()
        assert not []
        assert not set()
        assert not {}

    def test_convert_tuple_list(self, my_triple: tuple, my_list: list):
        assert list(my_triple) == my_list
        assert tuple(my_list) == my_triple

    def test_convert_list_set(self, my_list: list, my_set: set):
        assert set(my_list) == my_set
        assert list(my_set) == my_list

    def test_convert_list_dict(self, my_list: list, my_value_list: list, my_dict: dict):
        assert dict(zip(my_list, my_value_list)) == my_dict
        assert list(my_dict) == list(my_dict.keys()) == my_list
        assert list(my_dict.items()) == list(zip(my_list, my_value_list))
        assert list(my_dict.values()) == my_value_list

    def test_convert_set_dict(self, my_set: set, my_dict: dict):
        assert set(my_dict) == set(my_dict.keys()) == my_set
        assert dict.fromkeys(my_set, 'x') == {0: 'x', 1: 'x', 2: 'x'}

    def test_comprehend_set(self, my_set):
        assert {i for i in range(10) if i < 3} == my_set

    def test_comprehend_dict(self, my_dict):
        assert {i: 'abc'[i] for i in range(3)} == my_dict

    def test_set_from_range(self, my_set):
        assert set(range(3)) == my_set

    def test_frozenset_from_set(self, my_set):
        assert frozenset(my_set) == frozenset((0, 1, 2))

    def test_type(self, my_triple: tuple, my_list: list, my_set: set, my_dict: dict):
        assert isinstance(my_triple, tuple)
        assert isinstance(my_list, list)
        assert isinstance(my_set, set)
        assert isinstance(my_dict, dict)

    def test_nonempty(self, my_triple: tuple, my_list: list, my_set: set, my_dict: dict):
        assert my_triple
        assert my_list
        assert my_set
        assert my_dict

    def test_length(self, my_triple: tuple, my_list: list, my_set: set, my_dict: dict):
        assert len(my_triple) == len(my_list) == len(
            my_set) == len(my_dict) == 3

    def test_access_dict(self, my_dict: dict):
        assert my_dict[1] == 'b'

    def test_change_dict(self, my_dict: dict):
        del my_dict[1]
        my_dict[2] = 'z'
        my_dict[3] = 'w'
        assert my_dict == {0: 'a', 2: 'z', 3: 'w'}

    def test_change_set(self, my_set: set):
        my_set.remove(1)
        my_set.discard(1)
        my_set.discard(2)
        my_set.add(3)
        assert my_set == {0, 3}

    def test_copy(self, my_list: list, my_set: set, my_dict: dict):
        assert list(my_list) == my_list
        assert set(my_set) == my_set
        assert dict(my_dict) == my_dict

    def test_in_set(self, my_set: set):
        assert 1 in my_set
        assert 3 not in my_set

    def test_in_dict(self, my_dict: dict):
        assert 1 in my_dict
        assert 3 not in my_dict

    def test_clear(self, my_list: list, my_set: set, my_dict: dict):
        my_list.clear()
        my_set.clear()
        my_dict.clear()
        assert my_list == []
        assert my_set == set()
        assert my_dict == {}

    def test_union(self, my_set: set, my_dict: dict):
        assert my_set | {3, 4, 5} == {0, 1, 2, 3, 4, 5}
        assert my_dict | {3: 'd', 4: 'e', 5: 'f'} == {0: 'a',
                                                      1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}

    def test_intersect(self, my_set: set):
        assert my_set & {0, 2, 4} == {0, 2}

    def test_difference(self, my_set: set):
        assert my_set - {1, 2, 4} == {0}

    def test_symmetric_difference(self, my_set: set):
        assert my_set ^ {1, 2, 4} == {0, 4}

    def test_dict_pop(self, my_dict: dict):
        assert my_dict.pop(1) == 'b'
        assert my_dict == {0: 'a', 2: 'c'}

    def test_popitem(self, my_set: set, my_dict: dict):
        key = my_set.pop()
        assert key in {0, 1, 2}
        assert len(my_set) == 2
        key, val = my_dict.popitem()
        assert key in {0, 1, 2}
        assert val in {'a', 'b', 'c'}
        assert len(my_dict) == 2

    def test_flatten(self, my_set: set, my_dict: dict):
        assert {*my_set, 3, 4} == {0, 1, 2, 3, 4}
        assert {**my_dict, 3: 'd', 4: 'e'} == {0: 'a',
                                               1: 'b', 2: 'c', 3: 'd', 4: 'e'}

    def test_dict_get(self, my_dict: dict):
        assert my_dict.get(1) == 'b'
        assert my_dict.get(3) is None
        assert my_dict.get(3, -1) == -1

    def test_dict_setdefault(self, my_dict: dict):
        assert my_dict.setdefault(1) == 'b'
        assert my_dict.setdefault(3) is None
        assert my_dict.setdefault(5, -1) == -1

    def test_dict_update(self, my_dict: dict):
        my_dict.update({0: 'x', 3: 'w'})
        assert my_dict == {0: 'x', 1: 'b', 2: 'c', 3: 'w'}

    def test_dict_reversed(self, my_dict: dict):
        assert list(reversed(my_dict)) == [2, 1, 0]

    def test_isdisjoint(self, my_set: set):
        assert my_set.isdisjoint({3, 4, 5})

    def test_issubset(self, my_set: set):
        assert my_set <= {0, 1, 2, 3}
        assert my_set > {1, 2}
