#!/usr/bin/env python3
"""Module defining CountedIterator:
a subclass of a real iterator that counts how many items are iterated.
"""


class CountedIterator:
    """An iterator that wraps another iterator and counts items fetched."""

    def __init__(self, iterable):
        """Initialize with an iterable and set the counter to zero."""
        self._iterator = iter(iterable)  # store the real iterator
        self._count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self  # required for for-loops and iteration protocols

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self._iterator)  # may raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self._count
