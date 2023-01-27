from math import ceil


class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other) -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(
            (self.hour + (self.minute + minutes) // 60) % 24,
            (self.minute + minutes) % 60,
        )

    def __sub__(self, minutes):
        return Clock(
            (self.hour - ceil(-((self.minute - minutes) / 60))) % 24,
            (self.minute - minutes) % 60,
        )
