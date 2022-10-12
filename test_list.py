"""Unit tests to characterize python data structures"""

from functools import reduce
import pytest

class TestList:
    """Unit tests to characterize python lists"""

    @pytest.fixture
    def my_list(self) -> list:
        return [0, 1, 2]

    def test_create(self, my_list: list):
        assert [0, 1, 2] == my_list

    def test_length(self, my_list: list):
        assert len(my_list) == 3

    def test_from_tuple(self, my_list: list):
        my_tuple = (0, 1, 2)
        assert list(my_tuple) == my_list

    def test_from_range(self, my_list: list):
        my_range = range(3)
        assert list(my_range) == my_list

    def test_comprehend(self, my_list: list):
        assert [i for i in range(10) if i < 3] == my_list

    def test_access(self, my_list: list):
        assert my_list[1] == 1

    def test_access_backwards(self, my_list: list):
        assert my_list[-2] == 1

    def test_mutate(self, my_list: list):
        my_list[1] = -1
        assert my_list == [0, -1, 2]

    def test_delete(self, my_list: list):
        del my_list[1]
        assert my_list == [0, 2]

    def test_concatenate(self, my_list: list):
        assert my_list + [3, 4, 5] == [0, 1, 2, 3, 4, 5]

    def test_append(self, my_list: list):
        my_list.append(3)
        assert my_list == [0, 1, 2, 3]

    def test_copy(self, my_list: list):
        assert my_list[:] == my_list

    def test_slice(self, my_list: list):
        assert my_list[1:-1] == [1]
        assert my_list[-2:] == [1, 2]
        assert my_list[:2] == [0, 1]

    def test_slice_assign(self, my_list: list):
        my_list[1:] = [2, 4]
        assert my_list == [0, 2, 4]
        my_list[-2:-1] = [1, 2, 3]
        assert my_list == [0, 1, 2, 3, 4]
        my_list[:2] = []
        assert my_list == [2, 3, 4]

    def test_flatten(self, my_list: list):
        assert [-2, -1, *my_list, 3, 4] == [-2, -1, 0, 1, 2, 3, 4]

    def test_type(self, my_list: list):
        assert isinstance(my_list, list)

    def test_reverse(self, my_list: list):
        my_list.reverse()
        assert my_list == [2, 1, 0]

    def test_get_reversed(self, my_list: list):
        assert list(reversed(my_list)) == [2, 1, 0]

    def test_delete_slice(self, my_list: list):
        del my_list[1:2]
        assert my_list == [0, 2]

    def test_clear(self, my_list: list):
        del my_list[:]
        assert my_list == []

    def test_extend(self, my_list: list):
        my_list.extend([3, 4, 5])
        assert my_list == [0, 1, 2, 3, 4, 5]

    def test_index(self, my_list: list):
        assert my_list.index(1) == 1

    def test_pop(self, my_list: list):
        assert my_list.pop() == 2
        assert my_list == [0, 1]

    def test_remove(self, my_list: list):
        my_list.remove(1)
        assert my_list == [0, 2]

    def test_sort(self, my_list: list):
        my_list.sort()
        assert my_list == [0, 1, 2]

    def test_count(self, my_list: list):
        assert my_list.count(1) == 1

    def test_insert(self, my_list: list):
        my_list.insert(1, 0.5)
        assert my_list == [0, 0.5, 1, 2]

    def test_in(self, my_list: list):
        assert 1 in my_list

    def test_equals(self, my_list: list):
        assert my_list == [0, 1, 2]

    def test_compare(self, my_list: list):
        assert my_list < [0, 1, 3]

    def test_multiply(self, my_list: list):
        assert my_list * 2 == [0, 1, 2, 0, 1, 2]

    def test_sum(self, my_list: list):
        assert sum(my_list) == 3

    def test_enumerate(self, my_list: list):
        assert list(enumerate(my_list)) == [(0, 0), (1, 1), (2, 2)]

    def test_zip(self, my_list: list):
        assert list(zip(my_list, ['a', 'b', 'c'])) == [(0, 'a'), (1, 'b'), (2, 'c')]

    def test_max(self, my_list: list):
        assert max(my_list) == 2

    def test_iter(self, my_list: list):
        it = iter(my_list)
        assert next(it) == 0
        assert next(it) == 1
        assert next(it) == 2
        with pytest.raises(StopIteration):
            next(it)
