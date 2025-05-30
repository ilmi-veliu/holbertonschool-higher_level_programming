#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""

class SwimMixin:
    """Mixin that adds swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly."""

    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
