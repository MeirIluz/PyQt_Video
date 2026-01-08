from dataclasses import dataclass


@dataclass
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        self.count += 1

    def decrement(self) -> None:
        self.count -= 1

    def reset(self) -> None:
        self.count = 0
