BLANK = object()
from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class Hashtable:
    def __init__(self, capacity):
        self.pairs = capacity * [BLANK]

    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __delitem__(self, key):
        if key in self:
            self.pairs[self._index(key)] = None
        else:
            raise KeyError(key)


    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % len(self)
