"""Car class - inherits from Vehicle."""

from __future__ import annotations
from vehicle import Vehicle


class Car(Vehicle):
    """A car: small passenger vehicle."""

    def __init__(self, make: str, model: str, year: int, doors: int = 4) -> None:
        super().__init__(make, model, year)
        self.doors = doors

    def horn(self) -> str:
        """Override the horn sound for cars."""
        return "Honk honk!"

    def info(self) -> str:
        """Extend parent info to include doors."""
        base = super().info()
        return f"{base} - Car({self.doors} doors)"
