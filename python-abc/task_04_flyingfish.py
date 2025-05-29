#!/usr/bin/env python3
"""Module illustrating multiple inheritance with FlyingFish."""

class Fish:
    """Represents a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat info."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat info."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish inheriting from Fish and Bird."""

    def fly(self):
        """Override fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print(FlyingFish.mro())
