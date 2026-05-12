from dataclasses import dataclass

@dataclass
class Confine:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    def __hash__(self):
        return hash((self.state1no, self.state2no))

    def __eq__(self, other):
        return self.state1no == other.state1no and self.state2no == other.state2no

    def __str__(self):
        return str(self.state1ab) + " - " + str(self.state2ab)

