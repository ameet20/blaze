from dynd import nd

from .core import DataDescriptor

class Python(DataDescriptor):
    def __init__(self, storage=None, schema=None, dshape=None):
        self.storage = storage if storage is not None else []
        self._schema = schema
        self._dshape = dshape

    def _extend(self, seq):
        self.storage.extend(seq)

    def _iter(self):
        return iter(self.storage)

    def _getitem(self, key):
        return self.storage[key]
