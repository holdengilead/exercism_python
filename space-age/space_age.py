"""
https://exercism.org/tracks/python/exercises/space-age
"""

from dataclasses import dataclass
from typing import Callable, Dict

SECONDS_YEAR: int = 31557600
PLANETS: Dict[str, float] = {
    "earth": 1.0,
    "jupiter": 11.862615,
    "mars": 1.8808158,
    "mercury": 0.2408467,
    "neptune": 164.79132,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "venus": 0.61519726,
}


@dataclass
class SpaceAge:
    """
    Intercept the call method, and return the function to calculate the space age in
    that planet.
    """

    seconds: int

    def __getattr__(self, planet: str) -> Callable[[], float]:
        def method() -> float:
            return round(self.seconds / SECONDS_YEAR / PLANETS[planet.split("_")[1]], 2)

        return method
