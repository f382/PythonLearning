"""Unit tests to characterize python collections"""
from collections import ChainMap, Counter, defaultdict
import heapq
import copy


class TestCollections:
    """Unit tests to characterize python collections"""

    def test_chainmap(self):
        chain_map = ChainMap({'x': 0, 'y': 1}, {'z': 2})
        assert chain_map['z'] == 2
        chain_map.maps.append({'x': 3})
        assert chain_map.parents['x'] == 3
        assert chain_map.new_child({'z': -1})['z'] == -1

    def test_counter(self):
        counter = Counter(['x', 'x', 'y'])
        assert counter == Counter(
            {'x': 2, 'y': 1, 'z': 0}) == Counter(w=0, x=2, y=1)
        counter['x'] += 1
        assert counter['x'] == 3
        assert counter['w'] == 0
        assert list(counter.elements()) == ['x', 'x', 'x', 'y']
        assert counter.total() == 4
        assert counter.most_common() == counter.most_common(2) == [
            ('x', 3), ('y', 1)]
        counter.subtract({'x': 2})
        counter.update({'y': 1})
        counter['z'] = -1
        assert +counter == Counter(['x', 'y', 'y'])

    def test_defaultdict(self):
        list_dict = defaultdict(list)
        assert list_dict['x'] == []
        list_dict['y'].append(0)
        assert list_dict['y'] == [0]

    def test_heapq(self):
        heapq.heapify(heap := [])
        heapq.heappush(heap, 2)
        heapq.heappush(heap, 1)
        assert heapq.heappushpop(heap, 3) == 1
        assert heapq.heapreplace(heap, 0) == 2
        assert heapq.heappop(heap) == 0
        assert heap == [3]
        assert list(heapq.merge(heap, [1])) == [1, 3]
        assert heapq.nsmallest(1, heap) == [3]

    def test_copy(self):
        my_list = [0, 1, 2]
        assert copy.copy(my_list) == my_list.copy() == my_list[:] == my_list

    def test_deepcopy(self):
        my_list = [0, 1, 2]
        assert copy.deepcopy(my_list) == my_list
