"""Unit tests to characterize python collections"""
from collections import ChainMap, Counter


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
