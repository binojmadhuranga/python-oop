"""Base Vehicle class for inheritance practice."""

from __future__ import annotations


class Vehicle:
    """Base class for vehicles."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0  # protected attribute (convention)

    def accelerate(self, increase: float) -> None:
        """Increase speed by `increase` (non-negative)."""
        if increase < 0:
            raise ValueError("increase must be non-negative")
        self._speed += increase

    def brake(self, decrease: float) -> None:
        """Decrease speed by `decrease` but not below zero."""
        if decrease < 0:
            raise ValueError("decrease must be non-negative")
        self._speed = max(0, self._speed - decrease)

    @property
    def speed(self) -> float:
        """Current speed (read-only property)."""
        return self._speed

    def horn(self) -> str:
        """Return the horn sound (can be overridden)."""
        return "Beep!"

    def info(self) -> str:
        """Return a short descriptive string for the vehicle."""
        return f"{self.year} {self.make} {self.model} (speed={self._speed})"
