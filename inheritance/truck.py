"""Truck class - inherits from Vehicle."""

from __future__ import annotations
from vehicle import Vehicle


class Truck(Vehicle):
    """A truck: larger vehicle with cargo capacity."""

    def __init__(self, make: str, model: str, year: int, capacity_tons: float = 1.0) -> None:
        super().__init__(make, model, year)
        self.capacity_tons = float(capacity_tons)

    def horn(self) -> str:
        """Override the horn sound for trucks."""
        return "HONK!"

    def load(self, tons: float) -> None:
        """Load cargo onto the truck."""
        if tons < 0:
            raise ValueError("tons must be non-negative")
        if tons > self.capacity_tons:
            raise ValueError("Exceeds truck capacity")
        # in a more complete example we would track load state; here it's a no-op

    def info(self) -> str:
        """Extend parent info to include capacity."""
        base = super().info()
        return f"{base} - Truck(capacity={self.capacity_tons}t)"
